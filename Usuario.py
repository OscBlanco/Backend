from flask_login import UserMixin,LoginManager
from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3
import datetime
from catalogo import Catalogo


login=LoginManager()
class Usuario(UserMixin):
    Base='base_datos.sqlite'
    def __init__(self,correo_elect,contrasena):
        self.id=id(correo_elect)
        self._correo_elect=correo_elect
        self._contrasena=generate_password_hash(contrasena)
    @property
    def get_ID(self):
        return self.id    
    @property
    def get_correo(self):
        return self._correo_elect
       
    @property
    def get_pass(self):
        return self._contrasena

    @get_pass.setter
    def set_pass(self,contrasena):
        self._contrasena=generate_password_hash(contrasena)
        return self._contrasena
    @staticmethod
    def get_bd():
        return sqlite3.connect(Usuario.Base)
    
    def verif_cont(self,contrasena):
        user=self.get_usuario(self.get_correo)
        if user is not None:
            contra=user[2]
            return check_password_hash(contra,contrasena)
        return None
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
    
    def actualizar_contrasena(self,contrasena):
        con=self.get_bd
        contra=self.set_pass(contrasena)
        sentencia='UPDATE usuarios SET contra = ? WHERE ID = ?'
        con.cursor().execute(sentencia,[contra])
        con.commit()
    @staticmethod
    def borrar_usuario(correo):
        con=Usuario.get_bd()
        cursor=con.cursor()
        borrar='DELETE FROM usuario WHERE correo= ?'
        cursor.execute(borrar,[correo])
        con.commit()
    
    def comentar(self,comentario,id_user,nombre_producto):
        con=Usuario.get_bd()
        cursor=con.cursor()
        id_producto=Catalogo.get_by_name(nombre_producto)[0]
        comentar='INSERT INTO comentarios(comentario,ID_USUARIO,ID_producto) VALUES (?,?,?) '
        cursor.execute(comentar,[comentario,id_user,id_producto])
        con.commit()
    
    def borrar_comentario(self,comentario):
        con=Usuario.get_bd()
        cursor=con.cursor()
        comentar='SELECT id FROM comentarios WHERE comentario=? '
        cursor.execute(comentar,[comentar,comentario])
        id_comentario=cursor.fetchone()
        eliminar='DELETE FROM comentarios WHERE id=?'
        cursor.execute(eliminar,[id_comentario])
        con.commit()
    
    def editar_comentario(self,comentario_ant,coment_nuevo):
        con=Usuario.get_bd()
        cursor=con.cursor()
        comentar='SELECT id FROM comentarios WHERE comentario=? '
        cursor.execute(comentar,[comentar,comentario_ant])
        id_comentario=cursor.fetchone()
        editar='UPDATE comentarios SET comentario=? WHERE id=?'
        cursor.execute(editar,[coment_nuevo,id_comentario])
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

@login.user_loader
def load_user(correo):
    return Usuario.get_usuario(correo)            
