#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

key1 = pd.read_csv('bosomi_plot.csv')
key1['x'] = key1['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
key2 = pd.read_csv('brabar_plot.csv')
key2['x'] = key2['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
key3 = pd.read_csv('crox_plot.csv')
key3['x'] = key3['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
key4 = pd.read_csv('iphone_plot.csv')
key4['x'] = key4['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
key5 = pd.read_csv('wetwipes_plot.csv')
key5['x'] = key5['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))

x1,y1 = key1.x,key1.scores
x2,y2 = key2.x,key2.scores
x3,y3 = key3.x,key3.scores
x4,y4 = key4.x,key4.scores
x5,y5 = key5.x,key5.scores

plt.plot(x1,y1,label='Bosom')
plt.plot(x2,y2,label='Brabar')
plt.plot(x3,y3,label='Crox')
plt.plot(x4,y4,label='Iphone')
plt.plot(x5,y5,label='Wet Wipe')

plt.title('scores by keywords')
plt.legend(loc='upper left')
plt.show()
