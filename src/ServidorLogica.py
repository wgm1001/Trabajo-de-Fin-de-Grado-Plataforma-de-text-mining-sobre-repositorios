# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Servidor Logica
Esta clase esta dedicada a llamar a las distintas funciones de las clases
para que el servidor no lo haga directamente
"""
from Extractor import Extractor
from Almacen import Almacen
from Predictor import Predictor
import os
from datetime import datetime

class ServidorLogica:
    id_count=0
    modelos=dict()
    ruta_error='..'+os.path.sep+'errores.txt'  
    def extraer_rep(argumentos,pipe):
        url=argumentos['url']
        url=url.split('/')
        if url[2]!='gitlab.com':
            pipe.send(400)
        url=url[3]+'/'+url[4]
        try:
            if 'token' in argumentos.keys():
                ext=Extractor(link=url,token=argumentos['token'])
            else:
                ext=Extractor(url)
            p=ext.extraer()
            Almacen.guardar(p)
            pipe.send(200)
        except Exception as e:
            ServidorLogica.log(str(e))
            if str(e)=='Proyecto no encontrado':
                pipe.send(404)
            if str(e)=='Permisos insuficientes':
                pipe.send(401)
            raise

    @staticmethod
    def crearModelo(id_ses,modelo):
        temp=ServidorLogica.modelos
        temp[id_ses]=Predictor(modelo=modelo)
        ServidorLogica.modelos=temp
    
    @staticmethod
    def entrenarModelo(id_ses,repositorios,stopW,idioma,comentarios,metodo,sinEtiqueta,pipe):
        try:
            ServidorLogica.modelos[id_ses].entrenar(repositorios=repositorios,stopW=stopW,idioma=idioma,comentarios=comentarios,metodo=metodo,sinEtiqueta=sinEtiqueta)
            Almacen.guardarModelo(ServidorLogica.modelos[id_ses])
            pipe.env(200)
        except Exception as e:
            ServidorLogica.log(str(e))
            if str(e)=='Argumentos incorrectos':
                pipe.env(400)
            raise
            
    @staticmethod
    def sacarModelo(id_ses,repositorios):
        temp=ServidorLogica.modelos
        temp[id_ses]= Almacen.sacarModelo(repositorios)
        ServidorLogica.modelos=temp
        return temp[id_ses]
    
    @staticmethod
    def predIssue(id_ses,issue_text):
        return ServidorLogica.modelos[id_ses].predecir(issue_text)
    
    @staticmethod
    def getId():
        ServidorLogica.id_count+=1
        return ServidorLogica.id_count
    
    @staticmethod
    def log(txt):
        log=open(ServidorLogica.ruta_error,"a")
        log.write("Ha ocurrido un error ("+datetime.now()+"):\n"+txt)
        