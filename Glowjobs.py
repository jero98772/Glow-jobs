#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Glowjobs - by Glowjobs
from flask import Flask, render_template, request, flash, redirect ,session
app = Flask(__name__)
class webpage():
  @app.route("/")
  def index():
    return render_template("index.html")
  @app.route("/offers")
  def offers():
    return render_template("offers.html")
  @app.route("/blog")
  def blog():
    return render_template("blog.html")
  @app.route("/launchapp")
  def launchapp():
    return render_template("launchapp.html")
  @app.route("/conctact")
  def conctact():
    return render_template("conctact.html")
  @app.route("/get_premium")
  def get_premium():
    return render_template("get_premium.html")

      

      

      

      
if __name__ == "__main__":
  app.run(debug=True,host="127.0.0.1",port=5000)
