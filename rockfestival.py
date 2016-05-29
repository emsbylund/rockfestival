# *-* coding:utf-8 *-*

import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import MySQLdb
from socket import *
import datetime

sock=socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

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
    cursor = call_database()
    cursor.execute(sql)
    answer_from_db = cursor.fetchall()

    # ÄNDRA TIME TILL DATETIME I DATABASEN ISTÄLLET!

    #for every in answer_from_db:
        #every[0][0] = (datetime.datetime.min + every[0]).time()
    show_schedule = answer_from_db[0]
    print answer_from_db
    sql2 = "SELECT namn\
                FROM band"
    cursor.execute(sql2)
    answer_from_db2 = cursor.fetchall()
    list_of_bands = answer_from_db2[0]
    sql3 = "SELECT namn\
                FROM scen"
    cursor.execute(sql3)
    answer_from_db3 = cursor.fetchall()
    stages = answer_from_db3[0]
    close_database()
    #return template('spelschema', schedule = show_schedule, list_of_bands = list_of_bands, stages = stages)

@route('/festival_workers')
def show_festival_workers():

    namn = request.forms.get('name')
    telnr = request.forms.get('TelNr')
    bday = request.forms.get('bday')
    boss = request.forms.get('choose_chef')

    print boss


    #sql2 = "INSERT\
                #INTO festivaljobbare(Namn, Person_nr, Telefon_nr, Ansvarig_chef)\
                #VALUES('%s', '%d', '%d', '%s', '%d')" % (namn, telnr, bday, )
    #ask_database_to2 = []
    #return template('festivaljobbare', festivaljobbare = show_festivaljobbare, chef = show_ansvarigchef)

    return template('festivaljobbare')

@route('/static/<filename>')
def server_static(filename):
    '''
    Hanterar routingen till static-filerna.
    Skickar tillbaka filen i static som efterfrågas i URL:en.
    '''
    return static_file(filename, root='static')

@route('/add_new_performance', method="POST")
def add_new_performance():
    band = request.forms.get('choose_band')
    stage = request.forms.get('choose_stage')
    start_time = request.forms.get('add_start_time')
    finish_time = request.forms.get('add_finish_time')
    date = request.forms.get('date_for_show')

    sql = "SELECT BandID FROM Band WHERE Namn = '%s'" % (band)
    cursor = call_database()
    cursor.execute(sql)
    answer_from_database = cursor.fetchall()
    #ask_database_to = ['fetchall()']
    #answer_from_database = call_database(sql, ask_database_to)
    band_id = answer_from_database[0][0][0]

    sql1 = "INSERT INTO framtradande(BandID, Starttid, Datum, Sluttid, Scen)\
            #VALUES('%d', '%s', '%s', '%s', '%s')" % (band_id, start_time, date, finish_time, stage)
    cursor.execute(sql1)
    #ask_database_to1 = []
    #answer_from_database1 = call_database(sql, ask_database_to)
    print "Tjoho"

run(host='localhost', port=8000, debug=True, reloader=True)
