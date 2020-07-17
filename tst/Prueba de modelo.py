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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
'''
idioma='spanish'
stop=True
stopWords = set(stopwords.words(idioma))
ran_sta=np.random.RandomState(0)
repositorio=Almacen.sacarRepositorios(idRepositorio=8860457)
issues_text=[]
y=[]
for i in repositorio.issues:
    temp=i.title
    if i.description is not None:
        temp+=' '+i.description
    for c in i.notes:
        temp+=' '+c
    issues_text.append(temp)
    if len(i.labels)>0:
        y.append(i.labels[0])
    else:
        y.append('Sin etiqueta')

y=np.array(y)
bolsa = CountVectorizer(stop_words=stopWords)
#bolsa=TfidfVectorizer(stop_words=stopWords)
#bolsa=HashingVectorizer(stop_words=stopWords,alternate_sign=False)
bolsa.fit(issues_text)
#names = bolsa.get_feature_names()
x=bolsa.transform(issues_text).toarray()
#frequency_matrix = pd.DataFrame(data=x, columns=names)
x=np.array(x)
X_train, X_test, Y_train, Y_test= train_test_split(x, y, random_state=ran_sta)
clasificador = MultinomialNB()
clasificador.fit(X_train, Y_train)
pred=clasificador.predict(X_test)
#print(Y_test,pred)
from sklearn.metrics import accuracy_score
print('Accuracy score: ', format(accuracy_score(Y_test, pred)))
#'''



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
    
    temp=i.title
    if i.description is not None:
        temp+=' '+i.description
    for c in i.notes:
        temp+=' '+c
    issues_text.append(temp)
    if len(i.labels)>0:
        y.append(i.labels[0])
    else:
        y.append('Sin etiqueta')
y=np.array(y)
#y=MultiLabelBinarizer().fit_transform(y)
bolsa = CountVectorizer(stop_words=stopWords)
bolsa.fit(issues_text)
x=bolsa.transform(issues_text).toarray()
x=np.array(x)
X_train, X_test, Y_train, Y_test= train_test_split(x, y, random_state=ran_sta)
clasificador = svm.SVC(random_state=ran_sta)
clasificador.fit(X_train, Y_train)
pred=clasificador.predict(X_test)
print(Y_test,pred)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy score: ', format(accuracy_score(Y_test, pred)))

#'''


#'''

# Prueba multiple


from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, ComplementNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from time import time
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score, recall_score
#'foundrynet/dnd5e' 'inkscape/inkscape','commento/commento','gnachman/iterm2'
# 8860457 3472737 6094330 252461

idioma='spanish'
stop=True
stopWords = set(stopwords.words(idioma))
ran_sta=np.random.RandomState(0)
for idRepositorio in [8860457, 3472737, 6094330, 252461]:
#for idRepositorio in [252461]:
    repositorio=Almacen.sacarRepositorios(idRepositorio=idRepositorio)
    print('='*65)
    print('\033[92m','Repositorio: ',repositorio.pid, repositorio.name,'\033[0m')
    issues_text=[]
    y=[]
    for i in repositorio.issues:
#        if len(i.labels)>0:
#            temp=i.title
#            if i.description is not None:
#                temp+=' '+i.description
#            for c in i.notes:
#                temp+=' '+c
#            issues_text.append(temp)        
#            y.append(i.labels[0])    
        temp=i.title
        if i.description is not None:
            temp+=' '+i.description
        for c in i.notes:
            temp+=' '+c
        issues_text.append(temp)
        for n in range(len(i.labels)):
            y.append(i.labels[n])
            if n>0:
                issues_text.append(temp)
        else:
            y.append('Sin etiqueta')
    
    y=np.array(y)
    bolsa = CountVectorizer(stop_words=stopWords)
    bolsa.fit(issues_text)
    x=bolsa.transform(issues_text).toarray()
    x=np.array(x)
    mejor_acc=['',0]
    mejor_f1=['',0]
    mejor_precis=['',0]
    mejor_rec=['',0]
    kf=KFold(n_splits=10)
    clasificadores=[MultinomialNB(),Perceptron(max_iter=500),svm.SVC(),KNeighborsClassifier(n_neighbors=10),PassiveAggressiveClassifier(max_iter=500),RandomForestClassifier(),NearestCentroid(),BernoulliNB(),ComplementNB()]
