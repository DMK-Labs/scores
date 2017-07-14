#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

k_time = pd.read_csv('iphone_time.csv')
k_time['datetime'] = k_time['datetime']/3600
k_id = set(k_time['board_id'])

start = k_time.iloc[0,3]
end = k_time.iloc[-1,3]
times = np.arange(start,end+0.25,0.25)
to_time = lambda x: dt.datetime.fromtimestamp(x)
x = np.array(map(to_time,times*3600))

def line(i,x,sample):
    a = (sample.iloc[i+1,1] - sample.iloc[i,1])/float((sample.iloc[i+1,3] - sample.iloc[i,3]))
    b = sample.iloc[i,1] - a*sample.iloc[i,3]
    y = a*x + b
    return y

def estimate(board_id,x):
    # column numbers
    ## 0: board_id, 1: clicks/y, 2: date(y-m-d h:m:s), 3:datetime/x 
    sample = k_time[k_time.board_id==board_id]
    age = 0
    if x < sample.iloc[0,3]:
        y = 0
    elif x >= sample.iloc[-1,3]:
        y = sample.iloc[-1,1]
        age = x - sample.iloc[0,3]
    else:
        i = filter(lambda j: sample.iloc[j,3] <= x and sample.iloc[j+1,3] > x,
                   range(len(sample)))
        y = line(i[0],x,sample)
        age = x - sample.iloc[0,3]
    return y, age

def score(board_id, time, gravity=1.8):
    clicks,age = estimate(board_id,time)
    return clicks / pow((age+2), gravity)


scores = []
m=0
for board in k_id:
    board_score = np.array(map(lambda z: score(board,z),times))
    scores.append(board_score)
    print m
    m += 1
y = sum(scores)

key = '아이폰'
data = pd.DataFrame({'time_points':times,'scores':y,'x':x})
data['keyword'] = key
data.to_csv('iphone_plot.csv',index=False,encoding='utf-8')





