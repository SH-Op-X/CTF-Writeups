import sqlite3
from flask import Flask, request, redirect, render_template
import time
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        password = request.form['password']
        real = 'REDACTED'
        if len(password) != 7:
            return render_template('login.html', message="you need 7 chars")
        for i in range(len(password)):
            if password[i] != real[i]:
                message = "incorrect"
                return render_template('login.html', message=message)
            else:
                time.sleep(1)
        if password == real:
            message = "yayy! hi kirby"

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
