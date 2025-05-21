import mariadb as db

class ConexionDB():
    def __init__(self):
        self.__host = "localhost"
        self.__puerto = 3307
        self.__usuario = "root"
        self.__password = ""
        self.__database = "ejemplo"
        self.__conexion = None


    def getConection(self):
        return self.__conexion
    

    def crearConexion(self):
        self.__conexion = db.connect(host= self.__host,
                                     user= self.__usuario,
                                     password = self.__password,
                                     port = self.__puerto,
                                     database= self.__database)
    
    def cerrarConexion(self):
        if self.__conexion:
            self.__conexion.close()
            self.__conexion = None
        

        
        