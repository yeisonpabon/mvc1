from tkinter import messagebox
from models.ConexiondB import ConexionDB
class Usuario():
    def __init__(self, nombreUsusario,password):
        self.nombreUsuario = nombreUsusario
        self.password = password
        self.rol = ""

    
    def iniciarSesion(self,nombreusuario,password):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conn = miConexion.getConection()
        cursor = conn.cursor()
        cursor.execute("select * from usuario")
        listausuarios = cursor.fetchall()
        for usuario in listausuarios:
            if(usuario[1] == nombreusuario and usuario[2] == password):
                self.rol = usuario[3]
                if(self.rol == "admin"):
                    messagebox.showinfo("informacion","Acceso correcto a administrador")
                    # crear objeto administrador y abrir el menu de adminstrador
                else:
                    messagebox.showinfo("informacion","Acceso correcto a digitador")
                miConexion.cerrarConexion()
            return
        messagebox.showwarning("advertencia","el ussuario no existe")


