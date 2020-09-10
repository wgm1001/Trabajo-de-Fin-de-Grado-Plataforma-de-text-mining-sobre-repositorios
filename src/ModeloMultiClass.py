# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Modelo Multiclass
Esta implementa la predicción a través del modelo Pasado por argumento
"""
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from src.ModeloSingleClass import ModeloSingleClass
import numpy as np
from sklearn.preprocessing import LabelBinarizer

class ModeloMultiClass:
    switchAlgoritmo={'OneVsRest':OneVsRestClassifier}
    def __init__(self,mod):
        self.clasificador =ModeloMultiClass.switchAlgoritmo[mod](MultinomialNB())
        
    def entrenar(self,X,y):
        self.clasificador.fit(X, y)

    def predecir(self,X):
        return self.clasificador.predict(X)
    
"""
@author: Willow Maui García Moreno
Clase Modelo Multiclass Manual
Esta implementa la predicción a través del modelo Pasado por argumento creando un modelo por etiqueta
"""

class ModeloMultiClassManual:
    def __init__(self,mod):
        self.modelo=mod
        self.clasificadores=dict()
        
    def entrenar(self,X,y):
        for etiquetas in y:
            for etiqueta in etiquetas:
                if etiqueta not in self.clasificadores.keys():
                    temp_X=[]
                    temp_Y=[]
                    self.clasificadores[etiqueta]=ModeloSingleClass.switchAlgoritmo[self.modelo]
                    for i in range(len(y)):
                        temp_Y.append(etiqueta in y[i])
                        temp_X.append(X[i])
                    temp_X=np.array(temp_X)
                    temp_Y=np.array(temp_Y)
                    self.clasificadores[etiqueta].fit(temp_X,temp_Y)

    def predecir(self,X):
        pred=[]
        for etiqueta in self.clasificadores.keys():
            if self.clasificadores[etiqueta].predict(X):
                pred.append(etiqueta)
        if not pred:
            pred.append('Sin etiqueta')
        return pred