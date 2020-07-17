# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Issue
Clase dedicada a almacenar los distintos valores de una issue y hacer
las transformaciones a JSON si se pide
"""
import json 

class Issue:  
    def __init__(self,iid=None,title=None,description=None,labels=[],notes=[],state=None):
        self.iid=iid
        self.title=title
        self.description=description
        self.labels=labels
        self.notes=notes
        self.state=state
    
    def makeJSONList(self):
        if isinstance(self.labels, str):
            self.notes=list(json.loads(self.notes))
            self.labels=list(json.loads(self.labels))
        
    def makeListJSON(self):
        if not isinstance(self.labels, str):
            self.notes=json.dumps(self.notes)
            self.labels=json.dumps(self.labels)