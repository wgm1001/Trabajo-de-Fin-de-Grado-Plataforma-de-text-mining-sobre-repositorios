# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase transcriptor Multi Class
Clase dedicada a transforma los parametros de un repositorio a la entrada de modelos Multiclase
"""
from src.Almacen import Almacen
import numpy as np
from nltk.corpus import stopwords
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


class TranscriptorMultiClass:  
    switchTipoBolsa={'CV':CountVectorizer,'TFIDF':TfidfVectorizer}
    def __init__(self):
        self.labels=[]
        
    def transcribir_entrenar(self,repositorios,sinEtiqueta,stopW='True',idioma='spanish',comentarios=True,metodo='CV'):
        issues_text=[]
        labels=[]
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
                        labels.append(i.labels)
                    else:
                        if sinEtiqueta:
                            labels.append('Sin etiqueta') 
        y=np.array(labels)
        for l in self.labels:
            if l not in self.labels:
                self.labels.append(l)
        binarizer=MultiLabelBinarizer().fit(y)
        y=binarizer.transform(y)
        tipoBolsa=TranscriptorMultiClass.switchTipoBolsa[metodo]
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
    
    def recuperar(self,y):
        fin=[]
        for i in range(len(y)):
            temp=[]
            for x in range(len(self.labels)):
                if y[i]==1:
                    temp.append(self.labels[x])
            fin.append(temp)
        return fin
    
    def __checkArgs(self,metodo,idioma):
        if metodo not in TranscriptorMultiClass.switchTipoBolsa.keys():
            raise Exception('Argumentos incorrectos')
        if idioma not in stopwords.fileids():
            raise Exception('Argumentos incorrectos')