#    clasificadores=[MultinomialNB(),Perceptron(max_iter=500),KNeighborsClassifier(n_neighbors=10),PassiveAggressiveClassifier(max_iter=500),RandomForestClassifier(),NearestCentroid(),BernoulliNB(),ComplementNB()]
    for c in clasificadores:
        print('-'*65)
        print('\033[93m','clasificador: ',c.__class__,'\033[0m')
        clasificador = c
        tiempo_train=0.0
        tiempo_pred=0.0
        accuracy=0
        f1=0
        rec=0
        precis=0
        for train_index,test_index in kf.split(x):
            X_train, X_test=x[train_index],x[test_index]
            Y_train, Y_test=y[train_index],y[test_index]
            t0=time()
            clasificador.fit(X_train, Y_train)
            tiempo_train+=time()-t0
            t0=time()
            pred=clasificador.predict(X_test)
            tiempo_pred+=time()-t0
            accuracy+=accuracy_score(Y_test, pred)
            rec+=recall_score(Y_test, pred,average='micro')
            f1+=f1_score(Y_test, pred,average='micro')
            precis+=precision_score(Y_test, pred,average='micro')
        print('Entrenamiento %0.5fs' % (tiempo_train/10),' Prediccion %0.5fs' %(tiempo_pred/10))
        
        accuracy=accuracy/10
        if accuracy>mejor_acc[1]:
            mejor_acc[1]=accuracy
            mejor_acc[0]=c.__class__
        print('Accuracy score: %0.7f' % accuracy)
        
        f1=f1/10
        if f1>mejor_f1[1]:
            mejor_f1[1]=f1
            mejor_f1[0]=c.__class__
        print('F1 score: %0.7f' % f1)
        
        precis=precis/10
        if precis>mejor_precis[1]:
            mejor_precis[1]=precis
            mejor_precis[0]=c.__class__
        print('Precision media score: %0.7f' % precis)
        
        rec=rec/10
        if rec>mejor_rec[1]:
            mejor_rec[1]=rec
            mejor_rec[0]=c.__class__
        print('Recall score: %0.7f' % rec)

    print('~'*65)
    print(' Accuracy mejor con %0.7f es ' % mejor_acc[1],mejor_acc[0])
    print(' F1 mejor con %0.7f es ' % mejor_f1[1],mejor_f1[0])
    print(' Recall mejor con %0.7f es ' % mejor_rec[1],mejor_rec[0])
    print(' Precision  mejor con %0.7f es ' % mejor_precis[1],mejor_precis[0])
    
    
