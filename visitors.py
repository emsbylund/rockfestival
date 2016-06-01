# *-* coding:utf-8 *-*

import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import MySQLdb
from socket import *
import datetime

db = None
cursor = None

def call_database():
    global db
    global cursor
    # connect
    db = MySQLdb.connect(host="195.178.232.16", port=3306, user="af6551", passwd="antonj123", db="af6551")
    # create a cursor
    cursor = db.cursor()
    return cursor

def close_database():
    global db
    db = db.close()


@route('/schedule')
def schedule():
    sql = "SELECT DATE_FORMAT(framtradande.starttid, '%T'), DATE_FORMAT(framtradande.sluttid, '%T'), band.namn as Band, scen.namn as Scen, DATE_FORMAT(framtradande.datum, '%y-%m-%d')\
                FROM framtradande\
                INNER JOIN band\
                ON band.BandID = framtradande.bandID\
                INNER JOIN scen\
                ON framtradande.scen = scen.namn;"
    cursor = call_database()
    cursor.execute(sql)
    show_schedule = cursor.fetchall()

    sql1 = "SELECT Namn, Musikstil, Ursprungsland\
    FROM band;"
    cursor.execute(sql1)
    show_band_info = cursor.fetchall()

    close_database()
    return template('visitor_schedule', schedule = show_schedule, band_info = show_band_info)

@route('/static/<filename>')
def server_static(filename):
    '''
    Hanterar routingen till static-filerna.
    Skickar tillbaka filen i static som efterfrågas i URL:en.
    '''
    return static_file(filename, root='static')

run(host='localhost', port=8000, debug=True, reloader=True)
