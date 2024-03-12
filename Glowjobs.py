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
      
if __name__ == "__main__":
  app.run(debug=True,host="127.0.0.1",port=5000)
