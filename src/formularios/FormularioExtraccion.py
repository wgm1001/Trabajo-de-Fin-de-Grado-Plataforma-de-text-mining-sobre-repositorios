# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Formulario extracción
Formulario utilizado para intercambiar los datos entre el cliente y el servidor relativos a la extracción 
de repositorios
"""
from wtforms import Form, StringField, validators

class FormularioExtraccion(Form):
    url=StringField('Url',[validators.URL(message='Url incorrecta. Introduzca de nuevo la url del repositorio.'),validators.Required(message='Es necesaria la URL')])
    token=StringField('Token privado',[validators.Optional()])
    