# *-* coding:utf-8 *-*

import bottle
from bottle import route, get, post, run, template, error, static_file, request, redirect, abort, response, app
import MySQLdb
from socket import *
import datetime

#sock=socket()
#sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

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
    sql = "SELECT DATE_FORMAT(framtradande.starttid, '%h:%i'), DATE_FORMAT(framtradande.sluttid, '%h:%i'), band.namn as Band, scen.namn as Scen, DATE_FORMAT(framtradande.datum, '%y-%m-%d')\
                FROM framtradande\
                INNER JOIN band\
                ON band.BandID = framtradande.bandID\
                INNER JOIN scen\
                ON framtradande.scen = scen.namn;"
    cursor = call_database()
    cursor.execute(sql)
    show_schedule = cursor.fetchall()
    sql2 = "SELECT namn\
                FROM band"
    cursor.execute(sql2)
    list_of_bands = cursor.fetchall()
    sql3 = "SELECT namn\
                FROM scen"
    cursor.execute(sql3)
    stages = cursor.fetchall()
    close_database()
    return template('spelschema', schedule = show_schedule, list_of_bands = list_of_bands, stages = stages)

@route('/festival_workers')
def show_festival_workers():

    sql = "SELECT Festivaljobbare.Person_Nr, Festivaljobbare.Namn, Festivaljobbare.Telefon_Nr, Ansvarig_chef.Namn as Chef\
             FROM Festivaljobbare\
             INNER JOIN Ansvarig_Chef\
             ON Festivaljobbare.Ansvarig_Chef = Ansvarig_Chef.PersonNr;"
    cursor = call_database()
    cursor.execute(sql)
    show_festivaljobbare = cursor.fetchall()
   
    sql1 = "SELECT personNr\
                FROM Ansvarig_Chef"
    cursor.execute(sql1)
    show_ansvarigchef = cursor.fetchall()
    close_database()
    return template('festivaljobbare', festivaljobbare = show_festivaljobbare, chef = show_ansvarigchef)

@route('/add_new_worker/', method = "POST")
def get_festival_workers():
    global db
    namn = request.forms.get('name')
    telnr = request.forms.get('TelNr')
    bday = request.forms.get('bday')
    boss = request.forms.get('choose_chef')
    print boss
    

    cursor = call_database()
    sql = "INSERT INTO festivaljobbare values('%s', '%s', '%s', '%s')" % (bday, namn, telnr, boss)
    cursor.execute(sql)
    db.commit()
    print "det funkar"
    
    

@route('/static/<filename>')
def server_static(filename):
    '''
    Hanterar routingen till static-filerna.
    Skickar tillbaka filen i static som efterfrågas i URL:en.
    '''
    return static_file(filename, root='static')

@route('/add_new_performance', method="POST")
def add_new_performance():
    global db
    band = request.forms.get('choose_band')
    stage = request.forms.get('choose_stage')
    start_time = request.forms.get('add_start_time')
    finish_time = request.forms.get('add_finish_time')
    date = request.forms.get('date_for_show')

    sql = "SELECT BandID FROM Band WHERE Namn = '%s'" % (band)
    cursor = call_database()
    cursor.execute(sql)
    answer_from_db = cursor.fetchone()
    band_id = int(answer_from_db[0])

    sql1 = "INSERT INTO framtradande VALUES('%d', '%s', '%s', '%s', '%s');" % (band_id, start_time, date, finish_time, stage)
    cursor.execute(sql1)
    db.commit()
    print "Det funkade"
    close_database()

@route('/show_security')
def show_security():
    sql = "SELECT Sakerhetsansvarig.Scen, Sakerhetsansvarig.Startdatum, Sakerhetsansvarig.Starttid,\
    Sakerhetsansvarig.Slutdatum, Sakerhetsansvarig.Sluttid, Festivaljobbare.Namn, Sakerhetsansvarig.Festivaljobbare\
    FROM Sakerhetsansvarig\
    INNER JOIN Festivaljobbare\
    ON Sakerhetsansvarig.Festivaljobbare = Festivaljobbare.Person_Nr;"
    cursor = call_database()
    cursor.execute(sql)
    show_securityworker = cursor.fetchall()

    sql2 = "SELECT Festivaljobbare.Person_Nr\
                FROM Festivaljobbare"
    cursor.execute(sql2)
    list_of_workers = cursor.fetchall()

    sql1 = "SELECT namn\
                FROM scen"
    cursor.execute(sql1)
    stages = cursor.fetchall()
    close_database()
   
    return template('sakerhetsansvarig', securityworker = show_securityworker, list_of_workers = list_of_workers, stages = stages )

@route('/add_new_security',  method="POST")
def add_new_security():
    global db

    worker = request.forms.get('choose_worker')
    stage = request.forms.get('choose_stage')
    start_time = request.forms.get('add_start_time')
    finish_time = request.forms.get('add_finish_time')
    start_date = request.forms.get('start_date')
    end_date = request.forms.get('end_date')

    cursor = call_database()
    sql2 = "INSERT INTO Sakerhetsansvarig VALUES (%s, %s, %s, %s, %s, %s);" % (worker, stage, start_time, finish_time, start_date, end_date)
    cursor.execute(sql2)
    db.commit()
    print "Det funkade"
    close_database()
    

run(host='localhost', port=8000, debug=True, reloader=True)
