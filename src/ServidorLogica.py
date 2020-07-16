# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Servidor Logica
Esta clase esta dedicada a llamar a las distintas funciones de las clases
para que el servidor no lo haga directamente
"""
from Extractor import Extractor
from Almacen import Almacen
class ServidorLogica:
    @staticmethod
    def extraer_rep(argumentos):
        url=argumentos['url']
        url=url.split('/')
        if url[2]!='gitlab.com':
            return 400
        url=url[3]+'/'+url[4]
        try:
            if 'token' in argumentos.keys():
                ext=Extractor(link=url,token=argumentos['token'])
            else:
                ext=Extractor(url)
            p=ext.extraer()
            Almacen.guardar(p)
            return 200
        except Exception as e:
            if str(e)=='Proyecto no encontrado':
                return 404
            if str(e)=='Permisos insuficientes':
                return 401
            raise
