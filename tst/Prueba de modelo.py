# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba modelo
En esta prueba trataré de familiarizarme con el funcionamiento del modelo a usar para la predicción
"""
from sklearn.naive_bayes import MultinomialNB
from src.Almacen import Almacen
from nltk.corpus import stopwords
import numpy as np


stopWords = set(stopwords.words('english'))
repositorio=Almacen.sacarRepositorios(idRepositorio=8860457)
x=[]
y=[]
for i in repositorio.issues:

    if len(i.labels)>0:
        temp=[]
        temp+=i.title.split()
        if i.description is not None:
            temp+=i.description.split()
        for c in i.notes:
            temp+=c.split()
        fin=[]
        for s in temp:
            if s not in stopWords:
                fin.append(s)
        np.reshape(fin,(1,len(fin)))
        x.append(fin)
        y.append(i.labels)

clf = MultinomialNB()
clf.fit(x, y)
print(y[0],' predicho=',clf.predict(x[0]))
