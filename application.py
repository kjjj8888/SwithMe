from flask import Flask, render_template
import sys
import models
import pymysql
application = Flask(__name__)


@application.route("/")
def index():
    a = models.test()
    return render_template("result.html", a=a)


@application.route("/result/")
def result():
     return render_template("hello.html")


if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
