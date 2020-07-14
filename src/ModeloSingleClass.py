# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Modelo M
Esta implementa la predicción a través del modelo Pasado por argumento
"""
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
class ModeloSingleClass:
    switchAlgoritmo={'MultinomialNB':MultinomialNB(),'SVM':svm.SVC(),'KNN':KNeighborsClassifier(),'RandomForest':RandomForestClassifier()}
    def __init__(self,mod):
        self.clasificador =ModeloSingleClass.switchAlgoritmo[mod]
        
    def entrenar(self,X,y):
        self.clasificador.fit(X, y)

    def predecir(self,X):
        return self.clasificador.predict(X)