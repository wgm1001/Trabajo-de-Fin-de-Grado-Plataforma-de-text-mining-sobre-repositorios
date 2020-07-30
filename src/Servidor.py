# -*- coding: utf-8 -*-
"""
@author: Willow Maui García Moreno
Clase Servidor
Clase encargada de la comunicación con el cliente y comunicarla con las distintas partes del programa
"""
from flask import Flask, render_template, redirect, url_for,session
from formularios.FormularioExtraccion import FormularioExtraccion
from formularios.FormularioPrediccion import FormularioPrediccion
from formularios.FormularioIssue import FormularioIssue
from formularios.FormularioModelo import FormularioModelo
from flask import request
from ServidorLogica import ServidorLogica

app= Flask(__name__)
app.secret_key='palabra'

@app.route('/')
def main():
    session['pred']=None
    if 'id' not in session.keys():
        session['id']=ServidorLogica.getId()
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
        return redirect(url_for('error_c',error_c=resp))
    return render_template('extraer.html',formulario=formulario)

@app.route('/error/<error_c>')
def error_c(error_c=None):
    return render_template('error_c.html', error_c=error_c)

@app.route('/Extraer/correcta')
def extraccionCorrecta():
    return render_template('extraccionCorrecta.html')

@app.route('/Predecir/',methods=['GET','POST'])
def predecir():
    formulario=FormularioPrediccion(request.form) 
    if request.method =='POST':
        ServidorLogica.crearModelo(session['id'],formulario.modelo.data.strip())
        resp=ServidorLogica.entrenarModelo(session['id'],repositorios=formulario.repositorios.data,stopW=formulario.stopWords.data,idioma=formulario.idioma.data,comentarios=formulario.comentarios.data,metodo=formulario.metodo.data,sinEtiqueta=formulario.sinEtiqueta.data)
        session['modelo']=[formulario.repositorios.data,formulario.stopWords.data,formulario.idioma.data,formulario.comentarios.data,formulario.metodo.data,formulario.sinEtiqueta.data]
        if resp != 200:
            return redirect(url_for('error_c',error_c=resp))
        return redirect(url_for('predIssue',com=formulario.comentarios.data))
    return render_template('predecir.html',formulario=formulario)
        
@app.route('/Predecir/issue/<com>',methods=['GET','POST'])
def predIssue(com):
    formulario=FormularioIssue(request.form)
    session['pred']=None
    if request.method =='POST' and formulario.validate():
        issue_text=formulario.titulo.data+' '+formulario.descripcion.data+' '+formulario.estado.data
        if com == 'True':
            issue_text+=' '+formulario.comentarios.data
        issue_text=[issue_text]
        session['pred']=ServidorLogica.predIssue(session['id'],issue_text=issue_text)
    pred=session['pred']
    return render_template('issues.html',formulario=formulario, pred=pred,com=com)

@app.route('/Predecir/cargar',methods=['GET','POST'])
def recuperarModelo():
    formulario=FormularioModelo(request.form) 
    if request.method =='POST':
        mod=ServidorLogica.sacarModelo(session['id'],formulario.modelos.data)
        session['modelo']=[mod.repositorios,mod.stopW,mod.idioma,mod.comentarios,mod.metodo,mod.sinEtiqueta]
        return redirect(url_for('predIssue',com=mod.comentarios))
    return render_template('recuperarModelo.html',formulario=formulario)

@app.errorhandler(404)
def enlaceRoto(e):
    return render_template('enlaceRoto.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',threaded=True)
    