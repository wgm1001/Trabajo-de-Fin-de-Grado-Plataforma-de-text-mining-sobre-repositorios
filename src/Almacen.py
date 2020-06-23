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
    def guardar(project):
        con =  mysql.connector.connect(host=Almacen.conexion['host'], user=Almacen.conexion['user'], passwd=Almacen.conexion['passwd'], db=Almacen.conexion['db'])
        try:
            cursor = con.cursor(prepared=True)
            sql_insert_query = ' INSERT INTO Proyectos (idProyecto, Nombre, Descripcion, issues, etiquetas, momento) VALUES (%s,%s,%s,%s,%s,%s)'                                      
            project.makeListJSON()
            ins = (project.pid,project.name,project.description,project.issues,project.labels, datetime.now())
            cursor.execute(sql_insert_query, ins)
            con.commit()
        finally:
            con.close()
    
    @staticmethod
    def sacarTodos():
        projects=None
        con =  mysql.connector.connect(host=Almacen.conexion['host'], user=Almacen.conexion['user'], passwd=Almacen.conexion['passwd'], db=Almacen.conexion['db'])
        try:
            cursor = con.cursor(prepared=True)
            sql_insert_query = ' SELECT * FROM Proyectos '                                      
            cursor.execute(sql_insert_query)
            con.commit()
            projects=cursor.fetchAll()
            for x in projects:
                x.makeJSONList()
        finally:
            con.close()
        return projects