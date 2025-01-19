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

