# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Formulario Modelos
Formulario utilizado para intercambiar los datos entre el cliente y el servidor relativos a los
modelos guardados
"""
from wtforms import Form, SelectField,validators
from Almacen import Almacen

class FormularioModelo(Form):  
    modelos=SelectField('Modelos almacenados',[validators.DataRequired(message='es necesario seleccionar alguno')],choices=[(n.repositorios,str(n.repositorios)+' '+str(n.stopW)+' '+str(n.idioma)+' '+str(n.comentarios)+' '+str(n.metodo)+' '+str(n.sinEtiqueta)) for n in Almacen.sacarModelo()],validate_choice=False)
