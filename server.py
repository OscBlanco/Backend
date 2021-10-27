

from flask import Flask,render_template, jsonify,json,request,redirect
from flask_login import LoginManager,current_user,login_user,login_required
from flask_cors import CORS,cross_origin
from catalogo import Catalogo
from Usuario import Usuario,login
from Users import *

app=Flask(__name__,static_folder='./frontend/dist/',template_folder='./frontend/dist/')
#app=Flask(__name__)
#CORS(app, resources={r'*':{'origins': '*'}},CORS_SUPPORTS_CREDENTIALS=True)
app.config['SECRET_KEY']='3i-IdbODscH0yR4WFu_yvZppB76hh5I'
@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')



login.init_app(app)
login.login_view='home'
    
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        correo='correo'
        contrasena='contrasena'
        usuario=Usuario(correo,contrasena)
        if usuario is not None and usuario.verif_cont(contrasena):
            admin=usuario.get_usuario(correo)
            if admin[4]==1:
                login_user(usuario)
                return redirect('/home_Admin')
            login_user(usuario)
            return redirect('/home')
    return render_template('login')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST' :
        correo='correo'
        contrasena='contrasena'
        if Usuario.get_usuario(correo) is not None:
            return ('Este correo ya está registrado')
        user=Usuario(correo,contrasena)
        user.set_usuario(user.get_ID,user.get_correo,user.get_pass,0)
@app.route('/catalogo')
@login_required
def get_catalogo():
    cata=Catalogo().get_catalogo()
    return jsonify(cata)

@app.route('/catalogo1',methods=['POST'])
@login_required
def insertar_producto():
    detalles=request.get_json()
    nombre=detalles['nombre']
    precio=detalles['precio']
    calificacion=detalles['calificacion']
    resultado=Catalogo().insertar_producto(nombre,precio,calificacion)
    return jsonify(resultado)

@app.route('/catalogo1',methods=['PUT'])
@login_required
def actualizar_producto():
    detalles=request.get_json()
    ID=detalles['ID']
    nombre=detalles['nombre']
    precio=detalles['precio']
    calificacion=detalles['calificacion']
    resultado=Catalogo().actualizar_producto(ID,nombre,precio,calificacion)
    return jsonify(resultado)
@app.route('/catalogo1/<ID>',methods=['DELETE'])
@login_required
def borrar_producto(ID):
    resultado=Catalogo().borrar_producto(ID)
    return jsonify(resultado)

@app.route('/catalogo1/<ID>',methods=['GET'])
@login_required
def get_por_id(ID):
    resultado=Catalogo().get_por_id(ID)
    return jsonify(resultado)

    