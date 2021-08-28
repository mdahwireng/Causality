import pandas as pd

def describe(df:pd.DataFrame, stats=['skew', 'mad', 'median', 'kurt'])->pd.DataFrame:
    df = df.copy()
    d = df.describe()
    return d.append(df.reindex(d.columns, axis=1).agg(stats))

def filter_df(df, filter_col_name, filter_value):
    print('Filtering started...')
    seg = df
    filter_ = seg[filter_col_name] > filter_value
    print('\nFiltering completed')
    return seg[filter_]

def get_top10_per_col(df, top_num):
    df=df.copy()
    print('Retrieving columns info...')
    top_num_dict = {}
    for col in df.columns:
        print('Retrieving the top {} from {}'.format(top_num, col))
        top_num_dict[col] = df[col].sort_values(ascending=False).index[:top_num]
    print('Process completed')
    return top_num_dict

