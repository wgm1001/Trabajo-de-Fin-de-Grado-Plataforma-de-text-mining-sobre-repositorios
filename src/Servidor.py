# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Servidor
Clase encargada de la comunicación con el cliente y comunicarla con las distintas partes del programa
"""
from flask import Flask, render_template, redirect, url_for, flash
from formularios.FormularioExtraccion import FormularioExtraccion
from formularios.FormularioPrediccion import FormularioPrediccion
from flask import request
from ServidorLogica import ServidorLogica

app= Flask(__name__)
app.secret_key='palabra'
@app.route('/')
def main():
    return render_template('mainPage.html')

@app.route('/Extraer/',methods=['GET','POST'])
def extraer():
    formulario=FormularioExtraccion(request.form)
    if request.method =='POST' and formulario.validate():
        argumentos={'url':formulario.url.data}
        token=formulario.token.data.strip()
        if token != '':
            argumentos['token']=token
        resp=ServidorLogica.extraer_rep(argumentos)
        if resp==200:
            return redirect(url_for('extraccionCorrecta'))
        return redirect(url_for('errorExtraccion',error=resp))
    return render_template('extraer.html',formulario=formulario)

@app.route('/Extraer/error/<error>')
def errorExtraccion(error=None):
    return render_template('errorExtraccion.html', error=error)

@app.route('/Extraer/correcta')
def extraccionCorrecta():
    return render_template('extraccionCorrecta.html')

@app.route('/Predecir')
def predecir():
    formulario=FormularioPrediccion(request.form)


@app.errorhandler(404)
def enlaceRoto(e):
    return render_template('enlaceRoto.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',threaded=True)
    