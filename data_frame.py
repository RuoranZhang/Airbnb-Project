
def listings():
    import pandas as pd
    import numpy as np
    datafile='table/listings.csv'
    df=pd.read_csv(datafile,'utf-8',engine='python',delimiter=',',index_col='id')
    pd.set_option('display.max_columns',100)
    pd.set_option('display.max_colwidth', -1)
    df['thumbnail_url'].fillna('http://www.hotelnewsnow.com/Media/Default/Legacy//FeatureImages/airbnb_newyork.jpg', inplace=True)
    return df