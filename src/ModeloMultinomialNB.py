# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Modelo MultinomialNB
Esta implementa la predicción a través del modelo Multinomial
"""
from sklearn.naive_bayes import MultinomialNB

class ModeloMultinomialNB:
    def __init__(self):
        self.clasificador = MultinomialNB()
        
    def entrenar(self,X,y):
        self.clasificador.fit(X, y)

    def predecir(self,X):
        return self.clasificador.predict(X)