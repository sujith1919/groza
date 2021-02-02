#!/usr/bin/python
import psycopg2
from config import config
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version1 = cur.fetchone()
        print(db_version1)
        # display the PostgreSQL database server version
        cur.execute('SELECT * from LIFEBOAT')
        db_version2 = cur.fetchone()
        print(db_version2)
        #cur.fetchall()
     # close the communication with the PostgreSQL
        #cur.execute("INSERT INTO LIFEBOAT (flag,hostname, nagios_status, dr_hostname, host_type) VALUES ('0','st13p29im-lifeboat002.me.com','staging','mr21p30im-lifeboat002.me.com','lifeboat')" )
        #conn.commit()
        cur.execute("SELECT * FROM LIFEBOAT where hostname='st13p29im-lifeboat033.me.com'")
        cur.fetchall()
        if cur.rowcount == 1:
            cur.execute("UPDATE LIFEBOAT SET nagios_status=%s, kernel_version=%s where hostname='st13p29im-lifeboat033.me.com'"  ,('staging','4.1.12-124.14.2.el6uek'))
            conn.commit()
        else:
            print("insert")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
if __name__ == '__main__':
    connect()
