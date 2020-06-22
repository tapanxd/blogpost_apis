from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to task 3 API <br> Please enter the url as ' \
           '<br> <b>/`db_path`&&`table_name`&&`field_to_sort_by`</b>' \
           '<br> to access the API'


@app.route('/<path:db_name>&&<string:table_name>&&<string:sort_by>')
def sort_posts(db_name, table_name, sort_by):
    conn = sqlite3.connect(db_name + '.db')
    c = conn.cursor()

    c.execute("""SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='""" + table_name + """'""")
    flag = c.fetchone()[0]
    if flag == 0:
        return 'Table ' + table_name + ' does not exist!'
    else:
        q1 = """SELECT title from """ + table_name + """ ORDER BY """ + sort_by + """ DESC"""
        c.execute(q1)
        p = c.fetchall()
        conn.close()
        return render_template('print1.html', items=p)


@app.route('/filter/<path:db_name>&&<string:table_name>&&<string:filter_by>')
def filter_posts(db_name, table_name, filter_by):
    conn = sqlite3.connect(db_name + '.db')
    c = conn.cursor()

    c.execute("""SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='""" + table_name + """'""")
    flag = c.fetchone()[0]
    if flag == 0:
        return 'Table ' + table_name + ' does not exist!'

    elif filter_by == '12hour' or filter_by == '12hours':
        q2 = """SELECT title FROM """ + table_name + """ WHERE datePublished >= """ \
                                                     """(SELECT (strftime('%s','now','-12 hour')*1000));"""
        c.execute(q2)
        p = c.fetchall()
        conn.close()
        return render_template('print1.html', items=p)

    elif filter_by == '1day':
        q2 = """SELECT title FROM """ + table_name + """ WHERE datePublished >= """ \
                                                     """(SELECT (strftime('%s','now','-1 day')*1000));"""
        c.execute(q2)
        p = c.fetchall()
        conn.close()
        return render_template('print1.html', items=p)

    elif filter_by == '3day' or filter_by == '3days':
        q2 = """SELECT title FROM """ + table_name + """ WHERE datePublished >= """ \
                                                     """(SELECT (strftime('%s','now','-3 day')*1000));"""
        c.execute(q2)
        p = c.fetchall()
        conn.close()
        return render_template('print1.html', items=p)

    elif filter_by == '1week' or filter_by == '7days' or filter_by == '7day':
        q2 = """SELECT title FROM """ + table_name + """ WHERE datePublished >= """ \
                                                     """(SELECT (strftime('%s','now','-7 day')*1000));"""
        c.execute(q2)
        p = c.fetchall()
        conn.close()
        return render_template('print1.html', items=p)

    elif filter_by == '1month':
        q2 = """SELECT title FROM """ + table_name + """ WHERE datePublished >= """ \
                                                     """(SELECT (strftime('%s','now','-1 month')*1000));"""
        c.execute(q2)
        p = c.fetchall()
        conn.close()
        return render_template('print1.html', items=p)


@app.route('/filter/<path:db_name>&&<string:table_name>&&<string:date_one>&&<string:date_two>')
def filter_posts_by_date(db_name, table_name, date_one, date_two):
    conn = sqlite3.connect(db_name + '.db')
    c = conn.cursor()

    c.execute("""SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='""" + table_name + """'""")
    flag = c.fetchone()[0]
    if flag == 0:
        return 'Table ' + table_name + ' does not exist!'
    else:
        q3 = """SELECT title FROM """ + table_name + """ WHERE datePublished BETWEEN """ \
            """(SELECT (strftime('%s','""" + date_one + """')*1000)) AND """ \
            """(SELECT (strftime('%s','""" + date_two + """')*1000))"""
        c.execute(q3)
        p = c.fetchall()
        conn.close()
        return render_template('print1.html', items=p)


app.run(port=6137)
