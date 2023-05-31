CREATE TABLE persona (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (150)
);

CREATE TABLE departamento (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	fk_persona integer,
	CONSTRAINT depto_frkey FOREIGN KEY (fk_persona) 
	REFERENCES persona (id)
);




INSERT INTO persona (name, last_name) VALUES ('Juan', 'Saldivia');


SELECT * FROM persona;

SELECT * FROM persona WHERE id = 2;

DELETE FROM persona WHERE id = 2;

UPDATE persona SET email = 'algo@algo.com' WHERE id = 15;

select * from departamento d join persona p on (d.fk_persona = p.id) where p.id =1;


mutation{
  createPersona(name: "Tito", lastName: "Ledesma", email: "asds@asd.asd"){
    persona{
      id
      name
      lastName
      email 
    }
  }
}