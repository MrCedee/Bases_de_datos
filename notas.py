import mysql.connector
import os

os.system("cls")
mydb = mysql.connector.connect(
    # Configura la conexión
    host="localhost",
    user="root",
    passwd=""
)


def initDB():
    cursor = mydb.cursor()
    cursor.execute('CREATE SCHEMA IF NOT EXISTS python')
    cursor.execute('USE python')
    # Crea las tablas correspondientes al diagrama notas.png
    tabla_user = """
    CREATE TABLE IF NOT EXISTS  usuarios (
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50),
        PRIMARY KEY (username)
    );
    """
    tabla_notas = """
    CREATE  TABLE IF NOT EXISTS notas (
        id INT AUTO_INCREMENT,
        titulo VARCHAR(250) NOT NULL,
        creada TIMESTAMP NOT NULL,
        cuerpo VARCHAR(1000),
        autor VARCHAR(50) NOT NULL,
        PRIMARY KEY (id),
        CONSTRAINT
            FOREIGN KEY (autor)
            REFERENCES usuarios (username)
            ON DELETE CASCADE
            ON UPDATE CASCADE
    );
    """

    cursor.execute(tabla_user)
    cursor.execute(tabla_notas)



def muestraMenu():
    print('------- MENU -------')
    print('  1. Crear usuario')
    print('  2. Login')
    print('  3. Salir')
    print('--------------------')

def muestraOperaciones(usuario):
    print(f'------- OPERACIONES ({usuario}) -------')
    print('  1. Crear nota')
    print('  2. Listar mis notas')
    print('  3. Filtrar notas por fechas')
    print('  4. Borrar nota')
    print('  5. Logout')
    print('--------------------')


def crearUsuario():

    cursor = mydb.cursor()

    print('------ Registro de usuario ------\n')
    username =  input('Nombre de usuario : ')
    password =  input('Contraseña (¡visible!) : ')

    # Añadir el usuario a la BD

    print('------ Usuario añadido ------\n')

def login():
    username = input("Login: ")
    password = input("Password (¡visible!): ")

    # Comprobar que las credenciales son válidas
    credencialesValidas = ...

    # Si las credenciales son válidas, accedemos al meno principal
    if credencialesValidas:
        opcion = 0
        while opcion != 5:
            muestraOperaciones(username)
            opcion = int(input("Elige una opción : "))
            if opcion == 1:
                crearNota(username)
            elif opcion == 2:
                listarNotas(username)
            elif opcion == 3:
                filtrarNotas(username)
            elif opcion == 4:
                borrarNota(username)

def crearNota(username):
    titulo = input("Titulo: ")
    texto = input("Cuerpo: ")

    # Guardar nota en la BD

def listarNotas(username):
    # Mostrar por pantalla las notas del usuario, ordenadas por fecha de creación decreciente
    pass

def filtrarNotas(username):
    # Mostrar por pantalla las notas del usuario creadas entre dos fechas pedidas por pantalla
    pass

def borrarNota(username):
    # Pide el id de la nota que se quiere borrar y se elimina la fila correspondiente, siempre que la nota sea del usuario <username>
    pass

def run():
    n = 0
    while n != 3:
        muestraMenu()
        n = int(input("Elige una opción : "))
        if n == 1:
            crearUsuario()
        elif n == 2:
            login()
        elif n == 3:
            print('----- ¡Hasta pronto! -----')


if __name__ == '__main__':
    initDB()
    run()
