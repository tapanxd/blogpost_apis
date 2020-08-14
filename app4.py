from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to task 4 API'


@app.route('/create_chart/likes/<path:db_name>&&<string:table_name>&&<int:post_id>&&<string:date_one>&&<string'
           ':date_two>')
def create_chart(db_name, table_name, post_id, date_one, date_two):
    conn = sqlite3.connect(db_name + '.db')
    c = conn.cursor()

    c.execute("""SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='""" + table_name + """'""")
    flag = c.fetchone()[0]
    if flag == 0:
        return 'Table ' + table_name + ' does not exist!'

    else:
        # collect the timestamps of a post's each like
        q3 = """SELECT datePublished FROM likes where postId = """ + str(post_id) + """ AND datePublished BETWEEN """ \
                                                                               """(SELECT (strftime('%s','""" + date_one + """')*1000)) AND """ \
                                                                               """(SELECT (strftime('%s','""" + date_two + """')*1000))"""

        c.execute(q3)
        # make a list
        d = list(c)
        # convert each value in list from tuple to string and strip off the unwanted brackets and commas
        p = []
        r = []
        u = []
        v = []
        k = []
        l = []

        for i in d:
            p.append(str(i))

        for i in p:
            v.append(i.rstrip(',)').lstrip('('))
        v.sort()
        # print(v)
        # collect the count of likes from each timestamp for a particular post
        t = []
        for i in v:
            q4 = """SELECT COUNT(*) FROM likes WHERE datePublished <=""" + i + """ AND postID = """ + post_id
            c.execute(q4)
            t.append(list(c))

        # convert cursor object to int in the list
        for i in t:
            l.append(i[0])
        for i in l:
            k.append(str(i))
        for i in k:
            r.append(i.rstrip(',)').lstrip('('))
        for i in r:
            u.append(int(i))

        return render_template('chart.html', labels=v, values=u)


app.run(port=2401)
