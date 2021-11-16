from flask import Flask, g
from flask import render_template

import sqlite3

pap = Flask(__name__)


def db():
    sql = sqlite3.connect('db.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = db()
    return g.sqlite_db


@pap.route('/')
def index():
    import string
    import random

    special_chars = '!?-_@#:.,'
    printable_chars = string.ascii_letters + string.digits + special_chars
    nbr_chars = 12
    x = []
    for i in range(nbr_chars):
        x.append(random.choice(printable_chars))
    z = ''.join(x)

    db = get_db()
    db.execute('INSERT INTO counter VALUES (1)')
    db.commit()
    stats = db.execute('SELECT count FROM counter')
    results = stats.fetchone()
    r = stats.fetchall()
    final_result = len(r)

    return render_template('index.html', pwd=z, c=results, b=final_result)


if __name__ == '__main__':
    pap.run()



