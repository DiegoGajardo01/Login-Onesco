#ignore, chuleta pa actualizar repo


 git add .
 
 
 git commit -m "text"
 
 
 git push origin main
 
===========================================================================
Login (onesco_login): ID (AI) PK, user varchar(50), pass varchar(50)


(Fijarse en los NOT NULL)


Recepcion Dueño (onesco_recepcion_auto): rut_cliente varchar(10) PK, nombre_cliente varchar(50), contacto varchar(10)


Recepcion auto(onesco_recepcion_cliente): chasis varchar(60) PK, patente varchar(45), modelo varchar(45), marca varchar(45), año int, kilometraje int, precio int, precio_final int, estado boolean, rut_dueño varchar(10) FK



===========================================================================


Puntos a seguir ahora:


- Validación de rut cuando ingresa cliente lista, faltaría validar si el rut, está en la tabla o no (cuando ingresa Auto)


- Realizar dentro de recepcion actualizar los datos.


- Recepcion: Agregar "estado" en la visualizacion de la tabla de datos de autos y dejar que muestre el precio final pero q no se pueda editar


- Al eliminar sin datos(ninguna fila seleccionada) se puede corromper el programa


- Crear usuario: Bodega.


- bodega tablas: visualizar y tambien editar: piezas - autos.


- Tecnico, ingresar solamente estado y precio final, ver la tabla de bodega.(autos)


- **agregar imagen de icono y de estetica. ✓**


===========================================================================