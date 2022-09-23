use mydb;
insert into usuario (ID_Usuario,Nombre,Apellido,Telefono,Correo,Rol,Contraseña) values
	(1,'Felipe','Rodriguez','3','felipe@gmail.com','administrador',123456),
    (2,'Juan','Perez','3','juan@gmail.com','cliente',1234),
    (3,'Stefany','Rodriguez','3','stefany@gmail.com','cliente',3456),
    (4,'Nicolas','Mendez','3','nicolas@gmail.com','cliente',12345),
    (5,'Luisa','Riascos','3','luisa@gmail.com','cliente',23456)
    ;
-- select * from usuario
-- delete from usuario where ID_Usuario

insert into pelicula (ID_Pelicula,Nombre_Pelicula,Descripción,Director,Duración) values
	(1,'Iron Man 2','Al saberse que es Iron Man, el multimillonario inventor Tony Stark sufre presiones para enseñar su tecnología a los militares. Duda en contar los secretos de su traje blindado por si son mal usados. Con Pepper Potts y Rhodes de su lado, forja nuevas alianzas y enfrenta a un enemigo poderoso. Además, ve que no solo hay un loco que busca destruirlo, sino que la tecnología para salvarlo lo mata de a poco.','Jon Favreau','123 minutos'),
    (2,'Bichos una aventura en miniatura','Viaja dentro del mundo de los insectos en miniatura para disfrutar de la diversión y la aventura más allá de la vida debajo de cada hoja. Es una expedición con una pequeña hormiga que busca una banda de guerreros para luchar contra los saltamontes que amenazan su hogar. Se topa con un torbellino de insectos del circo, y su única esperanza de ganar es el vínculo de la amistad y el poder de la imaginación.','John Lasseter','1 h 35minutos'),
    (3,'harry potter y la piedra filosofal','La historia sigue a Harry Potter, un niño que al cumplir once años descubre que es un mago, por lo cual es enviado al Colegio Hogwarts de Magia y Hechicería ...','Chris Columbus','2 h 32 minutos'),
	(4,'El exorcismo de Dios','El exorcismo de Dios presenta una historia que se desarrolla en un pueblo ficticio llamado Nombre de Dios, el cual se encuentra en algún lugar montañoso de México donde Irán Castillo y Will Beinbrink se unieron en una lucha del bien contra el mal',' Alejandro Hidalgo','1h 38minuto')
    ;
-- select * from pelicula
-- delete from pelicula where ID_Pelicula

insert into genero(ID_Genero,Genero) values
	(1,'Accion'),
	(2,'Aventuras'),
	(3,'Ciencia Ficción'),
	(4,'Comedia'),
	(5,'Drama'),
	(6,'Fantasía'),
	(7,'Musical')
	;
-- select * from genero
-- delete from genero where ID_Genero

insert into pelicula_has_genero(Pelicula_ID_Pelicula,Genero_ID_Genero) values
    (1,2)
    ;
    
-- select * from pelicula_has_genero
