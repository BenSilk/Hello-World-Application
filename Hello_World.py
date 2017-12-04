# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:20:20 2017

@author: Ben
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello World")
