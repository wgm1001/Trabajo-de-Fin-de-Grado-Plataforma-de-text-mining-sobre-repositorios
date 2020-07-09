# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Predictor
Clase encraga de realizar el proceso de entrenamiento y predicción
"""
from src.TranscriptorSVM import TranscriptorSVM
from src.ModeloSVM import ModeloSVM
from src.TranscriptorMultinomialNB import TranscriptorMultinomialNB
class Predictor:
    def __init__(self,modelo='SVM',random_state=None):
        self.modelo=modelo
        if modelo=='SVM':
            trans=TranscriptorSVM.transcribir(repositorios=repositorios,stopW=stopW,idioma=idioma,comentarios=comentarios)
            self.X=trans[0]
            self.y=trans[1]
            self.labels=trans[2]
            self.clf=ModeloSVM(random_state=random_state)
        if modelo=='MultinomialNB':
            trans=TranscriptorMultinomialNB.transcribir(repositorios=repositorios,stopW=stopW,idioma=idioma,comentarios=comentarios)
            self.X=trans[0]
            self.y=trans[1]
            self.labels=None
            self.clf=ModeloSVM()
    def entrenar(self,stopW=True,idioma='english',comentarios=True,repositorios=[],):
        if self.modelo=='SVM':
            trans=TranscriptorSVM.transcribir(repositorios=repositorios,stopW=stopW,idioma=idioma,comentarios=comentarios)
            X=trans[0]
            y=trans[1]
            self.labels=trans[2]
        if self.modelo=='MultinomialNB':
            trans=TranscriptorMultinomialNB.transcribir(repositorios=repositorios,stopW=stopW,idioma=idioma,comentarios=comentarios)
            X=trans[0]
            y=trans[1]
            self.labels=None
        self.clf.entrenar(X,y)
    def predecir(self,y):
        pred=self.clf.predecir(y)
        if self.modelo=='SVM':
            pred=TranscriptorSVM.recuperar(pred,self.labels)
        return pred
        