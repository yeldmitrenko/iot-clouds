from flask import Flask, render_template, request

import logging
import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
PASSWORD = "0000"


@app.route('/')
def hello_world():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("fpassword")
        if password == PASSWORD:
            app.logger.info("User logged successfully")
            return render_template('login_success.html', utc_dt=datetime.datetime.utcnow())
        else:
            app.logger.error("Failed to log in")
            return render_template('login_fail.html', utc_dt=datetime.datetime.utcnow())
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
