#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pandas as pd
import time
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

clicks = pd.read_csv('ids_clicks.csv')
keyword = pd.read_csv('wetwipes.csv')
keyword = keyword.drop(['author','comment_n','content','likes','title'],1)


k_clicks = clicks[clicks.board_id==keyword.loc[0,'board_id']]
for ids in keyword.loc[1:,'board_id']:
    k_clicks = k_clicks.append(clicks[clicks.board_id==ids])
k_time = k_clicks.sort_values(by='date')


k_time.to_csv('weiwipes_time.csv',index=False,encoding='utf-8')

