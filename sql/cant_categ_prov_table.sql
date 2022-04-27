CREATE TABLE IF NOT EXISTS cant_categ_prov_table(
    id serial,
    provincia VARCHAR(255) NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    cantidad Integer NOT NULL,
    fecha_ins date,
    PRIMARY KEY(id)
);