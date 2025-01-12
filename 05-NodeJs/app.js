import { PrismaClient } from '@prisma/client';
import express from 'express';
const app = express();

// Instancio mi cliente de Prisma
// Me permite poder usar la ORM de Prisma
const prisma = new PrismaClient();

const port = 3000;

// Middleware para poder recibir datos en formato JSON
app.use(express.json());

// Este va a ser mi endpoint para listar todas las marcas
app.get("/api/marca", async (req, res) => {
   // Prisma.nombreModelo.metodo()
   const marcas = await prisma.tb_marca.findMany() //SELECT * FROM tb_marca;
   res.json(marcas);
})

app.post("/api/marca", async (req, res) => {
   /*
   req.body
   {
     "nombre":"Toshiba"
   }
   */
   const { nombre } = req.body;
   await prisma.tb_marca.create({
      data: {
         nombre: nombre
      }
   })
   res.json({ msg: "Marca creada correctamente" });
})

// RETO 01
// Hacer un endpoint para listar todas los productos
app.get("/api/producto", async (req, res) => {
   const producto = await prisma.tb_producto.findMany()
   res.json(producto);
})

// RETO 02
// Hacer un endpoint para crear un producto
// POST /api/producto
app.post("/api/producto", async (req, res) => {
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
})

app.get("/api/producto-marca", async (req, res) => {
   const result = await prisma.tb_producto_marca.findMany({
      include: {   // JOIN 
         tb_producto: true,
         tb_marca: true
      }
   })
   res.json(result);
})

app.post("/api/modelos", async (req, res) => {
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
 });
 

try {
   app.listen(port, () => {
      console.log(`Mi Backend esta funcionando 🔥🎉🦾 `);
      console.log(`http://localhost:${port}/`);
   });
} catch (error) {
   console.log(error);
}