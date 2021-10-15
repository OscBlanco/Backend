from Usuario import Usuario
#from flask_login import UserMixin
from werkzeug.security import check_password_hash
import sqlite3
from catalogo import Catalogo


class Administrador(Usuario,Catalogo):
    def __init__(self,ID,correo_elect,nombre_usuario,contrasena):
        Usuario.__init__(self,ID,correo_elect,nombre_usuario,contrasena)
    
    def verif_cont(self,contrasena):
        return check_password_hash(self.get_pass,contrasena)
    
        
    
    

class SuperAdm(Administrador):
    def __init__(self,correo_elect,nombre_usuario,contrasena,id_adm):
        super().__init__(correo_elect,nombre_usuario,contrasena,id_adm)
        
class UsuarioFinal(Usuario):
    pass

admin1=Administrador(2,'holas@correo','ivan','a12345')
set_usuario(admin1.get_ID,admin1.get_correo,admin1.get_nombre,admin1.get_pass)