# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Almacen
Esta clase se dedica a almacenar los proyectos en la base de datos y 
de recuperarlos
"""
import mysql.connector
from datetime import datetime
from src.Repositorio import Repositorio
from src.Label import Label
from src.Issue import Issue
import json
import pickle
import os

class Almacen:
    conexion=dict()
    #Ruta del archivo con los parametros de la conexión
    CON_PATH='..'+os.path.sep+'lib'+os.path.sep+'Conexion.txt'
    #esta variable se usa para almacenar si el programa ha cargado ya los datos de la conexión
    con_cargada=False
    #Con este metodo almacenaremos en la base de datos los proyectos recuperados
    @staticmethod
    def guardar(repositorio):
        if not isinstance(repositorio,Repositorio):
            raise Exception('Tipo a guardar incorrecto')
        con =  Almacen.getCon()
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
    
    def guardarModelo(modelo):
        con =  Almacen.getCon()
        try:
            repositorios=modelo.repositorios
            cursorModelo = con.cursor(prepared=True)
            momento=datetime.now()
            modelo.momento=momento
            sql_insert_query = ' INSERT INTO modelos (idProyectos, momento, modelo) VALUES (%s,%s,%s)'                                     
            ins = (json.dumps(repositorios),momento,pickle.dumps(modelo))
            cursorModelo.execute(sql_insert_query, ins)
            con.commit()
        finally:
            con.close()
            
    def sacarModelo(repositorios=None):
        con = Almacen.getCon() 
        try:
            cursorModelo = con.cursor(prepared=True)
            if repositorios is not None:
                sql_select_query = ' SELECT modelo FROM modelos where idProyectos=\''+str(repositorios)+'\' and momento=(select max(momento) from modelos where idProyectos=\''+str(repositorios)+'\')'
            else:
                sql_select_query = ' SELECT modelo FROM modelos order by momento desc'
            cursorModelo.execute(sql_select_query)
            modelos=[]
            modelos_id=[]
            for i in cursorModelo.fetchall():
                m=pickle.loads(i[0])
                if m.repositorios not in modelos_id:
                    modelos.append(m)
                    modelos_id.append(m.repositorios)
            modelos=modelos[0] if repositorios is not None else modelos
            return modelos
        finally:
            con.close()
    
    @staticmethod
    def sacarRepositorios(idRepositorio=None,moment=None):
        Almacen.__checkArgsSacar(idRepositorio=idRepositorio,moment=moment)
        projects=[]
        con = Almacen.getCon()
        try:
            cursor = con.cursor(buffered=True,dictionary=True)
            if idRepositorio is None:
                sql_select_query = ' SELECT * FROM repositorios order by momento desc'
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
                    # issues_d.append(Issue(iid=i['idIssue'],title=i['titulo'],description=i['descripcion'],labels=i['etiquetas'],notes=i['comentarios'],state=i['status']))
                    issues_d.append(Issue(iid=i[2],title=Almacen.dcd(i[3]),description=Almacen.dcd(i[4]),labels=Almacen.dcd(i[5]),notes=Almacen.dcd(i[6]),state=Almacen.dcd(i[7])))
                cursorLabels.execute(sql_select_labels_query, (p['idProyecto'],p['momento']))
                labels_d=[]
                for l in cursorLabels:
                    # labels_d.append(Label(lid=l['idLabel'],name=l['nombre'],color=l['color'],text_color=l['color_texto'],description=l['descripcion']))
                    labels_d.append(Label(lid=l[2],name=Almacen.dcd(l[3]),color=Almacen.dcd(l[4]),text_color=Almacen.dcd(l[5]),description=Almacen.dcd(l[6])))
                repo=Repositorio(pid=Almacen.dcd(p['idProyecto']),name=Almacen.dcd(p['Nombre']),description=Almacen.dcd(p['Descripcion']),issues=issues_d,labels=labels_d)
                if repo.pid not in [p.pid for p in projects ] :
                    projects.append(repo)
            for p in projects:
                p.makeJSONList()
        finally:
            con.close()
        if not projects and idRepositorio is not None:
            raise Exception('Id de repositorio no encontrado.')
        if not projects and idRepositorio is None:
            raise Exception('No hay repositorios guardados.')
        ret=projects[0] if idRepositorio is not None else projects
        return ret
    
    @staticmethod
    def __checkArgsSacar(idRepositorio,moment):
        if idRepositorio is not None and not isinstance(idRepositorio,int):
            raise Exception('Tipos a extraer incorrectos')
        if moment is not None and idRepositorio is None:
            raise Exception('Tipos a extraer incorrectos')
        if moment is not None and not isinstance(moment,int):
            raise Exception('Tipos a extraer incorrectos')
    
    @staticmethod
    def dcd(arg):
        if isinstance(arg,bytearray):
            return arg.decode("utf-8")
        return arg
    @staticmethod
    def getCon():
        if not Almacen.con_cargada:
            parametros= open(Almacen.CON_PATH).read()
            parametros=parametros.split('\'')
            Almacen.conexion['host']=parametros[1]
            Almacen.conexion['user']=parametros[3]
            Almacen.conexion['passwd']=parametros[5]
            Almacen.conexion['db']=parametros[7]
            Almacen.conexion['port']=parametros[9]
            Almacen.con_cargada=True
        return mysql.connector.connect(host=Almacen.conexion['host'],port=Almacen.conexion['port'], user=Almacen.conexion['user'], passwd=Almacen.conexion['passwd'], db=Almacen.conexion['db'],auth_plugin='mysql_native_password')