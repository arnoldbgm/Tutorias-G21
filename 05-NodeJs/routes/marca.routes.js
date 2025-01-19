import express from "express";
import { getAllMarcas } from "../controllers/marca.controller.js";

const router = express.Router();

// Este va a ser mi endpoint para obtener las marcas
// Este enpoint va ir acompañado de un contralador
router.get("/", getAllMarcas)

export default router;