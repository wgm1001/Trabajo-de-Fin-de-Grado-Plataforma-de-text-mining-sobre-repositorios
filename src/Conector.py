# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno

Clase Conector
La clase conector está dedicada a crear un objeto gitlab
a partir de un link, lo cual hará a través de un método estático
"""
import gitlab
import os
class Conector:
    @staticmethod
    def conectar():
        HOST='http://gitlab.com/'
        TOKEN_PATH='..'+os.path.sep+'lib'+os.path.sep+'Token.txt'
        TOKEN= open(TOKEN_PATH).read()
        return gitlab.Gitlab(HOST, private_token=TOKEN)