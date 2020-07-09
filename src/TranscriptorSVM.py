# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase transcriptor SVM
Clase dedicada a transforma los parametros de un repositorio a la entrada del modelo SVM
"""
from src.Almacen import Almacen
import numpy as np
from nltk.corpus import stopwords
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer

class TranscriptorSVM:
    @staticmethod
    def transcribir(repositorios=None,stopW='True',idioma='spanish',comentarios=True):
        issues_text=[]
        labels=[]
        for r in repositorios:
            repositorio=Almacen.sacarRepositorios(idRepositorio=r)
        for i in repositorio.issues:
            if len(i.labels)>0:
                temp=i.title
                if i.description is not None:
                    temp+=' '+i.description
                if comentarios:
                    for c in i.notes:
                        temp+=' '+c
                issues_text.append(temp)
                labels.append(i.labels)  
        y=np.array(labels)
        y=MultiLabelBinarizer().fit_transform(y)
        if stopW:
            stopWords = set(stopwords.words(idioma))
            bolsa = CountVectorizer(stop_words=stopWords)
        else:
            bolsa = CountVectorizer()
        bolsa.fit(issues_text)
        x=bolsa.transform(issues_text).toarray()
        x=np.array(x)
        return [x,y,labels]
    
    @staticmethod
    def recuperar(y,labels):
        fin=[]
        for i in range(len(y)):
            temp=[]
            for x in range(len(labels)):
                if y[i]==1:
                    temp.append(labels[x])
            fin.append(temp)
        return fin