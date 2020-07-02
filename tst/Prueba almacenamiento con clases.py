# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba sobre las clases de la fase de extracción
"""

from src import Extractor
from src import Almacen


#extractor=Extractor.Extractor('foundrynet/dnd5e')
#print('Creado extractor')
#proyecto=extractor.extraer()
#print('Extraido repostiorio')
#Almacen.Almacen.guardar(proyecto)
print('Almacenado')
coun=35
repositorios=Almacen.Almacen.sacarRepositorios()
for p in repositorios:
    print('id ',p.pid,' description ',p.description)
    for i in p.issues:
        if coun>0:
            print('iid ',i.iid,' labels ',i.labels, i.labels.__class__) 
            coun-=1