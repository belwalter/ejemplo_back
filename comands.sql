CREATE TABLE persona (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (150)
);

INSERT INTO persona (name, last_name) VALUES ('Juan', 'Saldivia');


SELECT * FROM persona;

SELECT * FROM persona WHERE id = 2;