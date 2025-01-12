-- CreateTable
CREATE TABLE "tb_marca" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(255) NOT NULL,

    CONSTRAINT "tb_marca_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "tb_modelos" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(255) NOT NULL,
    "precio" DECIMAL(10,2) NOT NULL,
    "stock" INTEGER NOT NULL,
    "descripcion" TEXT,
    "id_producto_marca" INTEGER NOT NULL,

    CONSTRAINT "tb_modelos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "tb_producto" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(255) NOT NULL,

    CONSTRAINT "tb_producto_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "tb_producto_marca" (
    "id" SERIAL NOT NULL,
    "id_producto" INTEGER NOT NULL,
    "id_marca" INTEGER NOT NULL,

    CONSTRAINT "tb_producto_marca_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "tb_marca_nombre_key" ON "tb_marca"("nombre");

-- CreateIndex
CREATE UNIQUE INDEX "tb_producto_nombre_key" ON "tb_producto"("nombre");

-- AddForeignKey
ALTER TABLE "tb_modelos" ADD CONSTRAINT "tb_modelos_id_producto_marca_fkey" FOREIGN KEY ("id_producto_marca") REFERENCES "tb_producto_marca"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "tb_producto_marca" ADD CONSTRAINT "tb_producto_marca_id_marca_fkey" FOREIGN KEY ("id_marca") REFERENCES "tb_marca"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "tb_producto_marca" ADD CONSTRAINT "tb_producto_marca_id_producto_fkey" FOREIGN KEY ("id_producto") REFERENCES "tb_producto"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
