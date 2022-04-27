CREATE TABLE IF NOT EXISTS cant_categoria_table(
    id serial NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    cantidad Integer NOT NULL,
    fecha_ins date,
    PRIMARY KEY(id)
);