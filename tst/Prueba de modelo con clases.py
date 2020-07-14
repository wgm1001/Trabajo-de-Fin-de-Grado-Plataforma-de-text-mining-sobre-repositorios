# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba modelo con clases
Esta prueba se encarga de comprobar que las clases funcionan correctamente.
"""
from src.Predictor import Predictor
from src.Almacen import Almacen
import numpy as np
def pruebaSVM():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaSVM()
    Ha predecido bien
    Ha llegado sin fallos
    
    '''
    p=Predictor(modelo='SVM')
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True)
    rep=Almacen.sacarRepositorios(19766159)
    issue=[rep.issues[0].title]
    pred=p.predecir(issue)
    if pred==rep.issues[0].labels:
        print('Ha predecido bien')
    print('Ha llegado sin fallos')

def pruebaMultinomialNB():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaMultinomialNB()
    Ha predecido bien
    Ha llegado sin fallos
    
    '''
    p=Predictor(modelo='MultinomialNB')
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,)
    rep=Almacen.sacarRepositorios(19766159)
    issue=[rep.issues[0].title]
    pred=p.predecir(issue)
    if pred==rep.issues[0].labels:
        print('Ha predecido bien')
    print('Ha llegado sin fallos')

def pruebaKNN():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaKNN()
    Ha llegado sin fallos
    
    '''
    p=Predictor(modelo='KNN')
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True)
    rep=Almacen.sacarRepositorios(19766159)
    issue=[rep.issues[0].title]
    p.predecir(issue)
    print('Ha llegado sin fallos')
   
def pruebaRandomForest():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaRandomForest()
    Ha llegado sin fallos
    
    '''
    p=Predictor(modelo='RandomForest')
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True)
    rep=Almacen.sacarRepositorios(19766159)
    issue=[rep.issues[0].title]
    p.predecir(issue)
    print('Ha llegado sin fallos')    
    
def pruebaOneVsRest():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaOneVsRest()
    Ha llegado sin fallos
    
    '''
    p=Predictor(modelo='OneVsRest')
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True)
    rep=Almacen.sacarRepositorios(19766159)
    issue=[rep.issues[5].title]
    p.predecir(issue)
    print('Ha llegado sin fallos')  
    
def pruebaModeloInvalido():
    '''
    Probaremos que nos salte el error si el modelo es incorrecto
    
    >>> pruebaModeloInvalido()
    Error detectado
    
        '''
    try:
        Predictor(modelo='Inválido')
    except Exception as e:
        if str(e)=='Modelo desconocido':
            print('Error detectado')
        else:
            raise
def pruebaBadArgs():
    '''
    En esta prueba introduciermos malos parametros en el entrenamiento.
    
    >>> pruebaBadArgs()
    Primer error detectado
    Segundo error detectado
    Tercer error detectado
    Cuarto error detectado
    Quinto error detectado
    Sexto error detectado
    '''  
    p=Predictor(modelo='RandomForest')
    try:
        p.entrenar(repositorios=[19766159],stopW='inválido',idioma='english',comentarios=True)
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Primer error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[19766159],stopW=True,idioma='Inválido',comentarios=True)
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Segundo error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios='invalido')
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Tercer error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[],stopW=True,idioma='english',comentarios=True)
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Cuarto error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,metodo='invalido')
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Quinto error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,sinEtiqueta='invalido')
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Sexto error detectado')
        else:
            raise
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()

