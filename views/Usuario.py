from tkinter import messagebox
from Models.conexionDB import ConexionDB

class Usuario():
    def __init__(self, nombreUsuario, password):
        self.nombreUsuario = nombreUsuario
        self.password = password
        self.rol = ""
        
    def iniciarSesion(self, nombreUsuario, password):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conn = miConexion.getConnection()
        cursor = conn.cursor()
        cursor.execute("select * from usuario")
        listaUsuarios = cursor.fetchall()
        for usuario in listaUsuarios:
            if (usuario[1] == nombreUsuario and usuario[2] == password):
                self.rol = usuario[3]
                if (self.rol == "admin"):
                    messagebox.showinfo("Informacion", "¡Acceso correcto Administrador!")
                    #crear objeto administrador y abrir menu Administrador
                else: 
                    messagebox.showinfo("Informacion", "¡Acceso correcto Digitador!")
                miConexion.cerrarConexion()
                return
        messagebox.showwarning("¡El nombre de usuario y/o contraseña no exixte," "Verifique e intente nuevamente!")
                     
            
        
        