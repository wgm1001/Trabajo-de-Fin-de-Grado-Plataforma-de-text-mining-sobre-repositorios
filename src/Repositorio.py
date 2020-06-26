import mysql.connector# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Proyecto
Clase dedicada a almacenar los distintos valores de un proyecto y hacer
las transformaciones de a JSON si ser pide
"""
import json 

class Repositorio:  
    def __init__(self,pid=None,name=None,description=None,issues=None,labels=None):
        self.pid=pid
        self.name=name
        self.description=description
        self.issues=issues
        self.labels=labels
    
    def makeJSONList(self):
        if isinstance(self.labels, json):
            for i in self.issues:
                i['notes']=json.loads(i['notes'])
                i['labels']=json.loads(i['labels'])
            self.labels=json.loads(self.labels)
        
    def makeListJSON(self):
        if isinstance(self.labels, json):
            for i in self.issues:
                i['notes']=json.dumps(i['notes'])
                i['labels']=json.dumps(i['labels'])
            self.labels=json.dumps(self.labels)