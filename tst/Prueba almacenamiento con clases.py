# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba sobre las clases de la fase de extracción
"""

from src import Extractor
from src import Almacen

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
    Almacen.Almacen.guardar(proyecto)
    p=Almacen.Almacen.sacarRepositorios(proyecto.pid)
    print('id ',p.pid,' description ',p.description)
    for i in p.issues:
            print('iid ',i.iid,' labels ',i.labels) 
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()