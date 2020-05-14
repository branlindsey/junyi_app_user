import numpy as np
import pandas as pd




def drop_columns(df):
    drop_cols = ['exercise', 'problem_type', 'problem_number', 'time_taken_attempts', 'hint_time_taken_list']
    df.drop(columns=drop_cols, inplace=True)
    return df 

def change_bool(df):
    bool_cols = ['topic_mode', 'suggested', 'review_mode','correct', 'hint_used','earned_proficiency']
    for col in bool_cols:
        df[col] = df[col].astype(int)
    return df
    

def convert_dates(df, df_time_col):
    df['time_done'] = pd.to_datetime(df['time_done'],unit='us')
    
def select_dat, df_time_col, date1, date2):
    df = (df[(df[df_time_col]>=date1)& (df[df_time_col]<=date2)])
    return df 