# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba de almacenamiento en la base de datos
"""
import mysql.connector
import gitlab
import os
import json
from datetime import datetime


# Obtención del Token o login
HOST='http://gitlab.com/'
TOKEN_PATH='..'+os.path.sep+'lib'+os.path.sep+'Token.txt'
TOKEN= open(TOKEN_PATH).read()
gl = gitlab.Gitlab(HOST, private_token=TOKEN)
project_url='foundrynet/dnd5e'
project= gl.projects.get(project_url)
id=project.id
issues=project.issues.list()
labels = project.labels.list(all=True)

con =  mysql.connector.connect(host="localhost", user="Willow", passwd="Garcia", db="TFG")
try:
    
    cursor = con.cursor(prepared=True)
    sql_insert_query = """ INSERT INTO prueba
                       (idPrueba, PruebaJSON, PruebaFecha) 
                       VALUES (%s,%s,%s)"""                       
    
    issues_t=[]  
    for x in issues:  
        issues_t.append({'id':x.iid,'description':x.description,'title':x.title})               
    prueba=json.dumps(issues_t)
    
    ins = (id, prueba, datetime.now())
    cursor.execute(sql_insert_query, ins)
    con.commit()

    cur = con.cursor()
    cur.execute("SELECT * FROM Prueba")
    for row in cur.fetchall():
        print(row[0],row[2])
        desc=json.loads(row[1])
        print(desc[0]['id'])
finally:
    con.close()
