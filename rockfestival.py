# *-* coding:utf-8 *-*

import bottle

@route('/schedule')
def schedule():
    return template('spelschema')

@route('/festival_workers')
def show_festival_workers():
    return template('festivaljobbare')
