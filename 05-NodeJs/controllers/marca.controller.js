import prisma from "../utils/prismaClient.js";

export const getAllMarcas = async (req, res) => {
   try {
      const marcas = await prisma.tb_marca.findMany() //SELECT * FROM tb_marca;
      res.json(marcas).status(200);
   } catch (error) {
      res.status(500).json({
         msg: "Ocurrio un error al obtener las marcas",
         error
      })
   }
}

export const createMarca = async (req, res) => {
   /*
   req.body
   {
     "nombre":"Toshiba"
   }
   */
   try {
      const { nombre } = req.body;
      await prisma.tb_marca.create({
         data: {
            nombre: nombre
         }
      });
      res.json({ msg: "Marca creada correctamente" });
   } catch (error) {
      res.status(500).json({
         msg: "Ocurrio un error al crear la marca",
         error
      });
   }
}

