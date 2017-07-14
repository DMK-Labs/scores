#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

k_time = pd.read_csv('key1_time.csv')
k_time['datetime'] = k_time['datetime']/3600
k_id = pd.DataFrame({'board_id':list(set(k_time['board_id']))})


def coef(i,sample):
    a = (sample.iloc[i+1,1] - sample.iloc[i,1])/float((sample.iloc[i+1,3] - sample.iloc[i,3]))
    b = sample.iloc[i,1] - a*sample.iloc[i,3]
    return a, b

def line(i,x,sample):
    a,b = coef(i,sample)
    y = a*x + b
    return y

def estimate(board_id,x):
    # column numbers
    ## 0: board_id, 1: clicks/y, 2: date(y-m-d h:m:s), 3:datetime/x 
    sample = k_time[k_time.board_id==board_id]
    i = 0
    age = x
    if x < sample.iloc[0,3]:
        y = 0
    elif x >= sample.iloc[len(sample)-1,3]:
        y = sample.iloc[len(sample)-1,1]
        age -= sample.iloc[0,3]
    else:
        for j in range(len(sample)):
            if sample.iloc[j,3] <= x < sample.iloc[j+1,3]:
                i = j
                break
        y = line(i,x,sample)
        age -= sample.iloc[0,3]
    return y, age

def score(board_id, times, gravity=1.8):
    score = []
    for time in times:
        clicks,age = estimate(board_id,time)
        score.append(clicks / pow((age+2), gravity))
    return score


start = k_time.iloc[0,3]
end = k_time.iloc[-1,3]
quater = 0.25

times = np.arange(start,end+0.25,0.25)
to_time = lambda x: dt.datetime.fromtimestamp(x*3600)
x = np.array([to_time(x) for x in times])

scores = []

m=0
for board in k_id.iloc[:10,0]:
    scores.append(np.array(score(board,times)))
    print m
    m += 1
y = scores[0]
for score in scores[1:]:
    y += score

key = '위메프'
data = pd.DataFrame({'time_points':times,'scores':y,'x':x})
data['keyword'] = key
data.to_csv('key1_plot.csv',index=False,encoding='utf-8')
