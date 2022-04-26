# Arquitectura

Se hará mediante esquema cliente/sevidor SQL, en practicamente todos los idiomas de programación hay librerías que implementan esta arquitectura.

## ODBC

Se trata de un estandar de acceso a las bases de datos, se crea una capa intermedia entre aplicación y base de datos, de forma que si se cambia la base de datos no se necesite cambiar la aplicación, en la práctica no es así. Python (pyodbc).
Las conexiones se apoyan en cadenas de caracteres de conexión.

En el curso usaremos el conector oficial de MySql que usa ODBC. 
