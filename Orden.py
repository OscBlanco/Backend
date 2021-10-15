from Users import UsuarioFinal
import datetime
class Orden():
    numero_orden=0
    def __init__(self,*productos):
        if len(productos)>0:
            Orden.numero_orden +=1
            
    def fecha_creac(self):
        return datetime.datetime.now