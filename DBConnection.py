# Connect to DB
import psycopg2
import json
import csv
from pprint import pprint
print('Connecting to postgreSQL')
def connect():
    conn = None
    try:
        conn = psycopg2.connect(host="0.pg-core-read.aws-prod.veritone.com",database="platform", user="postgres", password="postgres")
        # create a cursor
        
        # execute a statement
        #print('PostgreSQL database version:')
        #cur.execute('SELECT version()')
        
 
        # display the PostgreSQL database server version
        #db_version = cur.fetchone()
        #print(db_version)

        with open('config.json') as f:
            engines = json.load(f)
            pprint(engines)

        for engine in engines["engines"]:
            print(engine["id"])
            cur = conn.cursor()
            engine_sql_query = """SELECT * FROM job_new.task WHERE (created_date_time >= (extract(epoch FROM now()) - 60*60*5)::INT AND 
                        created_date_time <= extract(epoch FROM now())::INT) AND (engine_id =%s) 
                        AND task_status='failed' ORDER BY created_date_time DESC LIMIT 5000"""
            cur.execute(engine_sql_query, (engine["id"],))
            print("Getting data...")
            record = cur.fetchone()
            pprint(record)
            
            
            

            

        
        
       
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
if __name__ == '__main__':
    connect()