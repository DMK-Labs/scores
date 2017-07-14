#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import time
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np


board = pd.read_csv('crawl_board_new.csv')
zero = pd.DataFrame(board,columns=['board_id','registered_date'])
zero['clicks'] = 0
zero['date'] = zero['registered_date'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
zero['datetime'] = zero['date'].map(lambda x: time.mktime(x.timetuple()))
zero = zero.drop(['registered_date'],1)
clicks = pd.read_csv('crawl_board__clicks_new.csv')
clicks['date'] = clicks['date'].map(lambda x: dt.datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))
clicks['datetime'] = clicks['date'].map(lambda x: time.mktime(x.timetuple()))
clicks = clicks.drop(['bf_clicks','comment_count','bf_comment_count','likes', 'bf_likes',
                      'bf_date','crawl_interval'],1)
ids_clicks = pd.DataFrame()
for ids in zero.board_id:
    temp = zero[zero.board_id==ids]
    temp = temp.append(clicks[clicks.board_id==ids])
    ids_clicks = ids_clicks.append(temp)

ids_clicks.to_csv('ids_clicks.csv',index=False,encoding='utf-8')
