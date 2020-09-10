# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Formulario predicción
Formulario utilizado para intercambiar los datos entre el cliente y el servidor relativos a el
entrenamiento del modelo
"""
from wtforms import Form,SelectMultipleField, SelectField,BooleanField,validators
from src.ModeloSingleClass import ModeloSingleClass
from src.ModeloMultiClass import ModeloMultiClass
from Almacen import Almacen
from nltk.corpus import stopwords
from TranscriptorSingleClass import TranscriptorSingleClass

class FormularioPrediccion(Form):  
    modelo=SelectField('Algoritmo para el modelo',choices=[n for n in list(ModeloSingleClass.switchAlgoritmo.keys())+list(ModeloMultiClass.switchAlgoritmo.keys())],default='MultinomialNB')
    repositorios=SelectMultipleField('Repositorios para entrenar',coerce=int,choices=[(0,'Error, no hay repositorios')])
    multiManual=BooleanField('Definir si se desea que se genere un modelo por etiqueta')
    stopWords=BooleanField('Definir si se usan StopWords')
    idioma=SelectField('Definir idioma de las StopWords',[validators.data_required(message='Es necesario seleccionar algún repositorio')],choices=stopwords.fileids())
    comentarios=BooleanField('Definir si se utilizan comentarios en la predicción')
    metodo=SelectField('Definir método de conteo de palabras',choices=[c for c in list(TranscriptorSingleClass.switchTipoBolsa.keys())],default='CV')
    sinEtiqueta=BooleanField('Definir si se desea tener en cuenta las issues sin etiquetas')
    
    def __init__(self, *args, **kwargs):
        super(FormularioPrediccion, self).__init__(*args, **kwargs)
        repos = [(p.pid,p.name) for p in Almacen.sacarRepositorios()]
        if self.repositorios.choices is None:
            self.repositorios.choices=[(0,'Error, Necesitas descargar antes un repositorio')]
        else:
            self.repositorios.choices = repos