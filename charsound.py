# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:22:26 2016

@author: erik.lundin
"""

import time

while True:
    txt = input("which sound?")
    if txt is "9":
        #play sound
        print("playing sound 9")
    else:
        break
    
    import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []
