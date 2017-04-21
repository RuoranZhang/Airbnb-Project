import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
dataframe = pd.read_csv('table/listings.csv', 'utf-8', engine = 'python', delimiter = ',', index_col='id')

def rating_dist():
    review_scores_rating = dataframe[dataframe['review_scores_rating'].notnull()]
    review_scores_rating = pd.DataFrame(review_scores_rating, columns = ['review_scores_rating'])
    rating_list = list()
    for i in range(len(review_scores_rating)):
        rating_list.append(review_scores_rating.iloc[i]['review_scores_rating'])
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in rating_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])

    fig = plt.figure()
    fig.suptitle('Rating distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_xlabel('rating score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)  
    plt.savefig('static/images/rating.png')
    plt.close()


def accuracy_dist():
    review_scores_accuracy = dataframe[dataframe['review_scores_accuracy'].notnull()]
    review_scores_accuracy = pd.DataFrame(review_scores_accuracy, columns = ['review_scores_accuracy'])
    accuracy_list = list()
    for i in range(len(review_scores_accuracy)):
        accuracy_list.append(review_scores_accuracy.iloc[i]['review_scores_accuracy'])
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in accuracy_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])

    fig = plt.figure()
    fig.suptitle('Accuracy distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_xlabel('accuracy score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3) 
    plt.savefig('static/images/accuracy.png')
    plt.close() 

def cleanliness_dist():
    review_scores_cleanliness = dataframe[dataframe['review_scores_cleanliness'].notnull()]
    review_scores_cleanliness = pd.DataFrame(review_scores_cleanliness, columns = ['review_scores_cleanliness'])
    cleanliness_list = list()
    for i in range(len(review_scores_cleanliness)):
        cleanliness_list.append(review_scores_cleanliness.iloc[i]['review_scores_cleanliness'])
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in cleanliness_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])

    fig = plt.figure()
    fig.suptitle('Cleanliness distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_xlabel('cleanliness score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)
    plt.savefig('static/images/cleanliness.png')
    plt.close() 

def checkin_dist():
    review_scores_checkin = dataframe[dataframe['review_scores_checkin'].notnull()]
    review_scores_checkin = pd.DataFrame(review_scores_checkin, columns = ['review_scores_checkin'])
    checkin_list = list()
    for i in range(len(review_scores_checkin)):
        checkin_list.append(review_scores_checkin.iloc[i]['review_scores_checkin'])
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in checkin_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])

    fig = plt.figure()
    fig.suptitle('Checkin distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_xlabel('checkin score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3)
    plt.savefig('static/images/checkin.png')
    plt.close()

def communication_dist():
    review_scores_communication = dataframe[dataframe['review_scores_communication'].notnull()]
    review_scores_communication = pd.DataFrame(review_scores_communication, columns = ['review_scores_communication'])
    communication_list = list()
    for i in range(len(review_scores_communication)):
        communication_list.append(review_scores_communication.iloc[i]['review_scores_communication'])
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in communication_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])

    fig = plt.figure()
    fig.suptitle('Communication distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_xlabel('communication score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3) 
    plt.savefig('static/images/communication.png')
    plt.close() 


def location_dist():
    review_scores_location = dataframe[dataframe['review_scores_location'].notnull()]
    review_scores_location = pd.DataFrame(review_scores_location, columns = ['review_scores_location'])
    location_list = list()
    for i in range(len(review_scores_location)):
        location_list.append(review_scores_location.iloc[i]['review_scores_location'])
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in location_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])

    fig = plt.figure()
    fig.suptitle('Location distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_xlabel('location score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3) 
    plt.savefig('static/images/location.png')
    plt.close() 


def value_dist():
    review_scores_value = dataframe[dataframe['review_scores_value'].notnull()]
    review_scores_value = pd.DataFrame(review_scores_value, columns = ['review_scores_value'])
    value_list = list()
    for i in range(len(review_scores_value)):
        value_list.append(review_scores_value.iloc[i]['review_scores_value'])
    L1 = list()
    L2 = list()
    dictionary = {}
    for item in value_list:
        dictionary[item] = dictionary.get(item,0)+1
    for key in dictionary:
        L1.append(key)
    for keys in dictionary:
        L2.append(dictionary[keys])

    fig = plt.figure()
    fig.suptitle('Value distribution', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)
    ax = fig.add_subplot(111)
    ax.set_xlabel('value score')
    ax.set_ylabel('amount')
    ax.plot(L1,L2,'b',lw = 3) 
    plt.savefig('static/images/value.png')
    plt.close()

rating_dist()
accuracy_dist()
cleanliness_dist()
checkin_dist()
communication_dist()
location_dist()
value_dist()
