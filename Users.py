from Usuario import Usuario
from catalogo import Catalogo
from Orden import Orden

class Admin(Usuario,Catalogo):
    def __init__(self,correo_elect,contrasena):
        Usuario.__init__(self,correo_elect,contrasena)
        self._is_admin=1
    @property
    def get_adm(self):
        return self._is_admin
class SuperAdm(Admin):
    def __init__(self,correo_elect,contrasena):
        Usuario.__init__(self,correo_elect,contrasena)
        self._is_admin=1
    
    def set_admin(self,usuario):
        ID=usuario.get_ID
        correo=usuario.get_correo
        contra=usuario.get_pass
        admin=Admin(correo,contra)
        Usuario.borrar_usuario(correo)
        admin.set_usuario(ID,correo,contra,admin.get_adm)
        del usuario
        
        
    
class UsuarioFinal(Usuario):
    def __init__(self,correo_elect,contrasena):    
        super().__init__(self,correo_elect,contrasena)
        self._is_admin=0
        
    def compra(self,*productos):
        orden=Orden(*productos)
        fecha=orden.fecha_creac
        