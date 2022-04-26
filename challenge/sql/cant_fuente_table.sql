CREATE TABLE IF NOT EXISTS cant_fuente_table(
    id serial,
    fuente VARCHAR(255) NOT NULL,
    cantidad Integer NOT NULL,
    fecha_ins date,
    PRIMARY KEY(id)
);