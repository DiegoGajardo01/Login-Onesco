#ignore, chuleta pa actualizar repo


 git add .
 
 
 git commit -m "text"
 
 
 git push origin main
 
===========================================================================
Login (onesco_login): ID (AI) PK, user varchar(50), pass varchar(50)


(Fijarse en los NOT NULL)


Recepcion Dueño: rut_cliente varchar(10) PK, nombre_cliente varchar(50), contacto varchar(10)


Recepcion auto: chasis varchar(60) PK, patente varchar(45), modelo varchar(45), marca varchar(45), año int, precio int, rut_dueño varchar(10) FK


Autos(where disponible and estado=bueno): disponibilidad, modelo, precio, kilometraje. 


Tecnico: modelo, chasis, estado, piezas utilizadas, precio final compra, precio final venta.


Bodega: dos pestañas, vehiculos- piezas.


Dato del comprador y los datos del auto y el monto pagado con boletas adjuntas. 


El pago será vía efectivo o transacción el cual no se necesita que esté dentro de la aplicación solo el respaldo de ellos. 


===========================================================================


Puntos a seguir ahora:

-Rehacer las consultas de la creación de las tablas(Relacionarlas)


-Rehacer las tablas, y con eso, cambiar la logica de la programación

===========================================================================