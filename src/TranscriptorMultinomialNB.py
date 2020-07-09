# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase transcriptor MultinomialNB
Clase dedicada a transforma los parametros de un repositorio a la entrada del modelo MultinomialNB
"""
from src.Almacen import Almacen
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

class TranscriptorMultinomialNB:
    @staticmethod
    def transcribir(repositorios=None,stopW='True',idioma='spanish',comentarios=True):
        idioma='spanish'
        repositorio=Almacen.sacarRepositorios(idRepositorio=8860457)
        issues_text=[]
        y=[]
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
                    y.append(i.labels[0])
        
        y=np.array(y)
        if stopW:
            stopWords = set(stopwords.words(idioma))
            bolsa = CountVectorizer(stop_words=stopWords)
        else:
            bolsa = CountVectorizer()
        bolsa = CountVectorizer(stop_words=stopWords)
        bolsa.fit(issues_text)
        x=bolsa.transform(issues_text).toarray()
        x=np.array(x)
        return [x,y]
