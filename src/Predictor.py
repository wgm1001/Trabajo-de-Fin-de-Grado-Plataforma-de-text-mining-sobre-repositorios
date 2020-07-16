# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Predictor
Clase encraga de realizar el proceso de entrenamiento y predicción
"""
from src.ModeloSingleClass import ModeloSingleClass
from src.ModeloMultiClass import ModeloMultiClass
from src.TranscriptorMultiClass import TranscriptorMultiClass
from src.TranscriptorSingleClass import TranscriptorSingleClass

class Predictor:
    singleClass=ModeloSingleClass.switchAlgoritmo.keys()
    multiClass=ModeloMultiClass.switchAlgoritmo.keys()
    def __init__(self,modelo='MultinomialNB'):
        self.modelo=modelo
        if modelo not in Predictor.singleClass and modelo not in Predictor.multiClass:
            raise Exception('Modelo desconocido')
        if modelo in Predictor.singleClass:
            self.clf=ModeloSingleClass(mod=modelo)
        if modelo in Predictor.multiClass:
            self.clf=ModeloMultiClass(mod=modelo)
            
    def entrenar(self,repositorios,stopW=True,idioma='english',comentarios=True,metodo='CV',sinEtiqueta=True):
        self.__checkArgs(stopW=stopW,comentarios=comentarios,repositorios=repositorios,sinEtiqueta=sinEtiqueta)
        if self.modelo in Predictor.multiClass:
            self.trans=TranscriptorMultiClass()
        if self.modelo in Predictor.singleClass:
            self.trans=TranscriptorSingleClass()
        transcripcion=self.trans.transcribir_entrenar(repositorios=repositorios,sinEtiqueta=sinEtiqueta,stopW=stopW,idioma=idioma,comentarios=comentarios,metodo=metodo)
        X=transcripcion[0]
        y=transcripcion[1]
        self.clf.entrenar(X,y)
    def predecir(self,y):
        y=self.trans.transcribir(y)
        pred=self.clf.predecir(y)
        if self.modelo in Predictor.multiClass:
            pred=self.trans.recuperar(pred)
        else:
            pred=pred.tolist()
        return pred
    def __checkArgs(self,stopW,comentarios,repositorios,sinEtiqueta):
        if not isinstance(stopW,bool):
            raise Exception('Argumentos incorrectos')
        if not isinstance(comentarios,bool):
            raise Exception('Argumentos incorrectos')
        if not isinstance(sinEtiqueta,bool):
            raise Exception('Argumentos incorrectos')
        if not repositorios:
            raise Exception('Argumentos incorrectos')
        
        