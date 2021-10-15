from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3
import datetime

class Usuario(UserMixin):
    Base='base_datos'
    def __init__(self,ID,correo_elect,contrasena):
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

    def base_usuarios(self):
        con=self.get_bd
        usuarios='''CREATE TABLE IF NOT EXISTS usuarios(
        ID INTEGER PRIMARY KEY,
        correo TEXT UNIQUE NOT NULL,
        contra TEXT NOT NULL,
        fecha TEXT NOT NULL
        )'''
        con.cursor().execute(usuarios)
    def set_usuario(self,ID,correo,nombre,contra):
        con=self.get_bd
        fecha=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        usuario='''INSERT INTO usuarios(ID,correo,contra,fecha) VALUES (?,?,?,?) '''
        con.cursor().execute(usuario,[ID,correo,contra,fecha])
        con.commit()
    
    def actualizar_contrasena(self,contra):
        con=self.get_bd
        sentencia='UPDATE usuarios SET contra = ? WHERE ID = ?'
        con.cursor().execute(sentencia,[contra])
        con.commit()
    
    @staticmethod
    def get_usuario(correo):
        con=Usuario.get_bd()
        usuario='SELECT ID,correo,contra,fecha FROM usuarios WHERE correo= ?'
        con.cursor().execute(usuario,[correo])
        if con.cursor().fetchone() != None: 
            return con.cursor().fetchone()
        return None
        
    
