import { PrismaClient } from '@prisma/client';
import express from 'express';
import marcaRoutes from './routes/marca.routes.js';
import productRoutes from "./routes/producto.routes.js"
import modelRoutes from "./routes/modelo.routes.js"
import cors from 'cors';

const app = express();

const port = 3000;

// Middleware para poder recibir datos en formato JSON
app.use(cors())
app.use(express.json());


app.use("/api/marca", marcaRoutes)
app.use("/api/producto", productRoutes )
app.use("/api/modelos", modelRoutes)

// app.get("/api/producto-marca", async (req, res) => {
//    const result = await prisma.tb_producto_marca.findMany({
//       include: {   // JOIN 
//          tb_producto: true,
//          tb_marca: true
//       }
//    })
//    res.json(result);
// })



try {
   app.listen(port, () => {
      console.log(`Mi Backend esta funcionando 🔥🎉🦾 `);
      console.log(`http://localhost:${port}/`);
   });
} catch (error) {
   console.log(error);
}