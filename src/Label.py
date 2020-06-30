# -*- coding: utf-8 -*-
"""

@author: Willow Maui García Moreno
Clase Label
Clase dedicada a almacenar los distintos valores de una etiqueta y hacer
las transformaciones a JSON si se pide
"""
class Label:  
    def __init__(self,lid=None,name=None,description=None,color=None,text_color=None):
        self.lid=lid
        self.name=name
        self.description=description
        self.color=color
        self.text_color=text_color