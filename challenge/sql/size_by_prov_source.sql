CREATE TABLE IF NOT EXISTS size_prov_source(
    id serial,
    provincia VARCHAR(255) NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    cantidad Integer NOT NULL
);