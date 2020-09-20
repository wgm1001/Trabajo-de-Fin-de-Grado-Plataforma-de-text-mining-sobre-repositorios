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
    modelos=SelectField('Modelos almacenados', validators=[validators.DataRequired(message='es necesario seleccionar alguno')],choices=[('No hay modelos entrenados')],validate_choice=False)
    def __init__(self, *args, **kwargs):
            super(FormularioModelo, self).__init__(*args, **kwargs)
            self.modelos.choices = [(n.repositorios,str(n.repositorios)+' '+str(n.modelo)+' '+str(n.stopW)+' '+str(n.idioma)+' '+str(n.comentarios)+' '+str(n.metodo)+' '+str(n.sinEtiqueta)) for n in Almacen.sacarModelo()]
            #self.modelos.choices = [(n.repositorios,str(n.repositorios)+' '+str(n.modelo)+' '+str(n.MultiManual)+' '+str(n.stopW)+' '+str(n.idioma)+' '+str(n.comentarios)+' '+str(n.metodo)+' '+str(n.sinEtiqueta)) for n in Almacen.sacarModelo()]