# *-* coding:utf-8 *-*

import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import MySQLdb
from socket import *
import datetime

sock=socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

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
    sql = "SELECT TIME(framtradande.starttid), TIME(framtradande.sluttid), band.namn as Band, scen.namn as Scen, DATE(framtradande.datum)\
                FROM framtradande\
                INNER JOIN band\
                ON band.BandID = framtradande.bandID\
                INNER JOIN scen\
                ON framtradande.scen = scen.namn;"
    ask_database_to = ['fetchall()']
    answer_from_db = call_database(sql, ask_database_to)
    show_schedule = answer_from_db[0]
    #for performance in show_schedule:
        #print("{} spelar kl {} - {} den {} på scenen {}".format(performance[2], performance[0], performance[1], performance[4], performance[3]))
    return template('spelschema', schedule = show_schedule)

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
