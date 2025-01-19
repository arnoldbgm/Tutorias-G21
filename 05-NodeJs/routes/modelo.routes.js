import express from "express";
import { createModel, getModelosFiltrados } from "../controllers/modelo.controller.js";

const router = express.Router();

router.get("/filtrados", getModelosFiltrados)
router.post("/", createModel)

export default router;