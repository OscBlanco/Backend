

from flask import Flask,render_template, jsonify,json,request
from flask_login import LoginManager
from flask_cors import CORS,cross_origin
from catalogo import Catalogo

#app=Flask(__name__,static_folder='./frontend/dist/',template_folder='./frontend/dist/')
app=Flask(__name__)
#CORS(app, resources={r'*':{'origins': '*'}},CORS_SUPPORTS_CREDENTIALS=True)
app.config['SECRET KEY']='3i-IdbODscH0yR4WFu_yvZppB76hh5I'
#@app.route('/',defaults={'path':''})
#@app.route('/<path:path>')
#def render_vue(path):
#    return render_template('index.html')
#
#
#@app.route('/')
#def root():
#    return jsonify('Mensaje desde FLASK')
login_manager=LoginManager(app)



@app.route('/catalogo')
def get_catalogo():
    cata=Catalogo().get_catalogo()
    return jsonify(cata)

@app.route('/catalogo1',methods=['POST'])
def insertar_producto():
    detalles=request.get_json()
    nombre=detalles['nombre']
    precio=detalles['precio']
    calificacion=detalles['calificacion']
    resultado=Catalogo().insertar_producto(nombre,precio,calificacion)
    return jsonify(resultado)

@app.route('/catalogo1',methods=['PUT'])
def actualizar_producto():
    detalles=request.get_json()
    ID=detalles['ID']
    nombre=detalles['nombre']
    precio=detalles['precio']
    calificacion=detalles['calificacion']
    resultado=Catalogo().actualizar_producto(ID,nombre,precio,calificacion)
    return jsonify(resultado)
@app.route('/catalogo1/<ID>',methods=['DELETE'])
def borrar_producto(ID):
    resultado=Catalogo().borrar_producto(ID)
    return jsonify(resultado)

@app.route('/catalogo1/<ID>',methods=['GET'])
def get_por_id(ID):
    resultado=Catalogo().get_por_id(ID)
    return jsonify(resultado)

    