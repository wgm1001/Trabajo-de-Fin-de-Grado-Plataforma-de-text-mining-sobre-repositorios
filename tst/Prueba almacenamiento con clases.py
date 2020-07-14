# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba sobre las clases de la fase de extracción
"""
from datetime import datetime
from src import Extractor
from src.Almacen import Almacen

def prueba_almacenamiento():
    '''
    >>> prueba_almacenamiento()
    id  19766159  description  Proyecto de prueba del TFG para la extracción de issues.
    iid  1  labels  ['learn']
    iid  2  labels  ['enhancement']
    iid  3  labels  ['learn']
    iid  4  labels  ['critical', 'enhancement']
    iid  5  labels  ['learn']
    iid  6  labels  ['enhancement']
    
    '''
    extractor=Extractor.Extractor('wgm1001/TFG-tst')
    proyecto=extractor.extraer()
    Almacen.guardar(proyecto)
    p=Almacen.sacarRepositorios(proyecto.pid)
    print('id ',p.pid,' description ',p.description)
    for i in p.issues:
            print('iid ',i.iid,' labels ',i.labels) 
def prueba_guardar_mal():
    '''
    Intentaremos guardar algo incorrecto
    
    >>> prueba_guardar_mal()
    Detecta el fallo
    
    '''
    try:
        Almacen.guardar('Invalido')
    except Exception as e:
        if str(e)=='Tipo a guardar incorrecto':
            print('Detecta el fallo')
        else:
            raise
    
def prueba_recuperacion_erronea():
    '''
    Trataremos de extraer un repositorio erroneo
    
    >>> prueba_recuperacion_erronea()
    Detecta el primer fallo
    Detecta el segundo fallo
    Detecta el tercer fallo
    Detecta el último fallo
    
    '''
    try:
        Almacen.sacarRepositorios(-245)
    except Exception as e:
        if str(e)=='Id de repositorio no encontrado.':
            print('Detecta el primer fallo')
        else:
            raise
    try:
        Almacen.sacarRepositorios('Invalido')
    except Exception as e:
        if str(e)=='Tipos a extraer incorrectos':
            print('Detecta el segundo fallo')
        else:
            raise
    try:
        Almacen.sacarRepositorios(moment=datetime.now())
    except Exception as e:
        if str(e)=='Tipos a extraer incorrectos':
            print('Detecta el tercer fallo')
        else:
            raise
    try:
        Almacen.sacarRepositorios(idRepositorio=5,moment='Invalido')
    except Exception as e:
        if str(e)=='Tipos a extraer incorrectos':
            print('Detecta el último fallo')
        else:
            raise
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()