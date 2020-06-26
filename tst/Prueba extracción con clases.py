# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Prueba sobre las clases de la fase de extracción
"""

from src import Extractor

extractor=Extractor.Extractor('foundrynet/dnd5e')
proyecto=extractor.extraer()
print(proyecto.pid)
print(proyecto.name)
print(proyecto.description)
for i in proyecto.issues:
    print(i)