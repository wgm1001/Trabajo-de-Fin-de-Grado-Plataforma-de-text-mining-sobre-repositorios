# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Almacen
Esta clase se dedica a almacenar los proyectos en la base de datos y 
de recuperarlos
"""
import mysql.connector
from datetime import datetime

class Almacen:
    #parametros de la conexion
    conexion={'host':'localhost','user':'Willow','passwd':'Garcia','db':'TFG'}
    #Con este metodo almacenaremos en la base de datos los proyectos recuperados
    @staticmethod
    def guardar(repositorio):
        con =  mysql.connector.connect(host=Almacen.conexion['host'], user=Almacen.conexion['user'], passwd=Almacen.conexion['passwd'], db=Almacen.conexion['db'])
        try:
            cursorRepositorios = con.cursor(prepared=True)
            momento=datetime.now()
            sql_insert_query = ' INSERT INTO Repositorios (idProyecto, Nombre, Descripcion, Momento) VALUES (%s,%s,%s,%s)'                                      
            ins = (repositorio.pid,repositorio.name,repositorio.description, momento)
            cursorRepositorios.execute(sql_insert_query, ins)
            cursorLabels = con.cursor(prepared=True)
            for l in repositorio.labels:
                sql_insert_query = ' INSERT INTO Labels (idProyecto, Momento, idLabel,nombre,color,color_texto,descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s)'                                      
                ins = (repositorio.pid,momento,l['id'],l['name'],l['color'],l['text_color'],l['description'])
                cursorLabels.execute(sql_insert_query, ins)
            cursorIssues = con.cursor(prepared=True)
            for i in repositorio.issues:
                sql_insert_query = ' INSERT INTO Issues (idProyecto, Momento, idIssue,titulo,descripcion,etiquetas,comentarios,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'                                      
                ins = (repositorio.pid,momento,i['id'],i['title'],i['description'],i['labels'],i['notes'],i['state'])
                cursorIssues.execute(sql_insert_query, ins)
            con.commit()
        finally:
            con.close()
    
    @staticmethod 
    def sacarRepositorios():
        projects=None
        con =  mysql.connector.connect(host=Almacen.conexion['host'], user=Almacen.conexion['user'], passwd=Almacen.conexion['passwd'], db=Almacen.conexion['db'])
        try:
            cursor = con.cursor(prepared=True)
            sql_insert_query = ' SELECT * FROM Proyectos'                                      
            cursor.execute(sql_insert_query)
            con.commit()
            projects=cursor.fetchAll()
            for x in projects:
                x.makeJSONList()
        finally:
            con.close()
        return projects