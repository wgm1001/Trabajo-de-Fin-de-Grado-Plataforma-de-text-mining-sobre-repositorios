# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase extractor
Dedicada a la extracción de issues y labels de un repositorio
"""
from src.Conector import Conector
from src.Repositorio import Repositorio
from src.Issue import Issue
from src.Label import Label
class Extractor:
    #funciona tanto para un id como para una dirección
    def __init__(self,link,token=None):
        switch_errorcode={404:Exception('Proyecto no encontrado'),401:Exception('Permisos insuficientes')}
        gl=Conector.conectar(token)
        try:
            self.__project= gl.projects.get(link)
        except Exception as e:
            if e.response_code in switch_errorcode.keys():
                raise switch_errorcode[e.response_code]
            raise
        
    """
    Extrae y pasa a la clase almacen los distintos parametros necesarios 
    para este proyecto
    """
    def extraer(self):
            project=Repositorio()
            project.pid=self.__project.id
            project.name=self.__project.name
            project.description=self.__project.description
            issues=[]  
            for x in self.__project.issues.list(all=True):
                issues.append(Issue(iid=x.iid,title=x.title,description=x.description,labels=x.labels,notes=[n.body for n in x.notes.list()],state=x.state))
            project.issues=issues
            labels=[]  
            for x in self.__project.labels.list(all=True):
                labels.append(Label(lid=x.id,name=x.name,color=x.color,text_color=x.text_color,description=x.description))
            project.labels=labels
            return project
        