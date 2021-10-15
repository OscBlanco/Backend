#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:34:08 2021

@author: oscar
"""
from flask import Flask,render_template, jsonify,json,request
from flask_cors import CORS,cross_origin

app=Flask(__name__,static_folder='./frontend/dist/',template_folder='./frontend/dist/')
#Cors=CORS(app)

#CORS(app, resources={r'*':{'origins': '*'}},CORS_SUPPORTS_CREDENTIALS=True)


@app.route('/',defaults={'path':''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')


@app.route('/')
def root():
    return jsonify('Mensaje desde FLASK')


