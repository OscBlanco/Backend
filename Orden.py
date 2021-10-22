
import datetime
class Orden():
    numero_orden=0
    def __init__(self,*productos):
        if len(productos)>0:
            Orden.numero_orden +=1
    def fecha_creac(self):
         fecha=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
         return fecha
            
