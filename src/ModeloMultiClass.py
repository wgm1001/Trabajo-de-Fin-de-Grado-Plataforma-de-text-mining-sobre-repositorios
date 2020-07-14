# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Modelo M
Esta implementa la predicción a través del modelo Pasado por argumento
"""
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier

class ModeloMultiClass:
    switchAlgoritmo={'OneVsRest':OneVsRestClassifier}
    def __init__(self,mod):
        self.clasificador =ModeloMultiClass.switchAlgoritmo[mod](MultinomialNB())
        
    def entrenar(self,X,y):
        self.clasificador.fit(X, y)

    def predecir(self,X):
        return self.clasificador.predict(X)