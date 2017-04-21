def price_per_person(df):
    if int(df['minimum_nights'])>=1 and int(df['guests_included'])>=1:
        return int((df['price_num']*int(df['minimum_nights'])+int(df['cleaning_fee_num']))/(int(df['minimum_nights'])*int(df['guests_included'])))
    else: # ignore the missing minimum_nights and guests_included data
        return 0




def suggest_a_place(accommodates,neighbourhood_group_cleansed,min_price,max_price,first_prefer,second_prefer,third_prefer,fourth_prefer):
    import pandas as pd
    import numpy as np
    datafile='table/listings.csv'
    df=pd.read_csv(datafile,'utf-8',engine='python',delimiter=',',index_col='id')
    pd.set_option('display.max_columns',100)
    
    df['minimum_nights'].replace(0,1) #assume missing data minimum night is 1
    df['guests_included'].replace(0,1) #assume only 1 guest
    df['cleaning_fee'].fillna('0.0', inplace=True)
    df['review_scores_rating'].fillna(0, inplace=True)
    df['review_scores_accuracy'].fillna(0, inplace=True)
    df['review_scores_cleanliness'].fillna(0, inplace=True)
    df['review_scores_checkin'].fillna(0, inplace=True)
    df['review_scores_communication'].fillna(0, inplace=True)
    df['review_scores_location'].fillna(0, inplace=True)
    df['review_scores_value'].fillna(0, inplace=True)
    df['requires_license'].fillna(0, inplace=True)
    df['accommodates'].fillna(0, inplace=True)
    df['thumbnail_url'].fillna('http://www.hotelnewsnow.com/Media/Default/Legacy//FeatureImages/airbnb_newyork.jpg', inplace=True)


    df['price_num'] = (df['price'].apply(lambda x: int(float(''.join(x[1:].split(','))))))
    df['cleaning_fee_num']=(df['cleaning_fee'].apply(lambda x: int(float(x[1:]))))
    df['price_per_person']=df.apply(price_per_person,axis=1)
    
    # price_per_person, neighbourhood_group_cleansed,
    data=df[(df['accommodates']==accommodates) & (df['neighbourhood_group_cleansed']==neighbourhood_group_cleansed) & ((df['price_per_person']>min_price) & (df['price_per_person']<max_price))]
    
    #preference: review_scores_rating,review_scores_cleanliness,review_scores_checkin
    # review_scores_communication, review_scores_location,
    data_filter=data.sort([first_prefer,second_prefer,third_prefer,fourth_prefer], ascending=False)
    
    #number of suggestion: maximum 5 
    if len(data_filter)>=5:
        data_filter1=data_filter.iloc[:5]
    else:
        data_filter1=data_filter.iloc[:]
        
    id_list=data_filter1.index.tolist()
    #print(id_list)
    name_list=list()
    picture_list=list()
    price_list=list()
    for id in id_list:
        name_list.append(data_filter1.loc[id]['name'])
        picture_list.append(data_filter1.loc[id]['thumbnail_url'])
        price_list.append(data_filter1.loc[id]['price_per_person'])

    
    #name_picture=[(x,y) for x,y in zip(name_list,picture_list)]
    #name_id={x:y for x,y in zip(id_list,name_picture)}
    return id_list,name_list,picture_list,price_list
