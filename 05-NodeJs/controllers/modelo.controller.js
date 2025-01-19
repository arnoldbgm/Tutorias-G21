import prisma from "../utils/prismaClient.js";

export const createModel = async (req, res) => {
   /*
   req.body
   {
     "nombre": "8GB RAM, 1TB HDD",
     "precio": 5000,
     "stock": 10,
     "descripcion": "Buena laptop",
     "marca": "Acer",
     "producto": "Laptop"
   }
   */
   try {
      const { nombre, precio, stock, descripcion, marca, producto } = req.body;

      let newProductMarc = null;

      // Verificar si la marca existe, y sino, crearla
      let marcaUnica = await prisma.tb_marca.findUnique({
         where: { nombre: marca },
      });

      if (!marcaUnica) {
         marcaUnica = await prisma.tb_marca.create({
            data: { nombre: marca },
         });
      }

      // Verificar si el producto existe, y sino, crearlo
      let productoUnico = await prisma.tb_producto.findUnique({
         where: { nombre: producto },
      });

      if (!productoUnico) {
         productoUnico = await prisma.tb_producto.create({
            data: { nombre: producto },
         });
      }

      // Verificar si la relación producto-marca existe, y sino, crearla
      newProductMarc = await prisma.tb_producto_marca.findFirst({
         where: {
            id_marca: marcaUnica.id,
            id_producto: productoUnico.id,
         },
      });

      if (!newProductMarc) {
         newProductMarc = await prisma.tb_producto_marca.create({
            data: {
               id_marca: marcaUnica.id,
               id_producto: productoUnico.id,
            },
         });
      }

      // Crear el modelo relacionado con tb_producto_marca
      const newModel = await prisma.tb_modelos.create({
         data: {
            nombre,
            precio,
            stock,
            descripcion,
            id_producto_marca: newProductMarc.id, // Relación con tb_producto_marca
         },
      });

      res.status(201).json(newModel);
   } catch (error) {
      console.error(error);
      res.status(500).json({ error: "Ocurrió un error en el servidor" });
   }
}


export const getModelosFiltrados = async (req, res) => {
   const { tipo, id } = req.query; // tipo: 'marca' o 'producto', id: el id de la marca o producto

   if (!tipo || !id) {
      return res.status(400).json({ error: 'Faltan parámetros de tipo o id' });
   }

   try {
      let modelos;

      // Filtrar por marca
      if (tipo === 'marca') {
         modelos = await prisma.tb_modelos.findMany({
            where: {
               id_producto_marca: {
                  in: await prisma.tb_producto_marca.findMany({
                     where: { id_marca: parseInt(id) },
                     select: { id: true },
                  }).then((result) => result.map(item => item.id)),
               },
            },
            include: {
               tb_producto_marca: {
                  include: {
                     tb_marca: true, // Incluye la marca relacionada
                     tb_producto: true // Incluye el producto relacionado
                  }
               }
            }
         });
      }
      // Filtrar por producto
      else if (tipo === 'producto') {
         modelos = await prisma.tb_modelos.findMany({
            where: {
               id_producto_marca: {
                  in: await prisma.tb_producto_marca.findMany({
                     where: { id_producto: parseInt(id) },
                     select: { id: true },
                  }).then((result) => result.map(item => item.id)),
               },
            },
            include: {
               tb_producto_marca: {
                  include: {
                     tb_marca: true, // Incluye la marca relacionada
                     tb_producto: true // Incluye el producto relacionado
                  }
               }
            }
         });
      } else {
         return res.status(400).json({ error: 'Tipo no válido. Usa "marca" o "producto"' });
      }

      // Si no se encuentran modelos, retornar un mensaje adecuado
      if (modelos.length === 0) {
         return res.status(404).json({ message: 'No se encontraron modelos con los parámetros proporcionados' });
      }

      // Ahora el resultado incluirá la marca y el producto
      const result = modelos.map(modelo => ({
         id: modelo.id,
         nombre: modelo.nombre,
         precio: modelo.precio,
         stock: modelo.stock,
         descripcion: modelo.descripcion,
         marca: modelo.tb_producto_marca.tb_marca.nombre, // Nombre de la marca
         producto: modelo.tb_producto_marca.tb_producto.nombre // Nombre del producto
      }));

      return res.status(200).json(result);
   } catch (error) {
      console.error(error);
      return res.status(500).json({ error: 'Error en la consulta de modelos' });
   }
};
