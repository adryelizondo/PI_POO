from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("C:/Users/Bienvenido/OneDrive/Documentos/POO_PI.db")
            print("Conectado a la base de datos")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")

    def guardarUsuario(self, nom, cor, con):

        conx = self.conexionBD()

        if(nom == "" or cor == "" or con == ""):
           messagebox.showwarning("Cuidado!", "Ningún campo puede estar vacio")
           conx.close() 
        else:
            cursor = conx.cursor()
            conH = self.encriptarCont(con)
            datos = (nom, cor, conH)
            qrInsert = "insert into TBRegistros(nombre, correo, contra) values(?,?,?)"
            
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!", "Se guardo el usuario")
    
    def encriptarCont(self,con):
        conPlana = con
        conPlana = conPlana.encode() 
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana, sal)
        print(conHa)
        return conHa