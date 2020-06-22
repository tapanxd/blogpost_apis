from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to task 2 API <br> Please enter the url as ' \
           '<br> <b>/`db_path`&&`table_name`&&`field_to_sort_by`</b>' \
           '<br> to access the API'


@app.route('/<path:db_name>&&<string:table_name>&&<string:sort_by>')
def sort_authors(db_name, table_name, sort_by):
    conn = sqlite3.connect(db_name + '.db')
    c = conn.cursor()

    c.execute("""SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='""" + table_name + """'""")
    flag = c.fetchone()[0]
    if flag == 0:
        return 'Table ' + table_name + ' does not exist!'
    else:
        q1 = """SELECT firstName,lastName from """ + table_name + """ ORDER BY """ + sort_by + """ ASC"""
        c.execute(q1)
        d = c.fetchall()

        return render_template('print1.html', items=d)


app.run(port=9531)
