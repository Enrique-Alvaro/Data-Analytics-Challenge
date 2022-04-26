CREATE TABLE IF NOT EXISTS base(
    id serial NOT NULL,
    cod_localidad Integer NOT NULL,
    id_provincia Integer NOT NULL,
    id_departamente Integer NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    provincia VARCHAR(255) NOT NULL,
    localidad VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    domicilio VARCHAR(255) NOT NULL,
    codigo VARCHAR(255) NOT NULL,
    numero VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    web VARCHAR(255) NOT NULL,
    fecha_ins date ,
    PRIMARY KEY (id)
);

