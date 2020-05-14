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
    
def select_date(df, df_time_col, date1, date2):
    df = (df[(df[df_time_col]>=date1)& (df[df_time_col]<=date2)])
    return df 

def create_target(filepath, start, end, user_table):
    target_data = pd.read_pickle('../junyi_df.pickle')
    convert_dates(target_data, 'time_done')
    target_data = select_dates(target_data, 'time_done', start, end)
    
    target = dict()
    for user in list(user_table.index):
        if user in set(target_data['user_id']):
            target[user] = 1
        else: 
            target[user] = 0

    return target