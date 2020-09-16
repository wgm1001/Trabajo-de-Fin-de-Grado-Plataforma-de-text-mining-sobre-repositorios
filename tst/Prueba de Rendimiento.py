# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
 Clase Prueba de rendimiento
 Clase que se dedicará a ejecutar una prueba de rendimiento sobre los modelos presentes
"""
from src.Predictor import Predictor
from src.Almacen import Almacen
from datetime import datetime
import os
from time import time
import numpy as np
from sklearn.metrics import jaccard_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score, recall_score
from sklearn.preprocessing import MultiLabelBinarizer

def pruebaEficiencia():
    id_repositorios=[19766159,183616,8860457,6094330,3472737,36189]
    log=open('.'+os.path.sep+'Prueba Eficiencia.txt',"a")
    try:
        log.write("---------Prueba de eficiencia hecha el "+str(datetime.now())+"---------\n")
        from src.ModeloSingleClass import ModeloSingleClass
        from src.ModeloMultiClass import ModeloMultiClass
        algoritmos_single=ModeloSingleClass.switchAlgoritmo.keys()
        algoritmos_multi=ModeloMultiClass.switchAlgoritmo.keys()
#        algoritmos_single=['MultinomialNB']
        for repo in id_repositorios:
            log.write('************** Repositorio '+str(repo)+' **************'+'\n')
            y_test=[]
            mejor_acc=['',0]
            mejor_f1=['',0]
            mejor_precis=['',0]
            mejor_rec=['',0]
            issues=Almacen.sacarRepositorios(repo).issues
            print(repo)
            for prediction in range(len(issues)):
                if not issues[prediction].labels:
                    issues[prediction].labels=['Sin etiqueta']
            y=[i.labels for i in issues]
            y=np.array(y)
            binarizer=MultiLabelBinarizer().fit(y)
            y=binarizer.transform(y)
            for i in issues:
                y_test.append(i.labels)
            for mod in algoritmos_single:
                log.write('____Algoritmo '+mod+' sin multietiqueta_____'+'\n')
                clasificador = Predictor(modelo=mod,MultiManual=False)
                pred=[]
                tiempo_train=0.0
                tiempo_pred=0.0
                accuracy=0
                f1=0
                rec=0
                precis=0
                t0=time()
                clasificador.entrenar(repositorios=[repo],stopW=True,idioma='english',comentarios=True,metodo='CV',sinEtiqueta=True)
                tiempo_train=time()-t0
                t0=time()
                for i in issues:
                    pred.append(clasificador.predecir([str(i.title)+' '+str(i.description)+' '+str(i.state)+' '+str(i.notes)]))
                tiempo_pred+=time()-t0
                pred=np.array(pred)
                pred=binarizer.transform(pred)
                accuracy=jaccard_score(y, pred,average='micro')  
                if accuracy>mejor_acc[1]:
                    mejor_acc[1]=accuracy
                    mejor_acc[0]=mod
                f1=f1_score(y, pred,average='micro')
                if f1>mejor_f1[1]:
                    mejor_f1[1]=f1
                    mejor_f1[0]=mod
                precis=precision_score(y, pred,average='micro')
                if precis>mejor_precis[1]:
                    mejor_precis[1]=precis
                    mejor_precis[0]=mod
                rec=recall_score(y, pred,average='micro')
                if rec>mejor_rec[1]:
                    mejor_rec[1]=rec
                    mejor_rec[0]=mod
                log.write('Accuracy score: %0.7f' % accuracy+' F1 score: %0.7f' % f1+' Precision media score: %0.7f' % precis+' Recall score: %0.7f' % rec+'\n')    
            for mod in algoritmos_single:
                log.write('____Algoritmo '+mod+' con multietiqueta_____'+'\n')
                clasificador = Predictor(modelo=mod,MultiManual=True)
                pred=[]
                tiempo_train=0.0
                tiempo_pred=0.0
                accuracy=0
                f1=0
                rec=0
                precis=0
                t0=time()
                clasificador.entrenar(repositorios=[repo],stopW=True,idioma='english',comentarios=True,metodo='CV',sinEtiqueta=True)
                tiempo_train=time()-t0
                t0=time()
                for i in issues:
                     pred.append(clasificador.predecir([str(i.title)+' '+str(i.description)+' '+str(i.state)+' '+str(i.notes)]))
                tiempo_pred+=time()-t0
                log.write('Entrenamiento %0.5fs' % (tiempo_train)+' Prediccion %0.5fs' %(tiempo_pred)+'\n')
                pred=np.array(pred)
                pred=binarizer.transform(pred)
                accuracy=jaccard_score(y, pred,average='micro')  
                if accuracy>mejor_acc[1]:
                    mejor_acc[1]=accuracy
                    mejor_acc[0]=mod
                f1=f1_score(y, pred,average='micro')
                if f1>mejor_f1[1]:
                    mejor_f1[1]=f1
                    mejor_f1[0]=mod
                precis=precision_score(y, pred,average='micro')
                if precis>mejor_precis[1]:
                    mejor_precis[1]=precis
                    mejor_precis[0]=mod
                rec=recall_score(y, pred,average='micro')
                if rec>mejor_rec[1]:
                    mejor_rec[1]=rec
                    mejor_rec[0]=mod
                log.write('Accuracy score: %0.7f' % accuracy+' F1 score: %0.7f' % f1+' Precision media score: %0.7f' % precis+' Recall score: %0.7f' % rec+'\n')          
            for mod in algoritmos_multi:
                log.write('____Algoritmo '+mod+' sin multietiqueta_____'+'\n')
                clasificador = Predictor(modelo=mod,MultiManual=False)
                pred=[]
                tiempo_train=0.0
                tiempo_pred=0.0
                accuracy=0
                f1=0
                rec=0
                precis=0
                t0=time()
                clasificador.entrenar(repositorios=[repo],stopW=True,idioma='english',comentarios=True,metodo='CV',sinEtiqueta=True)
                tiempo_train=time()-t0
                t0=time()
                for i in issues:
                     pred.append(clasificador.predecir([str(i.title)+' '+str(i.description)+' '+str(i.state)+' '+str(i.notes)]))
                tiempo_pred+=time()-t0
                pred=np.array(pred)
                pred=binarizer.transform(pred)
#                aciertos=0
#                for prediction in range(len(pred)):
#                    if pred[prediction][0] in issues[prediction].labels or (pred[prediction][0]=='Sin etiqueta' and not issues[prediction].labels):
#                        aciertos+=1
#                accuracy=aciertos/len(pred)
                accuracy=jaccard_score(y, pred,average='micro')  
                if accuracy>mejor_acc[1]:
                    mejor_acc[1]=accuracy
                    mejor_acc[0]=mod
                f1=f1_score(y, pred,average='micro')
                if f1>mejor_f1[1]:
                    mejor_f1[1]=f1
                    mejor_f1[0]=mod
                precis=precision_score(y, pred,average='micro')
                if precis>mejor_precis[1]:
                    mejor_precis[1]=precis
                    mejor_precis[0]=mod
                rec=recall_score(y, pred,average='micro')
                if rec>mejor_rec[1]:
                    mejor_rec[1]=rec
                    mejor_rec[0]=mod
                log.write('Accuracy score: %0.7f' % accuracy+' F1 score: %0.7f' % f1+' Precision media score: %0.7f' % precis+' Recall score: %0.7f' % rec+'\n')    
            log.write(' Accuracy mejor con %0.7f es ' % mejor_acc[1]+mejor_acc[0]+' F1 mejor con %0.7f es ' % mejor_f1[1]+mejor_f1[0]+' Recall mejor con %0.7f es ' % mejor_rec[1]+mejor_rec[0]+' Precision  mejor con %0.7f es ' % mejor_precis[1]+mejor_precis[0]+'\n')
    finally:
        log.close()
pruebaEficiencia()