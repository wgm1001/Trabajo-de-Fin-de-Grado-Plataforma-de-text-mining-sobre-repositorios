# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase extractor
Dedicada a la extracción de issues y labels de un repositorio
"""
import Conector
import Almacen
import Proyecto
class Extractor:
    #funciona tanto para un id como para una dirección
    def __init__(self,link):
        gl=Conector.conectar()
        self.__project= gl.projects.get(link)
        
    """
    Extrae y pasa a la clase almacen los distintos parametros necesarios 
    para este proyecto
    """
    def extraer(self):
        project=Proyecto()
        project.pid=self.__project.id
        project.name=self.__project.name
        project.description=self.__project.description
        issues=[]  
        for x in self.__project.issues.list(all=True):
            issues.append({'id':x.iid,'title':x.title,'description':x.description,'labels':x.labels})
        project.issues=issues
        labels=[]  
        for x in self.__project.labels.list(all=True):
            labels.append({'id':x.id,'name':x.name,'color':x.color,'text_color':x.text_color,'description':x.description})
        project.labels=labels
        Almacen.guardar(project)
        