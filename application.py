from flask import Flask, render_template, request, url_for, redirect
import sys
import pymysql
import models
application = Flask(__name__)

@application.route("/")
def main():
    data=models.data_list
    return render_template("main.html", data=data)

@application.route("/result/1")
def result_post1():
    idx=models.idx1
    list=models.data_list
    return render_template("result.html", list=list, idx=idx)

@application.route("/result/2")
def result_post2():
    idx=models.idx2
    list=models.data_list
    return render_template("result2.html", list=list, idx=idx)

@application.route("/result/3")
def result_post3():
    idx=models.idx3
    list=models.data_list
    return render_template("result3.html", list=list, idx=idx)

@application.route("/result/4")
def result_post4():
    idx=models.idx4
    list=models.data_list
    return render_template("result4.html", list=list, idx=idx)

@application.route("/result/5")
def result_post5():
    idx=models.idx5
    list=models.data_list
    return render_template("result5.html", list=list, idx=idx)

@application.route("/result/6")
def result_post6():
    idx=models.idx6
    list=models.data_list
    return render_template("result6.html", list=list, idx=idx)

@application.route("/result/7")
def result_post7():
    idx=models.idx7
    list=models.data_list
    return render_template("result7.html", list=list, idx=idx)

@application.route("/result/8")
def result_post8():
    idx=models.idx8
    list=models.data_list
    return render_template("result8.html", list=list, idx=idx)

@application.route("/result/9")
def result_post9():
    idx=models.idx9
    list=models.data_list
    return render_template("result9.html", list=list, idx=idx)

@application.route("/result/10")
def result_post10():
    idx=models.idx10
    list=models.data_list
    return render_template("result10.html", list=list, idx=idx)

@application.route("/result/11")
def result_post11():
    idx=models.idx11
    list=models.data_list
    return render_template("result10.html", list=list, idx=idx)

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
