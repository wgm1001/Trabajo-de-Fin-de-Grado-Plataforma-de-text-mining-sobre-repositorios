# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba sobre las clases de la fase de extracción
"""

from src import Extractor

def ext_pid():
    '''
    Intentamos extraer la id del proyecto
    
    >>> ext_pid()
    19766159
    
    '''
    proyecto=get_pro()
    print(proyecto.pid) #pid 19766159
    
def ext_name():
    '''
    Intentamos extraer el nombre del proyecto
    
    >>> ext_name()
    Proyecto de prueba del TFG
    
    '''
    proyecto=get_pro()
    print(proyecto.name) #Proyecto de prueba del TFG
    
def ext_desc():
    '''
    Intentamos extraer la descripción
    
    >>> ext_desc()
    Proyecto de prueba del TFG para la extracción de issues.
    
    '''
    proyecto=get_pro()
    print(proyecto.description) #Proyecto de prueba del TFG para la extracción de issues.
    
def num_issues():
    '''
    Extraemos el número de issues
    
    >>> num_issues()
    6
    
    '''
    proyecto=get_pro()
    count=0
    for i in proyecto.issues:
        count+=1
    print(count)
    
def ext_com():
    '''
    Intentamos Sacar los comentarios de las issues

    >>> ext_com()
    ['Lo que planteaba como modelo es el Esquema']
    ['closed']
    ['closed']
    ['closed']
    ['closed']
    ['closed', 'por probar', 'Con esto probaremos que se descarga los comentarios']
    '''
    proyecto=get_pro()
    for i in proyecto.issues:
        print(i.notes)

def get_pro():
    extractor=Extractor.Extractor('wgm1001/TFG-tst') 
    return extractor.extraer()

if __name__ == "__main__":
    import doctest
    doctest.testmod()