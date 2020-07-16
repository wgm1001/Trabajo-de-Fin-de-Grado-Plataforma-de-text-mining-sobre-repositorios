# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase transcriptor Single Class
Clase dedicada a transforma los parametros de un repositorio para los modelos de prediccion de una
sola clase
"""
from src.Almacen import Almacen
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

class TranscriptorSingleClass:
    switchTipoBolsa={'CV':CountVectorizer,'TFIDF':TfidfVectorizer}
    def transcribir_entrenar(self,repositorios,sinEtiqueta,stopW='True',idioma='spanish',comentarios=True,metodo='CV'):
        self.__checkArgs(idioma=idioma,metodo=metodo)
        issues_text=[]
        y=[]
        for r in repositorios:
            repositorio=Almacen.sacarRepositorios(idRepositorio=r)
            for i in repositorio.issues:
                if sinEtiqueta or len(i.labels)>0:
                    temp=i.title
                    if i.description is not None:
                        temp+=' '+i.description
                    if comentarios:
                        for c in i.notes:
                            temp+=' '+c
                    issues_text.append(temp)
                    if len(i.labels)>0:
                        y.append(i.labels[0])
                    else:
                        if sinEtiqueta:
                            y.append('Sin etiqueta')
        y=np.array(y)
        tipoBolsa=TranscriptorSingleClass.switchTipoBolsa[metodo]
        if stopW:
            stopWords = set(stopwords.words(idioma))
            self.bolsa = tipoBolsa(stop_words=stopWords)
        else:
            self.bolsa = tipoBolsa()
            
        self.bolsa.fit(issues_text)
        x=self.bolsa.transform(issues_text).toarray()
        x=np.array(x)
        return [x,y]
    
    def transcribir(self,y):
        ret=self.bolsa.transform(y).toarray()
        return np.array(ret)
    
    def __checkArgs(self,metodo,idioma):
        if metodo not in TranscriptorSingleClass.switchTipoBolsa.keys():
            raise Exception('Argumentos incorrectos')
        if idioma not in stopwords.fileids():
            raise Exception('Argumentos incorrectos')
        