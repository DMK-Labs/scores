#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

key = pd.read_csv('key1_plot.csv')
key['x'] = key['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))

x,y = key.x,key.scores
plt.plot(x,y,label='Example')
plt.legend(loc='upper left')
plt.show()

'''
#board = '71eb7ac2643d41059232b3a7eb29c108'
y = score(board,times)
plt.plot(times,y,'b',times,y,'bo')
plt.show()
'''
