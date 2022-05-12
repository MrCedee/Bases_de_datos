import mysql.connector
import os
from datetime import datetime
import time
from mysql.connector.constants import ClientFlag
import os

os.system("cls")
config = {    
    "user":"Use1",
    "password":"HolaBuenasTardes",
    "client_flags":[ClientFlag.SSL],
    "ssl_ca":'Certificados/ca.perm',
    "ssl_cert":'Certificados/client-cert.perm',
    "ssl_key":'Certificados/client-key.perm'}
mydb = mysql.connector.connect(**config)


def initDB():
    cursor = mydb.cursor()
    cursor.execute('CREATE SCHEMA IF NOT EXISTS python')
    cursor.execute('USE python')
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
        creada BIGINT NOT NULL,
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
    os.system("cls")
    print('------- MENU -------')
    print('  1. Crear usuario')
    print('  2. LoginS')
    print('  3. Salir')
    print('--------------------')

def muestraOperaciones(usuario):
    os.system("cls")
    print(f'------- OPERACIONES ({usuario}) -------')
    print('  1. Crear nota')
    print('  2. Listar mis notas')
    print('  3. Filtrar notas por fechas')
    print('  4. Borrar nota')
    print('  5. Logout')
    print('--------------------')

def pedir_fechas():
    print(f'------- FECHAS -------')
    print('  Inserte dos fechas entre las que quiere obtener notas')
    print('-----------------------')


def crearUsuario():

    cursor = mydb.cursor()

    print('------ Registro de usuario ------\n')
    username =  input('Nombre de usuario : ')
    password =  input('Contraseña (¡visible!) : ')

    # Añadir el usuario a la BD
    add_user = """ INSERT INTO python.usuarios
                    VALUES (%s, %s)"""
    cursor.execute(add_user, (username, password))
    mydb.commit()
    os.system("cls")

    print('------ Usuario añadido ------\n')
    time.sleep(5)

def login():
    cursor = mydb.cursor()
    username = input("Login: ")
    password = input("Password (¡visible!): ")

    # Comprobar que las credenciales son válidas
    credencialesValidas = """SELECT EXISTS(SELECT * 
                                            FROM python.usuarios 
                                            WHERE username = %s and 
                                                password = %s)"""

    
    cursor.execute(credencialesValidas,(username,password))
    for (condition) in cursor:
        condition = condition[0]

    # Si las credenciales son válidas, accedemos al meno principal
    if condition:
        os.system("cls")
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
    cursor = mydb.cursor()
    titulo = input("Titulo: ")
    texto = input("Cuerpo: ")
    tiempo = datetime.timestamp(datetime.now())
    
    crear_nota = """INSERT INTO python.notas 
                    (titulo, creada, cuerpo, autor) 
                        VALUES (%s, %s, %s, %s)"""
    cursor.execute(crear_nota, (titulo, tiempo, texto, username))
    mydb.commit()

def listarNotas(username):
    cursor = mydb.cursor()
    consulta = """SELECT id, titulo, cuerpo
                    From python.notas
                    WHERE autor = %s 
                    ORDER BY creada DESC"""
    cursor.execute(consulta,[username])
    for (id,titulo, texto) in cursor:
        print("ID: " + str(id) + "   " + "Título: "+ str(titulo)+ ".")
        print("Cuerpo: "+ str(texto))
    input("Presione cualquier tecla para salir: ")
    # Mostrar por pantalla las notas del usuario, ordenadas por fecha de creación decreciente

def filtrarNotas(username):
    cursor = mydb.cursor()
    os.system("cls")
    pedir_fechas()
    f1 = input("Fecha Inicial: ") 
    f2 = input("Fecha Final: ") 
    f1 =  datetime.timestamp(datetime.strptime(f1, '%d/%m/%Y'))
    f2 =  datetime.timestamp(datetime.strptime(f2, '%d/%m/%Y'))
    consulta = """SELECT id, titulo, cuerpo
                    From python.notas
                    WHERE autor = %s AND creada BETWEEN %s AND %s
                    ORDER BY creada DESC"""
    cursor.execute(consulta, (username, f1, f2))
    for (id,titulo, texto) in cursor:
        print("ID: " + str(id) + "   " + "Título: "+ str(titulo)+ ".")
        print("Cuerpo: "+ str(texto))
    # Mostrar por pantalla las notas del usuario creadas entre dos fechas pedidas por pantalla
    input("Presione cualquier tecla para salir: ")

def borrarNota(username):
    os.system("cls")
    id = int(input("Inserte el id de la nota a eliminar: "))
    cursor = mydb.cursor()
    consulta = """DELETE
                    From python.notas
                    WHERE autor = %s and id = %s 
                    ORDER BY creada DESC"""
    cursor.execute(consulta, (username, id))
    mydb.commit()
    # Pide el id de la nota que se quiere borrar y se elimina la fila correspondiente, siempre que la nota sea del usuario <username>

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
            time.sleep(5)
            os.system("cls")


if __name__ == '__main__':
    initDB()
    run()
