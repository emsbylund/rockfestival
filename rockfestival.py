# *-* coding:utf-8 *-*

import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import MySQLdb

def call_database(sql, ask_database_to):
    # connect
    db = MySQLdb.connect(host="195.178.232.16", port=3306, user="af6551", passwd="antonj123", db="af6551")
    # create a cursor
    cursor = db.cursor()
    cursor_answer = []

    try:
        cursor.execute(sql)
        for query in ask_database_to:
            cursor_answer.append(eval('cursor.'+query))
        db.commit()

    except:
        db.rollback()

    db.close()
    return cursor_answer

@route('/')
def start_page():
    return template('rockfestival')

@route('/schedule')
def schedule():
    sql = "SELECT framtradande.starttid, framtradande.sluttid, band.namn as Band, scen.namn as Scen, framtradande.datum\
                FROM framtradande\
                INNER JOIN band\
                ON band.BandID = framtradande.bandID\
                INNER JOIN scen\
                ON framtradande.scen = scen.namn;"
    ask_database_to = ['fetchall()']
    answer_from_db = call_database(sql, ask_it_to)
    print answer_from_db[0]
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


run(host='localhost', port=8000, debug=True, reloader=True)
