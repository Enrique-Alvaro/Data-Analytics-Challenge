CREATE TABLE IF NOT EXISTS cine_insights_table(
    id serial NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    pantallas Integer NOT NULL,
    butacas Integer NOT NULL,
    espacio_incaa Integer NOT NULL,
    fecha_ins date,
    PRIMARY KEY(id)
);