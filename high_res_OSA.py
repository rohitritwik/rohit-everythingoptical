# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\rmalik\.spyder2\.temp.py
"""
#print("hello Ritwik")
#print('which school do you go to?')
#input()
#print("oh thatts a nice school")

import requests
import numpy as np
m = requests.get('http://10.120.68.74/wanl/data/json')
measData = m.json()['data']
foo = m.json()['data']
measData = np.array(foo)
freq = measData[:,0]
freq = measData[:,0]/1e6
Pwr = measData[:,3]/1e3








