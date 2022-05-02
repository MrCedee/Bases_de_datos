from sqlite3 import Timestamp
from MySQLdb import TimestampFromTicks
from sqlalchemy import create_engine
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from datetime import datetime

os.system("cls")
engine = create_engine(
    "mysql+pymysql://root:sqlalchemy@127.0.0.1:3306/alchemy"
)

Base = declarative_base()
session = 0

def initDB():
    global Base, session, Usuarios, Notas
    class Usuarios(Base):
        __tablename__ = "usuarios"

        username = Column(String(50), primary_key=True)
        password = Column(String(50), nullable=False)


        def __repr__(self):
            return f"<Usuario: {self.username}>"

    class Notas(Base):
        __tablename__ = "series"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        titulo = Column(String(250), nullable=False)
        cuerpo = Column(String(1000), nullable=False)
        autor = Column(String(50), ForeignKey("usuarios.username"))
        fecha_alta = Column(Timestamp, server_default=func.now())

        usuario = relationship("Usuarios", backref="notas")


        def __repr__(self):
            return f"<Id, '{self.id}', Titulo '{self.titulo}', \n Cuerpo '{self.cuerpo}'>"


   

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()



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

def pedir_fechas():
    print(f'------- FECHAS -------')
    print('  Inserte dos fechas entre las que quiere obtener notas')
    print('-----------------------')


def crearUsuario():


    print('------ Registro de usuario ------\n')
    username_ =  input('Nombre de usuario : ')
    password_ =  input('Contraseña (¡visible!) : ')

    # Añadir el usuario a la BD
    u1 = Usuarios(username=username_, password=password_)
    session.add(u1)
    session.commit()
    os.system("cls")

    print('------ Usuario añadido ------\n')

def login():
    username_ = input("Login: ")
    password_ = input("Password (¡visible!): ")

    # Comprobar que las credenciales son válidas
    credenciales = session.query(Usuario)
    credenciales.filter_by(username=username_)
    credenciales.filter_by(password=password_)
    credenciales.all()
    condition = True

    
    if credenciales[0] == None:
        condition = False

    # Si las credenciales son válidas, accedemos al meno principal
    if condition:
        os.system("cls")
        opcion = 0
        while opcion != 5:
            muestraOperaciones(username_)
            opcion = int(input("Elige una opción : "))
            if opcion == 1:
                crearNota(username_)
            elif opcion == 2:
                listarNotas(username_)
            elif opcion == 3:
                filtrarNotas(username_)
            elif opcion == 4:
                borrarNota(username_)

def crearNota(username_):
    titulo_ = input("Titulo: ")
    texto = input("Cuerpo: ")
    tiempo = datetime.today()
    
    c = Notas(titulo=titulo_, cuerpo=texto, autor=username_, creada=tiempo)
    session.add(c)
    session.commit()

def listarNotas(username_):
    u2 = session.query(Usuarios)
    u2.filter_by(username=username_)
    u2.all()
    u2 = u2[0]
    for i in u2.notas:
        print("ID: " + str(i.id) + "   " + "Título: "+ str(i.titulo)+ ".")
        print("Cuerpo: "+ str(i.cuerpo))
    # Mostrar por pantalla las notas del usuario, ordenadas por fecha de creación decreciente

def filtrarNotas(username):
    cursor = mydb.cursor()
    os.system("cls")
    pedir_fechas()
    f1 = input("Fecha Inicial: ")
    f2 = input("Fecha Final: ")
    f1 =  datetime. strptime(f1, '%d/%m/%y')
    f2 =  datetime. strptime(f2, '%d/%m/%y')
    consulta = """SELECT id, titulo, cuerpo
                    From python.notas
                    WHERE autor = %s AND creada BETWEEN %s AND %S
                    ORDER BY creada DESC"""
    cursor.execute(consulta, (username, f1, f2))
    for (id,titulo, texto) in cursor:
        print("ID: " + str(id) + "   " + "Título: "+ str(titulo)+ ".")
        print("Cuerpo: "+ str(texto))
    # Mostrar por pantalla las notas del usuario creadas entre dos fechas pedidas por pantalla
    pass

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
