#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Glowjobs - by Glowjobs
from flask import Flask, render_template, request, flash, redirect ,session
import random
import asyncio
from aiohttp import ClientSession

from tools.tools import *
app = Flask(__name__)


class webpage():
  run_crawler()
  async def fetch_data(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
  @app.route("/")
  def index():
    return render_template("index.html")
  @app.route("/offers")
  def offers():
    return render_template("offers.html")
  @app.route("/blog")
  def blog():
    return render_template("blog.html")
  @app.route("/launchapp",methods=['POST','GET'])
  def launchapp():
    randnum = random.randint(1, 5)
    if request.method == "POST":
      if request.form['submit_button'] == 'accept':
            pass 
      elif request.form['submit_button'] == 'reject':
            pass 
    return render_template("launchapp.html", randnum=randnum)
  @app.route("/conctact")
  def conctact():
    return render_template("conctact.html")
  @app.route("/get_premium")
  def get_premium():
    return render_template("get_premium.html")
 

if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  app.run(debug=True,host="127.0.0.1",port=5000)
