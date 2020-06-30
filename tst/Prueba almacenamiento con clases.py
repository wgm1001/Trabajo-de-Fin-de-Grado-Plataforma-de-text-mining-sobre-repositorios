# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba sobre las clases de la fase de extracción
"""

from src import Extractor
from src import Almacen


extractor=Extractor.Extractor('foundrynet/dnd5e')
print('Creado extractor')
proyecto=extractor.extraer()
print('Extraido repostiorio')
Almacen.Almacen.guardar(proyecto)
print('Almacenado')
repositorios=Almacen.Almacen.sacarRepositorios()
for i in repositorios:
    print('id ',i.pid,' description ',i.description)
