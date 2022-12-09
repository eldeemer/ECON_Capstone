#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 2
@author: sining/ethan

This script is designed to read in a "json-like" csv file as a pandas dataframe
The workflow:
    for each record, 
    1. first convert it into json strings, 
    2. and then reload it as python a dictionary,
    3. get the essential data part from this dict, convert to df
    4. concat the rows together

the tqdm module is just for progressing tracking. not essential.
Happy coding!
"""

import pandas as pd
import json
from tqdm import tqdm

data = pd.read_csv('C:/Users/eldee/Documents/Data/subreddits.csv')

result = pd.DataFrame()
for i in tqdm(data.index):
    row = data.loc[i]
    row = row.loc['SRC']
    j_string = data.to_json(orient='split')
    dict_file = json.loads(j_string)
    core_data = dict_file['data']
    sub_result = pd.DataFrame()
    for j in (core_data):
        d = json.loads(j[0])
        df = pd.json_normalize(d)
        sub_result = pd.concat([sub_result, df], axis=0)
    result = pd.concat([result, sub_result], axis=0)

result.to_csv("subreddit_df.csv")