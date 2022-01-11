import pandas as pd 
import sqlalchemy as db
from sqlalchemy.sql.schema import MetaData 


class Conexion:
    def __init__(self):
        super().__init__()
        self.conectar()

    def conectar(self):
        #Se crea la conexión
        nombre_usuario = 'root'
        password = 'Juan3221485_'
        servidor ='localhost'
        puerto = '3306'
        base_datos = 'crud'
        engine = db.create_engine(f"mysql+mysqlconnector://{nombre_usuario}:{password}@{servidor}:{puerto}/{base_datos}", echo=True)
        #Iniciamos conexion con DB
        self.connection = engine.connect()
        print(self.connection)
        # Se hece un mapeo de la BD
        metadata = db.MetaData()
        self.usuarios = db.Table('usuarios', metadata, autoload= True, autoload_with= engine)
        self.vehiculos = db.Table('vehiculos',metadata, autoload= True, autoload_with= engine)

    def crearVehiculo(self, datosVehiculos):
        insertarVehiculo = db.insert(self.vehiculos).values(datosVehiculos)
        self.connection.execute(insertarVehiculo)

    def listaVehiculos(self, dataFrame=False):
        query = db.select([self.vehiculos])
        resultado = self.connection.execute(query)
        resultset = resultado.fetchall()
        if(dataFrame):
            df = pd.Dataframe(resultset)
            return df
        else:
            print(resultset)
            return resultset

    def validarCredenciales(self,usuario, password):
        query = db.select([self.usuarios]).where(
            self.usuarios.columns.nombre_usuario==usuario,
            self.usuarios.columns.contraseña_usuario == password)
        resultado = self.connection.execute(query)
        Resultset = resultado.fetchall()
        return Resultset
        
                
                



    




