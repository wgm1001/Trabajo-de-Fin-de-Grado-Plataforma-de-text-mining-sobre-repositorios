# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Modelo SVM
Esta implementa la predicción a través del modelo SVM
"""
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm

class ModeloSVM:
    def __init__(self,ran_sta):
        self.clasificador = OneVsRestClassifier(svm.SVC(random_state=ran_sta))
        
    def entrenar(self,X,y):
        self.clasificador.fit(X, y)

    def predecir(self,X):
        return self.clasificador.predict(X)