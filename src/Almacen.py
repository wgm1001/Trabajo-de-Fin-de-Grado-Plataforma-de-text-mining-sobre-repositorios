# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Almacen
Esta clase se dedica a almacenar los proyectos en la base de datos y 
de recuperarlos
"""
import mysql.connector
from datetime import datetime
from src import Repositorio
from src import Label
from src import Issue

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
            repositorio.makeListJSON()
            sql_insert_query = ' INSERT INTO repositorios (idProyecto, nombre, descripcion, momento) VALUES (%s,%s,%s,%s)'                                      
            ins = (repositorio.pid,repositorio.name,repositorio.description, momento)
            cursorRepositorios.execute(sql_insert_query, ins)
            cursorLabels = con.cursor(prepared=True)
            for l in repositorio.labels:
                sql_insert_query = ' INSERT INTO labels (idProyecto, momento, idLabel,nombre,color,color_texto,descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s)'                                      
                ins = (repositorio.pid,momento,l.lid,l.name,l.color,l.text_color,l.description)
                cursorLabels.execute(sql_insert_query, ins)
            cursorIssues = con.cursor(prepared=True)
            for i in repositorio.issues:
                sql_insert_query = ' INSERT INTO issues (idProyecto, momento, idIssue,titulo,descripcion,etiquetas,comentarios,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'                                      
                ins = (repositorio.pid,momento,i.iid,i.title,i.description,i.labels,i.notes,i.state)
                cursorIssues.execute(sql_insert_query, ins)
            con.commit()
        finally:
            con.close()

    @staticmethod
    def sacarRepositorios(idRepositorio=None,moment=None):
        projects=[]
        con =  mysql.connector.connect(host=Almacen.conexion['host'], user=Almacen.conexion['user'], passwd=Almacen.conexion['passwd'], db=Almacen.conexion['db'])
        try:
            cursor = con.cursor(buffered=True,dictionary=True)
            if idRepositorio is None:
                sql_select_query = ' SELECT * FROM repositorios'
            else:
                if (moment is None):
                    sql_select_query = ' SELECT * FROM repositorios where idProyecto='+str(idRepositorio)+' and momento=(select max(momento) from repositorios where idProyecto='+str(idRepositorio)+')'
                else:
                     sql_select_query = ' SELECT * FROM repositorios where idProyecto='+str(idRepositorio)+' and momento='+str(moment)                              
            cursor.execute(sql_select_query)
            cursorIssues = con.cursor(prepared=True)
            sql_select_issues_query = ' SELECT * FROM issues where idProyecto=%s and momento=%s' 
            cursorLabels = con.cursor(prepared=True)
            sql_select_labels_query = ' SELECT * FROM labels where idProyecto=%s and momento=%s' 
            for p in cursor:
                cursorIssues.execute(sql_select_issues_query, (p['idProyecto'],p['momento']))
                issues_d=[]
                for i in cursorIssues:
                    # issues_d.append(Issue.Issue(iid=i['idIssue'],title=i['titulo'],description=i['descripcion'],labels=i['etiquetas'],notes=i['comentarios'],state=i['status']))
                    issues_d.append(Issue.Issue(iid=i[2],title=i[3],description=i[4],labels=i[5],notes=i[6],state=i[7]))
                cursorLabels.execute(sql_select_labels_query, (p['idProyecto'],p['momento']))
                labels_d=[]
                for l in cursorLabels:
                    # labels_d.append(Label.Label(lid=l['idLabel'],name=l['nombre'],color=l['color'],text_color=l['color_texto'],description=l['descripcion']))
                    labels_d.append(Label.Label(lid=l[2],name=l[3],color=l[4],text_color=l[5],description=l[6]))
                projects.append(Repositorio.Repositorio(pid=p['idProyecto'],name=p['Nombre'],description=p['Descripcion'],issues=issues_d,labels=labels_d))
            for p in projects:
                p.makeJSONList()
        finally:
            con.close()
        ret=projects[0] if idRepositorio is not None else projects
        return ret