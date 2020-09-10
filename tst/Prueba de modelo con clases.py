# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba modelo con clases
Esta prueba se encarga de comprobar que las clases funcionan correctamente.
"""
from src.Predictor import Predictor
from src.Almacen import Almacen
def pruebaSVM():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaSVM()
    Ha llegado sin fallos
    
    '''
    p=Predictor(modelo='SVM',MultiManual=False)
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,sinEtiqueta=True)
    rep=Almacen.sacarRepositorios(19766159)
    issue=[rep.issues[0].title]
    p.predecir(issue)
    print('Ha llegado sin fallos')

def pruebaMultinomialNB():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaMultinomialNB()
    Ha llegado sin fallos
    
    '''
    p=Predictor(modelo='MultinomialNB',MultiManual=False)
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,sinEtiqueta=True)
    rep=Almacen.sacarRepositorios(19766159)
    issue=[rep.issues[0].title]
    p.predecir(issue)
    print('Ha llegado sin fallos')

def pruebaKNN():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaKNN()
    Ha llegado sin fallos
    
    '''
    p=Predictor(modelo='KNN',MultiManual=False)
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,sinEtiqueta=True)
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
    p=Predictor(modelo='RandomForest',MultiManual=False)
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,sinEtiqueta=True)
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
    p=Predictor(modelo='OneVsRest',MultiManual=False)
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,sinEtiqueta=True)
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
        Predictor(modelo='Inválido',MultiManual=False)
    except Exception as e:
        if str(e)=='Modelo desconocido':
            print('Error detectado')
        else:
            raise
def pruebaAlmacenamientoModelo():
    '''
    Probaremos a guardar un modelo entrenado en la base de datos.
    
    >>> pruebaAlmacenamientoModelo()
    Llega sin errores
    
    '''
    p=Predictor(modelo='RandomForest',MultiManual=False)
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,sinEtiqueta=True)
    Almacen.guardarModelo(p)
    p=Almacen.sacarModelo([19766159])
    Almacen.sacarRepositorios(19766159)
    print('Llega sin errores')
            
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
    p=Predictor(modelo='RandomForest',MultiManual=False)
    try:
        p.entrenar(repositorios=[19766159],stopW='inválido',idioma='english',comentarios=True,sinEtiqueta=True)
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Primer error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[19766159],stopW=True,idioma='Inválido',comentarios=True,sinEtiqueta=True)
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Segundo error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios='invalido',sinEtiqueta=True)
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Tercer error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[],stopW=True,idioma='english',comentarios=True,sinEtiqueta=True)
    except Exception as e:
        if str(e)=='Argumentos incorrectos':
            print('Cuarto error detectado')
        else:
            raise
    try:
        p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,metodo='invalido',sinEtiqueta=True)
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
            
            
def pruebaModeloPorEtiqueta():
    '''
    Probaremos que funcione la predicción con este modelo
    
    >>> pruebaModeloPorEtiqueta()
    Ha llegado sin fallos
    
        '''
    p=Predictor(modelo='MultinomialNB',MultiManual=False)
    p.entrenar(repositorios=[19766159],stopW=True,idioma='english',comentarios=True,sinEtiqueta=True)
    rep=Almacen.sacarRepositorios(19766159)
    issue=[rep.issues[0].title]
    p.predecir(issue)
    print('Ha llegado sin fallos')
      
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

