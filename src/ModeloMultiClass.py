# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Modelo Multiclass
Esta implementa la predicción a través del modelo Pasado por argumento
"""
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from src.ModeloSingleClass import ModeloSingleClass

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
        self.modelo =ModeloSingleClass.switchAlgoritmo[mod]
        self.clasificadores=dict()
        
    def entrenar(self,X,y):
        for etiquetas in y:
            for etiqueta in etiquetas:
                if etiqueta not in self.clasificadores.keys():
                    temp_X=[]
                    temp_Y=[]
                    self.clasificadores[etiqueta]=self.modelo()
                    for i in range(len(y)):
                        if etiqueta in y[i]:
                            temp_Y.append(True)
                        else:
                            temp_Y.append(False)
                        temp_X.append(X[i])
                    self.clasificadores[etiqueta].fit(X,y)

    def predecir(self,X):
        pred=[]
        for etiqueta in self.clasificadores.keys():
            if self.clasificadores[etiqueta].predict(X):
                pred.append(etiqueta)
        if pred is None:
            pred.append('Sin etiqueta')
        return pred