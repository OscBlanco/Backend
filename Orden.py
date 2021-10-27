from Usuario import Usuario
import datetime
import sqlite3

class Orden():
    numero_orden=0
    Base='base_datos.sqlite'
    @staticmethod
    def ordenes():
        con=sqlite3.connect(Orden.Base)
        cursor=con.cursor()
        orden='''CREATE TABLE IF NOT EXISTS ordenes(
        ID INTEGER PRIMARY KEY, 
        ID_USUARIO INTEGER, 
		FECHA TEXT NOT NULL,
        TOTAL REAL NOT NULL,
        FOREIGN KEY (ID_USUARIO) references usuarios(ID))'''
        cursor.execute(orden)
        con.commit
    def add_orden(self,user):
        con=sqlite3.connect(Orden.Base)
        fecha=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cursor=con.cursor()
        sentencia='INSERT INTO ordenes (ID,ID_USUARIO,FECHA,TOTAL) values (?,?,?,?)'
        cursor.execute(sentencia,[self._ID,user.get_ID,fecha,self._total])
        con.commit()
        
    def __init__(self,user,**productos):
        if len(productos)>0:
            Orden.numero_orden +=1
            self._ID=Orden.numero_orden
            self._total=sum(productos.values())
            
  
            
