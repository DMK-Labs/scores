#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

key1 = pd.read_csv('key1_plot.csv')
key1['x'] = key1['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
key2 = pd.read_csv('key2_plot.csv')
key2['x'] = key2['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
key3 = pd.read_csv('key3_plot.csv')
key3['x'] = key3['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
key4 = pd.read_csv('key4_plot.csv')
key4['x'] = key4['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
key5 = pd.read_csv('key5_plot.csv')
key5['x'] = key5['x'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))

x1,y1 = key1.x,key1.scores
x2,y2 = key2.x,key2.scores
x3,y3 = key3.x,key3.scores
x4,y4 = key4.x,key4.scores
x5,y5 = key5.x,key5.scores

plt.plot(x1,y1,label='We make price')
plt.plot(x2,y2,label='11st')
plt.plot(x3,y3,label='G9')
plt.plot(x4,y4,label='Hotdeal')
plt.plot(x5,y5,label='money')

plt.title('scores by keywords')
plt.legend(loc='upper left')
plt.show()
