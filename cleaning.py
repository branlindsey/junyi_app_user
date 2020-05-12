import numpy as np
import pandas as pd

drop_cols = ['exercise', 'problem_type', 'problem_number', 'time_taken_attempts', 'hint_time_taken_list']

bool_cols = ['topic_mode', 'suggested', 'review_mode','correct', 'hint_used','earned_proficiency']


def drop_columms(df, drop_list)
    df.drop(columns=drop_list, inplace=True)
    return df 
s
def change_bool(df, bool_cols):
    for col in bool_cols:
        df[col] = df[col].astype(int)
    return df 
