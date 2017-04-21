def df():
    import pandas as pd
    dataframe = pd.read_csv('table/listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    return dataframe

def prop(id):
    dataframe = df()
    #dataframe = pd.read_csv('/Users/jizeng/1_DATA_ANALYTICS/airbnb/listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    properties = pd.DataFrame(dataframe, columns = ['property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms','beds','bed_type','square_feet' ])
    pd.set_option('display.max_colwidth', -2)
    l1 = ['property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms','beds','bed_type','square_feet']
    d = {}
    for item in l1:
        d.update({item:properties.loc[id][item]})
    return d

def pctl(id):
    from scipy import stats as ss
    import pandas as pd
    import pandas as pd
    dataframe = pd.read_csv('table/listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')

    review_scores_rating = dataframe[dataframe['review_scores_rating'].notnull()]
    review_scores_rating = pd.DataFrame(review_scores_rating, columns = ['review_scores_rating'])
    rating_list= review_scores_rating['review_scores_rating'].tolist()
    rating_pctl = int(ss.percentileofscore(rating_list, review_scores_rating.loc[id]['review_scores_rating'],kind='weak'))
    rating=('Rating',review_scores_rating.loc[id]['review_scores_rating'],str(rating_pctl)+'%')
    
    review_scores_accuracy = dataframe[dataframe['review_scores_accuracy'].notnull()]
    review_scores_accuracy = pd.DataFrame(review_scores_accuracy, columns = ['review_scores_accuracy'])
    accuracy_list= review_scores_accuracy['review_scores_accuracy'].tolist()
    accuracy_pctl = int(ss.percentileofscore(accuracy_list, review_scores_accuracy.loc[id]['review_scores_accuracy'],kind='weak'))
    accuracy=('Accuracy',review_scores_accuracy.loc[id]['review_scores_accuracy'],str(accuracy_pctl)+'%')
    
    review_scores_cleanliness = dataframe[dataframe['review_scores_cleanliness'].notnull()]
    review_scores_cleanliness = pd.DataFrame(review_scores_cleanliness, columns = ['review_scores_cleanliness'])
    cleanliness_list= review_scores_cleanliness['review_scores_cleanliness'].tolist()
    clean_pctl = int(ss.percentileofscore(cleanliness_list, review_scores_cleanliness.loc[id]['review_scores_cleanliness'],kind='weak'))
    clean=('Cleanliness',review_scores_cleanliness.loc[id]['review_scores_cleanliness'],str(clean_pctl)+'%')
    
    review_scores_checkin = dataframe[dataframe['review_scores_checkin'].notnull()]
    review_scores_checkin = pd.DataFrame(review_scores_checkin, columns = ['review_scores_checkin'])
    checkin_list= review_scores_checkin['review_scores_checkin'].tolist()
    checkin_pctl = int(ss.percentileofscore(checkin_list, review_scores_checkin.loc[id]['review_scores_checkin'],kind='weak'))
    ckeckin=('Checkin',review_scores_checkin.loc[id]['review_scores_checkin'],str(checkin_pctl)+'%')
    
    review_scores_communication = dataframe[dataframe['review_scores_communication'].notnull()]
    review_scores_communication = pd.DataFrame(review_scores_communication, columns = ['review_scores_communication'])
    communication_list=review_scores_communication['review_scores_communication'].tolist()
    communication_pctl = int(ss.percentileofscore(communication_list, review_scores_communication.loc[id]['review_scores_communication'],kind='weak'))
    communication=('Communication',review_scores_communication.loc[id]['review_scores_communication'],str(communication_pctl)+'%')
    
    review_scores_location = dataframe[dataframe['review_scores_location'].notnull()]
    review_scores_location = pd.DataFrame(review_scores_location, columns = ['review_scores_location'])
    location_list= review_scores_location['review_scores_location'].tolist()
    location_pctl = int(ss.percentileofscore(location_list, review_scores_location.loc[id]['review_scores_location'],kind='weak'))
    location=('Location',review_scores_location.loc[id]['review_scores_location'],str(location_pctl)+'%')
    
    review_scores_value = dataframe[dataframe['review_scores_value'].notnull()]
    review_scores_value = pd.DataFrame(review_scores_value, columns = ['review_scores_value'])
    value_list = review_scores_value['review_scores_value'].tolist()
    value_pctl = int(ss.percentileofscore(value_list, review_scores_value.loc[id]['review_scores_value'],kind='weak'))
    value=('Value',review_scores_value.loc[id]['review_scores_value'],str(value_pctl)+'%')
    pctl=[rating, accuracy,clean,ckeckin,communication,location,value]
    return pctl