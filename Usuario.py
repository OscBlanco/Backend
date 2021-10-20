#from flask_login import UserMixin,LoginManager
from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3
import datetime


#login=LoginManager()
class Usuario():
    Base='base_datos.sqlite'
    def __init__(self,correo_elect,contrasena):
        self._ID=id(correo_elect)
        self._correo_elect=correo_elect
        self._contrasena=generate_password_hash(contrasena)
    @property
    def get_ID(self):
        return self._ID    
    @property
    def get_correo(self):
        return self._correo_elect
       
    @property
    def get_pass(self):
        return self._contrasena

    @get_pass.setter
    def set_pass(self,contrasena):
        self._contrasena=generate_password_hash(contrasena) 
    @staticmethod
    def get_bd():
        return sqlite3.connect(Usuario.Base)
     
    def verif_cont(self,contrasena):
        return check_password_hash(self.get_pass,contrasena)
    @staticmethod
    def base_usuarios():
        con=Usuario.get_bd()
        usuarios='''CREATE TABLE IF NOT EXISTS usuarios(
        ID INTEGER PRIMARY KEY,
        correo TEXT UNIQUE NOT NULL,
        contra TEXT NOT NULL,
        fecha TEXT NOT NULL,
        Admin BIT NOT NULL
        )'''
        con.cursor().execute(usuarios)
        con.commit()
    def set_usuario(self,ID,correo,contra,is_admin):
        con=self.get_bd()
        cursor=con.cursor()
        fecha=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        usuario='''INSERT INTO usuarios(ID,correo,contra,fecha,Admin) VALUES (?,?,?,?,?) '''
        cursor.execute(usuario,[ID,correo,contra,fecha,is_admin])
        con.commit()
    
    def actualizar_contrasena(self,contra):
        con=self.get_bd
        sentencia='UPDATE usuarios SET contra = ? WHERE ID = ?'
        con.cursor().execute(sentencia,[contra])
        con.commit()
    
    @staticmethod
    def get_usuario(correo):
        con=Usuario.get_bd()
        cursor=con.cursor()
        usuario='''SELECT ID,correo,contra,fecha,Admin FROM usuarios WHERE correo= ?'''
        cursor.execute(usuario,[correo])
        resultado=cursor.fetchone()
        if resultado is not None: 
            return resultado
        return None

#user1=Usuario('oscar@correo.com','123456')
#user2=Usuario('julio@correo.com','654321')
#Usuario.base_usuarios()
#user1.set_usuario(user1.get_ID,user1.get_correo,user1.get_pass,1)
#user2.set_usuario(user2.get_ID,user2.get_correo,user2.get_pass,0)
#@login.user_loader
#def load_user(correo):
#    return Usuario.get_usuario(correo)            
#user1=Usuario(id('oscar@correo.com'),'oscar@correo.com','123456')
#print(user1.verif_cont('123456'))
#user1.base_usuarios()
#user1.set_usuario(user1.get_ID,user1.get_correo,user1.get_pass,1)    
#user2=Usuario(id('Jhan@correo.com'),'Jhan@correo.com','654321')
#user2.set_usuario(user2.get_ID,user2.get_correo,user2.get_pass,1)
#user3=Usuario(id('hola@correo.com'),'hola@correo.com','456789')
#user4=Usuario(id('pepe@correo.com'),'pepe@correo.com','contraseña')
#user3.set_usuario(user3.get_ID,user3.get_correo,user3.get_pass,0)
#user4.set_usuario(user4.get_ID,user4.get_correo,user4.get_pass,0)
