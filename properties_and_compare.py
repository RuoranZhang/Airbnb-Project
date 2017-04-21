

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import pandas as pd
from scipy import stats as ss
def df():
    dataframe = pd.read_csv('table/listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    return dataframe

def prop(id):
    dataframe=df()
    #dataframe = pd.read_csv('/Users/jizeng/1_DATA_ANALYTICS/airbnb/listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    properties = pd.DataFrame(dataframe, columns = ['property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms','beds','bed_type','square_feet','description' ])
    pd.set_option('display.max_colwidth', -2)
    l1 = ['property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms','beds','bed_type','square_feet']
    d = {}
    for item in l1:
        d.update({item:properties.loc[id][item]})
    summary=properties.loc[id]['description']
    return d,summary


def rating_dist(id):
    dataframe=df()
    #dataframe = pd.read_csv('/Users/jizeng/1_DATA_ANALYTICS/airbnb/listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    review_scores_rating = dataframe[dataframe['review_scores_rating'].notnull()]
    review_scores_rating = pd.DataFrame(review_scores_rating, columns = ['review_scores_rating'])
    rating_list = list()
    for i in range(len(review_scores_rating)):
        rating_list.append(review_scores_rating.iloc[i]['review_scores_rating'])
    rating_pctl = int(ss.percentileofscore(rating_list, review_scores_rating.loc[id]['review_scores_rating'], kind='weak'))
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in rating_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])
    value = review_scores_rating.loc[id]
    fig = plt.figure()
    fig.suptitle('Rating distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_title('percentile is {}%'.format(rating_pctl))
    ax.set_xlabel('rating score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)  
    plt.plot([value, value], [0, max(L2)], 'r-', lw=4)
    plt.savefig('static/images/rating.png')
    plt.close()
    

def accuracy_dist(id):
    dataframe=df()
    #dataframe = pd.read_csv('listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    review_scores_accuracy = dataframe[dataframe['review_scores_accuracy'].notnull()]
    review_scores_accuracy = pd.DataFrame(review_scores_accuracy, columns = ['review_scores_accuracy'])
    accuracy_list = list()
    for i in range(len(review_scores_accuracy)):
        accuracy_list.append(review_scores_accuracy.iloc[i]['review_scores_accuracy'])
    accuracy_pctl = int(ss.percentileofscore(accuracy_list, review_scores_accuracy.loc[id]['review_scores_accuracy'], kind='weak'))
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in accuracy_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])
    value = review_scores_accuracy.loc[id]
    fig = plt.figure()
    fig.suptitle('Accuracy distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_title('percentile is {}%'.format(accuracy_pctl))
    ax.set_xlabel('accuracy score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)  
    plt.plot([value, value], [0, max(L2)], 'r-', lw=4)
    plt.savefig('static/images/accuracy.png')
    plt.close()
        

def cleanliness_dist(id):
    dataframe=df()
    #dataframe = pd.read_csv('listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    review_scores_cleanliness = dataframe[dataframe['review_scores_cleanliness'].notnull()]
    review_scores_cleanliness = pd.DataFrame(review_scores_cleanliness, columns = ['review_scores_cleanliness'])
    cleanliness_list = list()
    for i in range(len(review_scores_cleanliness)):
        cleanliness_list.append(review_scores_cleanliness.iloc[i]['review_scores_cleanliness'])
    cleanliness_pctl = int(ss.percentileofscore(cleanliness_list, review_scores_cleanliness.loc[id]['review_scores_cleanliness'], kind='weak'))
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in cleanliness_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])
    value = review_scores_cleanliness.loc[id]
    fig = plt.figure()
    fig.suptitle('Cleanliness distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_title('percentile is {}%'.format(cleanliness_pctl))
    ax.set_xlabel('cleanliness score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)  
    plt.plot([value, value], [0, max(L2)], 'r-', lw=4)
    plt.savefig('static/images/cleanliness.png')
    plt.close()


def checkin_dist(id):
    dataframe=df()
    #dataframe = pd.read_csv('listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    review_scores_checkin = dataframe[dataframe['review_scores_checkin'].notnull()]
    review_scores_checkin = pd.DataFrame(review_scores_checkin, columns = ['review_scores_checkin'])
    checkin_list = list()
    for i in range(len(review_scores_checkin)):
        checkin_list.append(review_scores_checkin.iloc[i]['review_scores_checkin'])
    checkin_pctl = int(ss.percentileofscore(checkin_list, review_scores_checkin.loc[id]['review_scores_checkin'], kind='weak'))
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in checkin_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])
    value = review_scores_checkin.loc[id]
    fig = plt.figure()
    fig.suptitle('Checkin distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_title('percentile is {}%'.format(checkin_pctl))
    ax.set_xlabel('checkin score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)  
    plt.plot([value, value], [0, max(L2)], 'r-', lw=4)
    plt.savefig('static/images/checkin.png')
    plt.close()



def communication_dist(id):
    dataframe=df()
    #dataframe = pd.read_csv('listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    review_scores_communication = dataframe[dataframe['review_scores_communication'].notnull()]
    review_scores_communication = pd.DataFrame(review_scores_communication, columns = ['review_scores_communication'])
    communication_list = list()
    for i in range(len(review_scores_communication)):
        communication_list.append(review_scores_communication.iloc[i]['review_scores_communication'])
    communication_pctl = int(ss.percentileofscore(communication_list, review_scores_communication.loc[id]['review_scores_communication'], kind='weak'))
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in communication_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])
    value = review_scores_communication.loc[id]
    fig = plt.figure()
    fig.suptitle('Communication distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_title('percentile is {}%'.format(communication_pctl))
    ax.set_xlabel('communication score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)  
    plt.plot([value, value], [0, max(L2)], 'r-', lw=4)
    plt.savefig('static/images/communication.png')
    plt.close()



def location_dist(id):
    dataframe=df()
    #dataframe = pd.read_csv('listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    review_scores_location = dataframe[dataframe['review_scores_location'].notnull()]
    review_scores_location = pd.DataFrame(review_scores_location, columns = ['review_scores_location'])
    location_list = list()
    for i in range(len(review_scores_location)):
        location_list.append(review_scores_location.iloc[i]['review_scores_location'])
    location_pctl = int(ss.percentileofscore(location_list, review_scores_location.loc[id]['review_scores_location'], kind='weak'))
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in location_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])
    value = review_scores_location.loc[id]
    fig = plt.figure()
    fig.suptitle('Location distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_title('percentile is {}%'.format(location_pctl))
    ax.set_xlabel('location score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)  
    plt.plot([value, value], [0, max(L2)], 'r-', lw=4)
    plt.savefig('static/images/location.png')
    plt.close()
        




def value_dist(id):
    dataframe=df()

    #dataframe = pd.read_csv('listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')
    review_scores_value = dataframe[dataframe['review_scores_value'].notnull()]
    review_scores_value = pd.DataFrame(review_scores_value, columns = ['review_scores_value'])
    value_list = list()
    for i in range(len(review_scores_value)):
        value_list.append(review_scores_value.iloc[i]['review_scores_value'])
    value_pctl = int(ss.percentileofscore(value_list, review_scores_value.loc[id]['review_scores_value'], kind='weak'))
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in value_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])
    value = review_scores_value.loc[id]
    fig = plt.figure()
    fig.suptitle('Value distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_title('percentile is {}%'.format(value_pctl))
    ax.set_xlabel('value score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)  
    plt.plot([value, value], [0, max(L2)], 'r-', lw=4)
    plt.xlabel("value score")  
    plt.savefig('static/images/value.png')
    plt.close()
#rating_dist(523123)

        