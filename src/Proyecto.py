import mysql.connector# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Proyecto
Clase dedicada a almacenar los distintos valores de un proyecto y hacer
las transformaciones de a JSON si ser pide
"""
import json 

class Proyecto:  
    def __init__(self,pid=None,name=None,description=None,issues=None,labels=None):
        self.pid=pid
        self.name=name
        self.description=description
        self.issues=issues
        self.labels=labels
    
    def makeJSONList(self):
        if isinstance(self.issues, json):
            self.issues=json.loads(self.issues)
            self.labels=json.loads(self.labels)
        
    def makeListJSON(self):
        if isinstance(self.issues, json):
            self.issues=json.dumps(self.issues)
            self.labels=json.dumps(self.labels)