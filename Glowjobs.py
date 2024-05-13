#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Glowjobs - by Glowjobs
from flask import Flask, render_template, request, flash, redirect ,session
import random
import asyncio
from aiohttp import ClientSession

from tools.tools import *
app = Flask(__name__)

class counter():
    _instances = {}
    def __new__(cls, maxvalue):
        if maxvalue not in cls._instances:
            cls._instances[maxvalue] = super().__new__(cls)
        return cls._instances[maxvalue]

    def __init__(self, maxvalue):
        # Initialize only if the instance is newly created
        if not hasattr(self, 'initialized'):
            self.start = maxvalue
            self.maxvalue = maxvalue
            self.initialized = True
            self.rnd = random.randint(1, maxvalue)
    def rnd_value(self):
      return (self.rnd*self.start)%self.maxvalue
    def decrement(self,value=1):
      self.start-=value

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
    c=counter(5)
    if request.method == "POST":
      if request.form['submit_button'] == 'accept':
            pass 
      elif request.form['submit_button'] == 'reject':
            pass 
    c.decrement()
    return render_template("launchapp.html", randnum=c.rnd_value())
  @app.route("/conctact")
  def conctact():
    return render_template("conctact.html")
  @app.route("/get_premium")
  def get_premium():
    return render_template("get_premium.html")
 

if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  app.run(debug=True,host="127.0.0.1",port=5000)
