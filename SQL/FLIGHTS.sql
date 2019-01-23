CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES ("Natal", "São Paulo", 200);
INSERT INTO flights (origin, destination, duration) VALUES ("Curitiba", "Fortaleza", 100);
INSERT INTO flights (origin, destination, duration) VALUES ("Rio de Janeiro", "Belo Horizonte", 420);
INSERT INTO flights (origin, destination, duration) VALUES ("Salvador", "Brasília", 220);
 