# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Formulario Issues
Formulario dedicado a almacenar los valores de una issue
"""
from wtforms import Form, SelectField, StringField, validators

class FormularioIssue(Form):
    titulo=StringField('Título de la issue a predecir',[validators.Required(message='Es necesario el título de la Issue')])
    descripcion=StringField('Descripción de la issue a predecir',[validators.Optional()])
    comentarios=StringField('Comentarios de la issue a elegir',[validators.Optional()])
    estado=SelectField('Estado de la issue',choices=['opened','closed'],validate_choice=False)