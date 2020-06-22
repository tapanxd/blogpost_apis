from flask import Flask
import json
import pandas as pd
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to task 1 API <br> Please enter the url as' \
           ' <br> <b>/`json_file_path`&&`db_path`&&`table_name`</b>' \
           '<br> to access the API'


@app.route('/<path:file_name>&&<path:db_name>&&<string:table_name>')
def to_sql(file_name, db_name, table_name):
    with open(file_name) as p:
        data = json.load(p)

    t = pd.DataFrame(data)

    conn = sqlite3.connect(db_name + '.db')
    c = conn.cursor()

    c.execute("""SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='""" + table_name + """'""")
    flag = c.fetchone()[0]
    if flag != 0:
        return 'Table ' + table_name + ' already exists!'
    else:
        t.to_sql(table_name, conn)
        conn.close()
        return 'Table ' + table_name + ' created'


app.run(port=8000)
