# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba modelo
En esta prueba trataré de familiarizarme con el funcionamiento del modelo a usar para la predicción
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from src.Almacen import Almacen
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm

idioma='spanish'
stop=True
stopWords = set(stopwords.words(idioma))
ran_sta=np.random.RandomState(0)
repositorio=Almacen.sacarRepositorios(idRepositorio=8860457)
issues_text=[]
y=[]
for i in repositorio.issues:
    if len(i.labels)>0:
        temp=i.title
        if i.description is not None:
            temp+=' '+i.description
        for c in i.notes:
            temp+=' '+c
        issues_text.append(temp)
        y.append(i.labels[0])

y=np.array(y)
bolsa = CountVectorizer(stop_words=stopWords)
bolsa.fit(issues_text)
#names = bolsa.get_feature_names()
x=bolsa.transform(issues_text).toarray()
#frequency_matrix = pd.DataFrame(data=x, columns=names)
x=np.array(x)
#x=x.reshape(-1,1)
X_train, X_test, Y_train, Y_test= train_test_split(x, y, random_state=ran_sta)
#training_data = bolsa.fit_transform(X_train)
#testing_data = bolsa.transform(X_test)
clasificador = MultinomialNB()
#clasificador = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,random_state=ran_sta))
#y_score = clasificador.fit(X_train, Y_train).decision_function(X_test)
#print(y_score)
clasificador.fit(X_train, Y_train)
pred=clasificador.predict(X_test)
print(Y_test,pred)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy score: ', format(accuracy_score(Y_test, pred)))




'''
# con SVM
idioma='spanish'
stop=True
stopWords = set(stopwords.words(idioma))
ran_sta=np.random.RandomState(0)
repositorio=Almacen.sacarRepositorios(idRepositorio=8860457)
issues_text=[]
y=[]
for i in repositorio.issues:
    if len(i.labels)>0:
        temp=i.title
        if i.description is not None:
            temp+=' '+i.description
        for c in i.notes:
            temp+=' '+c
        issues_text.append(temp)
        y.append(i.labels)
y=np.array(y)
y=MultiLabelBinarizer().fit_transform(y)
bolsa = CountVectorizer(stop_words=stopWords)
bolsa.fit(issues_text)
x=bolsa.transform(issues_text).toarray()
x=np.array(x)
X_train, X_test, Y_train, Y_test= train_test_split(x, y, random_state=ran_sta)
clasificador = OneVsRestClassifier(svm.SVC(random_state=ran_sta))
clasificador.fit(X_train, Y_train)
pred=clasificador.predict(X_test)
print(Y_test,pred)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy score: ', format(accuracy_score(Y_test, pred)))
'''