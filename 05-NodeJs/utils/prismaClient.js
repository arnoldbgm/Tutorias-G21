// Este archivo se encarga de instanciar el cliente de Prisma para realizar las consultas a la base de datos
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export default prisma;