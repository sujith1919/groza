from __future__ import print_function
from flask import Flask ,request, jsonify, render_template
import json
import sys
import psycopg2
from config import config
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('work.html')


@app.route('/names' ,methods=['GET', 'POST'])

def add_message():

# Get the post data from adminm host

    content = request.json

#Iterate through the JSON data

    for key in content:
        host_name = key
        dr_hostname = request.json[key]['DR-PARTNER']
        nagios = request.json[key]['HOST-NAGIOS']
        dr_nagios = request.json[key]['DR-NAGIOS']
        kernel_version = request.json[key]['KERNEL-VERSION']
        flag = request.json[key]['FLAG']
        hosttype = request.json[key]['HOST-TYPE']

        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a cursor
            cur = conn.cursor()
            # check if hostname exits in DB, upsert accordingly
            cur.execute("SELECT * FROM LIFEBOAT where hostname='%s'" % host_name)
            cur.fetchall()
            if cur.rowcount == 1:
                cur.execute("UPDATE LIFEBOAT SET nagios_status=%s, kernel_version=%s where hostname=%s"  ,(nagios,kernel_version,host_name))
                conn.commit()
            else:
                cur.execute('INSERT INTO LIFEBOAT (hostname, nagios_status, kernel_version,dr_hostname, flag,host_type) VALUES (%s,%s,%s,%s,%s,%s)', (host_name,nagios,kernel_version,dr_hostname,flag,hosttype))
                conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
         # close the communication with the PostgreSQL                
                print('Database connection closed.')
        #print('lol' , file=sys.stdout)

    return "success"