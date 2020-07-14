# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba sobre las clases de la fase de extracción
"""

from src import Extractor
def ext_bad_rep():
    '''
    Intenamos sacar un proyecto erróneo
    
    >>> ext_bad_rep()
    Detecta el fallo
    
    '''
    try:
        Extractor.Extractor('wgm1001/mal_puesto_TFG-tst')
    except Exception as e:
        if str(e)=='Proyecto no encontrado':
            print('Detecta el fallo')
        else:
            raise
def ext_proj_sin_permiso():
    '''
    Intentamos extraer repositorio con un token inválido
    
    >>> ext_proj_sin_permiso()
    Detecta el fallo
    
    '''
    try:
        Extractor.Extractor('wgm1001/mal_puesto_TFG-tst',token='Invalido')
    except Exception as e:
        if str(e)=='Permisos insuficientes':
            print('Detecta el fallo')
        else:
            raise
    
def ext_pid():
    '''
    Extraemos la id del proyecto
    
    >>> ext_pid()
    19766159
    
    '''
    proyecto=get_pro()
    print(proyecto.pid) #pid 19766159
    
def ext_name():
    '''
    Extraemos el nombre del proyecto
    
    >>> ext_name()
    Proyecto de prueba del TFG
    
    '''
    proyecto=get_pro()
    print(proyecto.name) #Proyecto de prueba del TFG
    
def ext_desc():
    '''
    Extraemos la descripción y comprobamos su veracidad
    
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
    Sacamos los comentarios de las issues

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