# Repositorio:  8860457 Foundry VTT 5th Edition 
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
#Entrenamiento 0.04821s  Prediccion 0.00130s
#Accuracy score: 0.6271838
#F1 score: 0.6271838
#Precision media score: 0.6271838
#Recall score: 0.6271838
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.svm._classes.SVC'> 
#Entrenamiento 1.60375s  Prediccion 0.09730s
#Accuracy score: 0.6227463
#F1 score: 0.6227463
#Precision media score: 0.6227463
#Recall score: 0.6227463
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
#Entrenamiento 0.25063s  Prediccion 0.00160s
#Accuracy score: 0.5597484
#F1 score: 0.5597484
#Precision media score: 0.5597484
#Recall score: 0.5597484
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
#Entrenamiento 0.26803s  Prediccion 0.14286s
#Accuracy score: 0.6026904
#F1 score: 0.6026904
#Precision media score: 0.6026904
#Recall score: 0.6026904
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
#Entrenamiento 0.59615s  Prediccion 0.00169s
#Accuracy score: 0.6046122
#F1 score: 0.6046122
#Precision media score: 0.6046122
#Recall score: 0.6046122
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
#Entrenamiento 0.45768s  Prediccion 0.00888s
#Accuracy score: 0.6531447
#F1 score: 0.6531447
#Precision media score: 0.6531447
#Recall score: 0.6531447
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
#Entrenamiento 0.01310s  Prediccion 0.00200s
#Accuracy score: 0.2255765
#F1 score: 0.2255765
#Precision media score: 0.2255765
#Recall score: 0.2255765
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
#Entrenamiento 0.06171s  Prediccion 0.00330s
#Accuracy score: 0.6134871
#F1 score: 0.6134871
#Precision media score: 0.6134871
#Recall score: 0.6134871
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
#Entrenamiento 0.04861s  Prediccion 0.00110s
#Accuracy score: 0.5540881
#F1 score: 0.5540881
#Precision media score: 0.5540881
#Recall score: 0.5540881
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Accuracy mejor con 0.6531447 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# F1 mejor con 0.6531447 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# Recall mejor con 0.6531447 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# Precision  mejor con 0.6531447 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
#=================================================================
# Repositorio:  3472737 inkscape 
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
#Entrenamiento 11.72318s  Prediccion 0.05021s
#Accuracy score: 0.3732143
#F1 score: 0.3732143
#Precision media score: 0.3732143
#Recall score: 0.3732143
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.svm._classes.SVC'> 
#Entrenamiento 205.18512s  Prediccion 9.72871s
#Accuracy score: 0.4279762
#F1 score: 0.4279762
#Precision media score: 0.4279762
#Recall score: 0.4279762
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
#Entrenamiento 37.82746s  Prediccion 0.05614s
#Accuracy score: 0.3464286
#F1 score: 0.3464286
#Precision media score: 0.3464286
#Recall score: 0.3464286
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
#Entrenamiento 10.49703s  Prediccion 13.62207s
#Accuracy score: 0.3946429
#F1 score: 0.3946429
#Precision media score: 0.3946429
#Recall score: 0.3946429
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
#Entrenamiento 74.34363s  Prediccion 0.06195s
#Accuracy score: 0.4101190
#F1 score: 0.4101190
#Precision media score: 0.4101190
#Recall score: 0.4101190
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
#Entrenamiento 9.77805s  Prediccion 0.04941s
#Accuracy score: 0.4464286
#F1 score: 0.4464286
#Precision media score: 0.4464286
#Recall score: 0.4464286
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
#Entrenamiento 0.39513s  Prediccion 0.07257s
#Accuracy score: 0.1636905
#F1 score: 0.1636905
#Precision media score: 0.1636905
#Recall score: 0.1636905
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
#Entrenamiento 12.75371s  Prediccion 0.15461s
#Accuracy score: 0.3869048
#F1 score: 0.3869048
#Precision media score: 0.3869048
#Recall score: 0.3869048
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
#Entrenamiento 12.41282s  Prediccion 0.05519s
#Accuracy score: 0.3821429
#F1 score: 0.3821429
#Precision media score: 0.3821429
#Recall score: 0.3821429
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Accuracy mejor con 0.4464286 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# F1 mejor con 0.4464286 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# Recall mejor con 0.4464286 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# Precision  mejor con 0.4464286 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
#=================================================================
# Repositorio:  6094330 Commento 
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
#Entrenamiento 0.06181s  Prediccion 0.00140s
#Accuracy score: 0.4550189
#F1 score: 0.4550189
#Precision media score: 0.4550189
#Recall score: 0.4550189
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.svm._classes.SVC'> 
#Entrenamiento 1.23716s  Prediccion 0.04794s
#Accuracy score: 0.3541667
#F1 score: 0.3541667
#Precision media score: 0.3541667
#Recall score: 0.3541667
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
#Entrenamiento 0.28092s  Prediccion 0.00120s
#Accuracy score: 0.3752841
#F1 score: 0.3752841
#Precision media score: 0.3752841
#Recall score: 0.3752841
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
#Entrenamiento 0.16706s  Prediccion 0.06668s
#Accuracy score: 0.3754735
#F1 score: 0.3754735
#Precision media score: 0.3754735
#Recall score: 0.3754735
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
#Entrenamiento 0.66885s  Prediccion 0.00100s
#Accuracy score: 0.4000947
#F1 score: 0.4000947
#Precision media score: 0.4000947
#Recall score: 0.4000947
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
#Entrenamiento 0.35014s  Prediccion 0.00861s
#Accuracy score: 0.4063447
#F1 score: 0.4063447
#Precision media score: 0.4063447
#Recall score: 0.4063447
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
#Entrenamiento 0.00960s  Prediccion 0.00170s
#Accuracy score: 0.1894886
#F1 score: 0.1894886
#Precision media score: 0.1894886
#Recall score: 0.1894886
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
#Entrenamiento 0.07070s  Prediccion 0.00340s
#Accuracy score: 0.4029356
#F1 score: 0.4029356
#Precision media score: 0.4029356
#Recall score: 0.4029356
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
#Entrenamiento 0.06077s  Prediccion 0.00140s
#Accuracy score: 0.4276515
#F1 score: 0.4276515
#Precision media score: 0.4276515
#Recall score: 0.4276515
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Accuracy mejor con 0.4550189 es  <class 'sklearn.naive_bayes.MultinomialNB'>
# F1 mejor con 0.4550189 es  <class 'sklearn.naive_bayes.MultinomialNB'>
# Recall mejor con 0.4550189 es  <class 'sklearn.naive_bayes.MultinomialNB'>
# Precision  mejor con 0.4550189 es  <class 'sklearn.naive_bayes.MultinomialNB'>    

