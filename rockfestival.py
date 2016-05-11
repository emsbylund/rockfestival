# *-* coding:utf-8 *-*

import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app

@route('/')
def start_page():
    return template('rockfestival')

@route('/schedule')
def schedule():
    return template('spelschema')

@route('/festival_workers')
def show_festival_workers():
    return template('festivaljobbare')

@route('/static/<filename>')
def server_static(filename):
    '''
    Hanterar routingen till static-filerna.
    Skickar tillbaka filen i static som efterfrågas i URL:en.
    '''
    return static_file(filename, root='static')


run(host='localhost', port=8080, debug=True, reloader=True)
