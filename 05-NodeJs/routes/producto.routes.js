import express from 'express';
import { createProducto, getAllProductos } from '../controllers/producto.controller.js';

const router = express.Router();

router.get("/", getAllProductos)
router.post("/", createProducto)


export default router;