# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:48:37 2017

@author: Ben
"""
import pytest
from Hello_World import hello

def test_hello():
    assert hello()=="Hello World"