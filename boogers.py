#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 18:01:03 2023

@author: jeanneliu
"""
import pandas as pd
import numpy as np

COLUMN_SPECS = [(0, 1), (1, 10), (10, 40), (40, 97)]
COLUMN_NAMES = ['RecordID', 'SHORT_EIN', 'SHORT_CPNY_NAME', 'Other']
OUTPUT_COLUMN_WIDTH = 96
output_file_path = 'Output/merged.txt'

mt_df = pd.read_csv("Input/jeanne_test_tabdelim.TXT", sep="\t", converters={"FEIN": str})

nhr_df = pd.read_fwf('Input/UKGInc_MA.txt', colspecs=COLUMN_SPECS, header=None,
                          names=COLUMN_NAMES)

mt_df["SHORT_EIN"] = mt_df["EIN"].str.replace('[^a-zA-Z0-9]', '', regex=True).str[0:9]
    # mt_df["SHORT_EIN"] = mt_df["EIN"].str[0:9]
mt_df["SHORT_NAME"] = mt_df["CPNY_NAME"].str[0:30]



def match_thing(row):
    SHORT_NAME=2
    RECORD=0
    SHORT_EIN=1
    
    if row[RECORD] == 'A':
       series=mt_df[(mt_df['SHORT_NAME'] == row[SHORT_NAME]) & (mt_df['SHORT_EIN'] == row[SHORT_EIN])]['FEIN']
       try:
           FEIN = series.iloc[0]
       except:
           FEIN=''
       if not FEIN == '':
           print('FEIN: {}, EIN: {}, Name: {} '.format(FEIN, row[SHORT_EIN], row[SHORT_NAME]))
        
       #print('name: {}, record: {}, EIN: {}'.format(row[SHORT_NAME], row[RECORD], row[SHORT_EIN]))
  # matching_row = mt_df['SHORT_NAME'] == name 
  #  try:
  #      print('{}'.format(matching_row))
  #  except:
  #      next
nhr_df.apply(match_thing, axis=1)


