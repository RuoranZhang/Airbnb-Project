def price(neighbourhood,room_type,accommodates,bathrooms,bedrooms,review_scores_cleanliness,review_scores_communication,review_scores_location):
    import pandas as pd
    from pandas_datareader import data
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mp
    import datetime as dt
    data = pd.read_csv('airbnb_data_NYC/listings(1).csv','utf-8',engine='python',delimiter=',')
    df = data[data['neighbourhood_group_cleansed'].isin([neighbourhood])]
    df = df.loc[:,['room_type','accommodates','bathrooms','bedrooms','review_scores_cleanliness','review_scores_communication','review_scores_location','price']]
    # price convert string into float
    df['price'] = df['price'].str.slice(1)
    df['price'] = df['price'].convert_objects(convert_numeric=True)
    # remove nan value
    for i in df:
        df = df[pd.notnull(df[i])]
    # change index
    df.index = list(range(len(df))) 
    # set dummy variable for room type
    df['x1'] = 0
    df['x2'] = 0
    cols = df.columns.tolist()
    cols = [cols[0]] + cols[-2:] + cols[1:len(cols)-2]
    df = df[cols]
    for i in range(len(df)):
        if df.loc[i]['room_type'] == 'Entire home/apt':
            df.ix[i,'x1'] = 1
        if df.loc[i]['room_type'] == 'Private room':
            df.ix[i,'x2'] = 1
    # delete
    del df['room_type']

    # create X and Y 
    cols = df.columns.tolist()
    cols = cols[:-1]
    X = df[cols]
    Y = df['price']
    size = 0.01
    if neighbourhood == 'Bronx' or neighbourhood == 'Staten Island' or neighbourhood == 'Queens':
        size = 0.1
    ##构造训练集和测试集  
    from sklearn.cross_validation import train_test_split  #这里是引用了交叉验证  
    X_train,X_test, Y_train, Y_test = train_test_split(X, Y, test_size=size, random_state=1)  
    from sklearn.linear_model import LinearRegression  
    linreg = LinearRegression()  
    model=linreg.fit(X_train, Y_train) 
    coef_ = linreg.coef_
    intercept_ = linreg.intercept_
    # pair the feature names with the coefficients  
    Y_pred = linreg.predict(X_test) 
    Y_pred = 1.2*Y_pred  
    plt.figure(figsize=(30, 10))  
    plt.plot(range(len(Y_pred)),Y_pred,'b',label="predict")  
    plt.plot(range(len(Y_pred)),Y_test,'r',label="test")  
    plt.legend(loc="upper right") #显示图中的标签  
    plt.xlabel("the number of sales")  
    plt.ylabel('value of sales')
    plt.title('Comparison between test prices and predictive prices')  
    if neighbourhood == "Manhattan":
        plt.savefig('static/images/comparisonManhattan.png')
        
    elif neighbourhood == "Brooklyn":
        plt.savefig('static/images/comparisonBrooklyn.png')
        
    elif neighbourhood == "Queens":
        plt.savefig('static/images/comparisonQueens.png')
       
    elif neighbourhood == "Bronx":
        plt.savefig('static/images/comparisonBronx.png')
        
    elif neighbourhood == "Staten Island":
        plt.savefig('static/images/comparisonStatenIsland.png')
    plt.close()
    

    if room_type == 'Entire home/apt':
        x1 = 1
        x2 = 0
    elif room_type == 'Private room':
        x1 = 0
        x2 = 1
    else:
        x1 = 0
        x2 = 0
    # type of input is string, change to float
    accommodates = float(accommodates)
    bathrooms = float(bathrooms)
    bedrooms = float(bedrooms)
    review_scores_cleanliness = float(review_scores_cleanliness)
    review_scores_communication = float(review_scores_communication)
    review_scores_location = float(review_scores_location)
    l = [x1,x2,accommodates,bathrooms,bedrooms,review_scores_cleanliness,review_scores_communication,review_scores_location]
    x = zip(l,coef_)
    price = 0
    for i in list(x):
        price += (i[0]*i[1])
    price = 1.2*(price + intercept_)
    price = int(price)
    return price