#=================================================================
# Repositorio:  252461 iterm2 
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
#Entrenamiento 212.10632s  Prediccion 0.59249s
#Accuracy score: 0.9411765
#F1 score: 0.9411765
#Precision media score: 0.9411765
#Recall score: 0.9411765
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
#Entrenamiento 352.07923s  Prediccion 0.72245s
#Accuracy score: 0.9320136
#F1 score: 0.9320136
#Precision media score: 0.9320136
#Recall score: 0.9320136
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
#Entrenamiento 257.21955s  Prediccion 1156.38593s
#Accuracy score: 0.9122172
#F1 score: 0.9122172
#Precision media score: 0.9122172
#Recall score: 0.9122172
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
#Entrenamiento 470.65498s  Prediccion 0.88223s
#Accuracy score: 0.9538462
#F1 score: 0.9538462
#Precision media score: 0.9538462
#Recall score: 0.9538462
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
#Entrenamiento 144.53358s  Prediccion 0.59702s
#Accuracy score: 0.9605204
#F1 score: 0.9605204
#Precision media score: 0.9605204
#Recall score: 0.9605204
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
#Entrenamiento 6.23328s  Prediccion 1.06792s
#Accuracy score: 0.2953620
#F1 score: 0.2953620
#Precision media score: 0.2953620
#Recall score: 0.2953620
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
#Entrenamiento 222.53930s  Prediccion 1.73950s
#Accuracy score: 0.9561086
#F1 score: 0.9561086
#Precision media score: 0.9561086
#Recall score: 0.9561086
#-----------------------------------------------------------------
# clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
#Entrenamiento 211.59906s  Prediccion 0.65440s
#Accuracy score: 0.9363122
#F1 score: 0.9363122
#Precision media score: 0.9363122
#Recall score: 0.9363122
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Accuracy mejor con 0.9605204 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# F1 mejor con 0.9605204 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# Recall mejor con 0.9605204 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
# Precision  mejor con 0.9605204 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>    
#'''
'''
Sin sin etiqueta

=================================================================
 Repositorio:  8860457 Foundry VTT 5th Edition 
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
Entrenamiento 0.01030s  Prediccion 0.00080s
Accuracy score: 0.7600000
F1 score: 0.7600000
Precision media score: 0.7600000
Recall score: 0.7600000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
Entrenamiento 0.04860s  Prediccion 0.00050s
Accuracy score: 0.6950000
F1 score: 0.6950000
Precision media score: 0.6950000
Recall score: 0.6950000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.svm._classes.SVC'> 
Entrenamiento 0.14584s  Prediccion 0.00840s
Accuracy score: 0.7500000
F1 score: 0.7500000
Precision media score: 0.7500000
Recall score: 0.7500000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
Entrenamiento 0.04209s  Prediccion 0.01361s
Accuracy score: 0.7500000
F1 score: 0.7500000
Precision media score: 0.7500000
Recall score: 0.7500000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
Entrenamiento 0.09692s  Prediccion 0.00070s
Accuracy score: 0.7450000
F1 score: 0.7450000
Precision media score: 0.7450000
Recall score: 0.7450000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
Entrenamiento 0.13781s  Prediccion 0.00742s
Accuracy score: 0.7550000
F1 score: 0.7550000
Precision media score: 0.7550000
Recall score: 0.7550000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
Entrenamiento 0.00330s  Prediccion 0.00080s
Accuracy score: 0.3450000
F1 score: 0.3450000
Precision media score: 0.3450000
Recall score: 0.3450000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
Entrenamiento 0.01323s  Prediccion 0.00070s
Accuracy score: 0.7350000
F1 score: 0.7350000
Precision media score: 0.7350000
Recall score: 0.7350000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
Entrenamiento 0.00995s  Prediccion 0.00030s
Accuracy score: 0.7450000
F1 score: 0.7450000
Precision media score: 0.7450000
Recall score: 0.7450000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Accuracy mejor con 0.7600000 es  <class 'sklearn.naive_bayes.MultinomialNB'>
 F1 mejor con 0.7600000 es  <class 'sklearn.naive_bayes.MultinomialNB'>
 Recall mejor con 0.7600000 es  <class 'sklearn.naive_bayes.MultinomialNB'>
 Precision  mejor con 0.7600000 es  <class 'sklearn.naive_bayes.MultinomialNB'>
=================================================================
 Repositorio:  3472737 inkscape 
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
Entrenamiento 5.89139s  Prediccion 0.04202s
Accuracy score: 0.4376849
F1 score: 0.4376849
Precision media score: 0.4376849
Recall score: 0.4376849
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
Entrenamiento 27.07194s  Prediccion 0.04386s
Accuracy score: 0.3591388
F1 score: 0.3591388
Precision media score: 0.3591388
Recall score: 0.3591388
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.svm._classes.SVC'> 
Entrenamiento 138.34477s  Prediccion 6.19535s
Accuracy score: 0.4241236
F1 score: 0.4241236
Precision media score: 0.4241236
Recall score: 0.4241236
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
Entrenamiento 8.37026s  Prediccion 8.96570s
Accuracy score: 0.4176900
F1 score: 0.4176900
Precision media score: 0.4176900
Recall score: 0.4176900
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
Entrenamiento 52.54827s  Prediccion 0.04131s
Accuracy score: 0.4190983
F1 score: 0.4190983
Precision media score: 0.4190983
Recall score: 0.4190983
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
Entrenamiento 7.62121s  Prediccion 0.03762s
Accuracy score: 0.4476545
F1 score: 0.4476545
Precision media score: 0.4476545
Recall score: 0.4476545
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
Entrenamiento 0.28181s  Prediccion 0.05817s
Accuracy score: 0.1499240
F1 score: 0.1499240
Precision media score: 0.1499240
Recall score: 0.1499240
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
Entrenamiento 6.17951s  Prediccion 0.10372s
Accuracy score: 0.4269504
F1 score: 0.4269504
Precision media score: 0.4269504
Recall score: 0.4269504
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
Entrenamiento 5.87998s  Prediccion 0.03901s
Accuracy score: 0.4347974
F1 score: 0.4347974
Precision media score: 0.4347974
Recall score: 0.4347974
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Accuracy mejor con 0.4476545 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
 F1 mejor con 0.4476545 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
 Recall mejor con 0.4476545 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
 Precision  mejor con 0.4476545 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
=================================================================
 Repositorio:  6094330 Commento 
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
Entrenamiento 0.03356s  Prediccion 0.00080s
Accuracy score: 0.5838333
F1 score: 0.5838333
Precision media score: 0.5838333
Recall score: 0.5838333
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
Entrenamiento 0.15104s  Prediccion 0.00070s
Accuracy score: 0.5631667
F1 score: 0.5631667
Precision media score: 0.5631667
Recall score: 0.5631667
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.svm._classes.SVC'> 
Entrenamiento 0.61661s  Prediccion 0.02172s
Accuracy score: 0.4941667
F1 score: 0.4941667
Precision media score: 0.4941667
Recall score: 0.4941667
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
Entrenamiento 0.07888s  Prediccion 0.02793s
Accuracy score: 0.4690000
F1 score: 0.4690000
Precision media score: 0.4690000
Recall score: 0.4690000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
Entrenamiento 0.37071s  Prediccion 0.00050s
Accuracy score: 0.5628333
F1 score: 0.5628333
Precision media score: 0.5628333
Recall score: 0.5628333
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
Entrenamiento 0.19555s  Prediccion 0.00770s
Accuracy score: 0.5350000
F1 score: 0.5350000
Precision media score: 0.5350000
Recall score: 0.5350000
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
Entrenamiento 0.00530s  Prediccion 0.00100s
Accuracy score: 0.2201667
F1 score: 0.2201667
Precision media score: 0.2201667
Recall score: 0.2201667
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
Entrenamiento 0.03871s  Prediccion 0.00190s
Accuracy score: 0.5063333
F1 score: 0.5063333
Precision media score: 0.5063333
Recall score: 0.5063333
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
Entrenamiento 0.03296s  Prediccion 0.00050s
Accuracy score: 0.5346667
F1 score: 0.5346667
Precision media score: 0.5346667
Recall score: 0.5346667
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Accuracy mejor con 0.5838333 es  <class 'sklearn.naive_bayes.MultinomialNB'>
 F1 mejor con 0.5838333 es  <class 'sklearn.naive_bayes.MultinomialNB'>
 Recall mejor con 0.5838333 es  <class 'sklearn.naive_bayes.MultinomialNB'>
 Precision  mejor con 0.5838333 es  <class 'sklearn.naive_bayes.MultinomialNB'>
=================================================================
 Repositorio:  252461 iterm2 
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
Entrenamiento 14.85985s  Prediccion 0.06902s
Accuracy score: 0.9044199
F1 score: 0.9044199
Precision media score: 0.9044199
Recall score: 0.9044199
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
Entrenamiento 28.65109s  Prediccion 0.07500s
Accuracy score: 0.8914365
F1 score: 0.8914365
Precision media score: 0.8914365
Recall score: 0.8914365
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.svm._classes.SVC'> 
Entrenamiento 246.05609s  Prediccion 15.00563s
Accuracy score: 0.9146409
F1 score: 0.9146409
Precision media score: 0.9146409
Recall score: 0.9146409
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
Entrenamiento 20.81560s  Prediccion 46.66056s
Accuracy score: 0.9116022
F1 score: 0.9116022
Precision media score: 0.9116022
Recall score: 0.9116022
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
Entrenamiento 46.71396s  Prediccion 0.08692s
Accuracy score: 0.9060773
F1 score: 0.9060773
Precision media score: 0.9060773
Recall score: 0.9060773
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
Entrenamiento 23.95814s  Prediccion 0.08292s
Accuracy score: 0.9171271
F1 score: 0.9171271
Precision media score: 0.9171271
Recall score: 0.9171271
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
Entrenamiento 0.62321s  Prediccion 0.10667s
Accuracy score: 0.3497238
F1 score: 0.3497238
Precision media score: 0.3497238
Recall score: 0.3497238
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
Entrenamiento 15.66803s  Prediccion 0.19685s
Accuracy score: 0.8994475
F1 score: 0.8994475
Precision media score: 0.8994475
Recall score: 0.8994475
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
Entrenamiento 14.54424s  Prediccion 0.07557s
Accuracy score: 0.8928177
F1 score: 0.8928177
Precision media score: 0.8928177
Recall score: 0.8928177
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Accuracy mejor con 0.9171271 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
 F1 mejor con 0.9171271 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
 Recall mejor con 0.9171271 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
 Precision  mejor con 0.9171271 es  <class 'sklearn.ensemble._forest.RandomForestClassifier'>
'''
'''
=================================================================
 Repositorio:  8860457 Foundry VTT 5th Edition 
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
Entrenamiento 0.03661s  Prediccion 0.00130s
Accuracy score: 0.7007407
F1 score: 0.7007407
Precision media score: 0.7007407
Recall score: 0.7007407
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
Entrenamiento 0.19160s  Prediccion 0.00140s
Accuracy score: 0.6037710
F1 score: 0.6037710
Precision media score: 0.6037710
Recall score: 0.6037710
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.svm._classes.SVC'> 
Entrenamiento 1.64618s  Prediccion 0.09704s
Accuracy score: 0.7446465
F1 score: 0.7446465
Precision media score: 0.7446465
Recall score: 0.7446465
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
Entrenamiento 0.30291s  Prediccion 0.15844s
Accuracy score: 0.7354882
F1 score: 0.7354882
Precision media score: 0.7354882
Recall score: 0.7354882
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
Entrenamiento 0.46482s  Prediccion 0.00190s
Accuracy score: 0.6272054
F1 score: 0.6272054
Precision media score: 0.6272054
Recall score: 0.6272054
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
Entrenamiento 0.63878s  Prediccion 0.00950s
Accuracy score: 0.7428283
F1 score: 0.7428283
Precision media score: 0.7428283
Recall score: 0.7428283
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
Entrenamiento 0.01330s  Prediccion 0.00190s
Accuracy score: 0.4461616
F1 score: 0.4461616
Precision media score: 0.4461616
Recall score: 0.4461616
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
Entrenamiento 0.04981s  Prediccion 0.00390s
Accuracy score: 0.6803367
F1 score: 0.6803367
Precision media score: 0.6803367
Recall score: 0.6803367
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
Entrenamiento 0.03643s  Prediccion 0.00130s
Accuracy score: 0.6143434
F1 score: 0.6143434
Precision media score: 0.6143434
Recall score: 0.6143434
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Accuracy mejor con 0.7446465 es  <class 'sklearn.svm._classes.SVC'>
 F1 mejor con 0.7446465 es  <class 'sklearn.svm._classes.SVC'>
 Recall mejor con 0.7446465 es  <class 'sklearn.svm._classes.SVC'>
 Precision  mejor con 0.7446465 es  <class 'sklearn.svm._classes.SVC'>
=================================================================
 Repositorio:  3472737 inkscape 
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
Entrenamiento 40.05670s  Prediccion 0.10893s
Accuracy score: 0.3101888
F1 score: 0.3101888
Precision media score: 0.3101888
Recall score: 0.3101888
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
Entrenamiento 69.17763s  Prediccion 0.10838s
Accuracy score: 0.1048221
F1 score: 0.1048221
Precision media score: 0.1048221
Recall score: 0.1048221
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.svm._classes.SVC'> 
Entrenamiento 1006.06332s  Prediccion 40.50082s
Accuracy score: 0.3504615
F1 score: 0.3504615
Precision media score: 0.3504615
Recall score: 0.3504615
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
Entrenamiento 26.11209s  Prediccion 54.13130s
Accuracy score: 0.3004729
F1 score: 0.3004729
Precision media score: 0.3004729
Recall score: 0.3004729
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
Entrenamiento 161.57839s  Prediccion 0.10597s
Accuracy score: 0.2091013
F1 score: 0.2091013
Precision media score: 0.2091013
Recall score: 0.2091013
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
Entrenamiento 139.72166s  Prediccion 0.11130s
Accuracy score: 0.3490338
F1 score: 0.3490338
Precision media score: 0.3490338
Recall score: 0.3490338
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
Entrenamiento 0.75956s  Prediccion 0.14853s
Accuracy score: 0.0179959
F1 score: 0.0179959
Precision media score: 0.0179959
Recall score: 0.0179959
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
Entrenamiento 43.60043s  Prediccion 0.24186s
Accuracy score: 0.3293276
F1 score: 0.3293276
Precision media score: 0.3293276
Recall score: 0.3293276
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
Entrenamiento 40.25705s  Prediccion 0.09612s
Accuracy score: 0.1882279
F1 score: 0.1882279
Precision media score: 0.1882279
Recall score: 0.1882279
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Accuracy mejor con 0.3504615 es  <class 'sklearn.svm._classes.SVC'>
 F1 mejor con 0.3504615 es  <class 'sklearn.svm._classes.SVC'>
 Recall mejor con 0.3504615 es  <class 'sklearn.svm._classes.SVC'>
 Precision  mejor con 0.3504615 es  <class 'sklearn.svm._classes.SVC'>
=================================================================
 Repositorio:  6094330 Commento 
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
Entrenamiento 0.10838s  Prediccion 0.00190s
Accuracy score: 0.3058584
F1 score: 0.3058584
Precision media score: 0.3058584
Recall score: 0.3058584
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._perceptron.Perceptron'> 
Entrenamiento 0.57069s  Prediccion 0.00200s
Accuracy score: 0.1743734
F1 score: 0.1743734
Precision media score: 0.1743734
Recall score: 0.1743734
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.svm._classes.SVC'> 
Entrenamiento 3.23252s  Prediccion 0.13471s
Accuracy score: 0.3866541
F1 score: 0.3866541
Precision media score: 0.3866541
Recall score: 0.3866541
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._classification.KNeighborsClassifier'> 
Entrenamiento 0.36344s  Prediccion 0.19225s
Accuracy score: 0.3515038
F1 score: 0.3515038
Precision media score: 0.3515038
Recall score: 0.3515038
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.linear_model._passive_aggressive.PassiveAggressiveClassifier'> 
Entrenamiento 1.20545s  Prediccion 0.00199s
Accuracy score: 0.2320489
F1 score: 0.2320489
Precision media score: 0.2320489
Recall score: 0.2320489
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.ensemble._forest.RandomForestClassifier'> 
Entrenamiento 1.83038s  Prediccion 0.00967s
Accuracy score: 0.3761278
F1 score: 0.3761278
Precision media score: 0.3761278
Recall score: 0.3761278
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.neighbors._nearest_centroid.NearestCentroid'> 
Entrenamiento 0.01480s  Prediccion 0.00260s
Accuracy score: 0.0931704
F1 score: 0.0931704
Precision media score: 0.0931704
Recall score: 0.0931704
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.BernoulliNB'> 
Entrenamiento 0.12273s  Prediccion 0.00450s
Accuracy score: 0.3444236
F1 score: 0.3444236
Precision media score: 0.3444236
Recall score: 0.3444236
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.ComplementNB'> 
Entrenamiento 0.10698s  Prediccion 0.00150s
Accuracy score: 0.1864662
F1 score: 0.1864662
Precision media score: 0.1864662
Recall score: 0.1864662
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Accuracy mejor con 0.3866541 es  <class 'sklearn.svm._classes.SVC'>
 F1 mejor con 0.3866541 es  <class 'sklearn.svm._classes.SVC'>
 Recall mejor con 0.3866541 es  <class 'sklearn.svm._classes.SVC'>
 Precision  mejor con 0.3866541 es  <class 'sklearn.svm._classes.SVC'>
=================================================================
 Repositorio:  252461 iterm2 
-----------------------------------------------------------------
 clasificador:  <class 'sklearn.naive_bayes.MultinomialNB'> 
Entrenamiento 477.71886s  Prediccion 11.22950s
Accuracy score: 0.2394352
F1 score: 0.2394352
Precision media score: 0.2394352
Recall score: 0.2394352
-----------------------------------------------------------------
'''


'''
#con one vs rest con SVM
idioma='spanish'
stop=True
stopWords = set(stopwords.words(idioma))
ran_sta=np.random.RandomState(0)
repositorio=Almacen.sacarRepositorios(idRepositorio=8860457)
issues_text=[]
y=[]
for i in repositorio.issues:
    temp=i.title
    if i.description is not None:
        temp+=' '+i.description
    for c in i.notes:
        temp+=' '+c
    issues_text.append(temp)
    if len(i.labels)>0:
        y.append(i.labels)
    else:
        y.append(['Sin etiqueta'])
yp=y
y=np.array(y)
mul=MultiLabelBinarizer().fit(y)
y=mul.transform(y)
bolsa = CountVectorizer(stop_words=stopWords)
bolsa.fit(issues_text)
x=bolsa.transform(issues_text).toarray()
x=np.array(x)
X_train, X_test, Y_train, Y_test= train_test_split(x, y, random_state=ran_sta)
clasificador = OneVsRestClassifier(svm.SVC(random_state=ran_sta))
clasificador.fit(X_train, Y_train)
pred=clasificador.predict(X_test)
for i in range(len(Y_test)):    
    print(Y_test[i],pred[i])
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy score: ', format(accuracy_score(Y_test, pred)))
#'''