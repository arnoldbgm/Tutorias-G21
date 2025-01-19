import prisma from "../utils/prismaClient.js";

export const getAllProductos = async (req, res) => {
   try {
      const productos = await prisma.tb_producto.findMany()
      res.json(productos).status(200);
   } catch (error) {
      res.status(500).json({
         msg: "Ocurrio un error al obtener los productos",
         error
      })
   }
}


export const createProducto = async (req, res) => {
   /*
req.body
{
  "nombre":"Audifonos"
}
*/
   const { nombre } = req.body;
   await prisma.tb_producto.create({
      data: {
         nombre: nombre
      }
   })
   res.json({ msg: "Producto creado correctamente" });
}
