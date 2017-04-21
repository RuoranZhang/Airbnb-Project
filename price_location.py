def price_per_person(df):
    if int(df['minimum_nights'])>=1 and int(df['guests_included'])>=1:
        return int((df['price_num']*int(df['minimum_nights'])+int(df['cleaning_fee_num']))/(int(df['minimum_nights'])*int(df['guests_included'])))
    else: # ignore the missing minimum_nights and guests_included data
        return 0


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

df['price_num'] = (df['price'].apply(lambda x: int(float(''.join(x[1:].split(','))))))
df['cleaning_fee_num']=(df['cleaning_fee'].apply(lambda x: int(float(x[1:]))))
df['price_per_person']=df.apply(price_per_person,axis=1)

def f(row):
    if row['price_per_person'] <=100:
        val = "less than 100"
    elif row['price_per_person'] <=200:
        val = "between 100 and 200"
    elif row['price_per_person'] <=300:
        val = "between 200 and 300"
    elif row['price_per_person'] >300:
        val = "larger than 300"
    return val

df['price_range'] = df.apply(f, axis=1)


group = df.groupby('neighbourhood_group_cleansed')

import matplotlib.pyplot as plt

# distribution of the price range
district=['Bronx','Brooklyn','Manhattan','Queens','Staten Island']
N = 5
menMeans = [group.size()[i] for i in district]


ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width)
group.size().plot(kind='bar',color=['yellowgreen', 'gold','lightcoral','lightskyblue','purple'],width=0.7,figsize=(10,5))

# add some text for labels, title and axes ticks
ax.set_ylabel('')
ax.set_xlabel('')
ax.set_title('')
ax.set_xticks(ind + width)
ax.set_xticklabels(('Bronx','Brooklyn','Manhattan','Queens','Staten Island'),rotation=15)
plt.ylim((0,22000))



def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/5, 1*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
plt.savefig('static/images/district.png')
plt.close()

district_price=df.groupby(['price_range','neighbourhood_group_cleansed'])
data=district_price.size().unstack()
data['Bronx'].plot.pie(figsize=(12, 12),colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple'],
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.ylabel('')
plt.savefig('static/images/bronx.png')
plt.close()

data['Brooklyn'].plot.pie(figsize=(12, 12),colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple'],
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.ylabel('')
plt.savefig('static/images/brooklyn.png')
plt.close()

data['Manhattan'].plot.pie(figsize=(12, 12),colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple'],
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.ylabel('')
plt.savefig('static/images/manhattan.png')
plt.close()

data['Queens'].plot.pie(figsize=(12, 12),colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple'],
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.ylabel('')
plt.savefig('static/images/queens.png')
plt.close()

data['Staten Island'].plot.pie(figsize=(12, 12),colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','purple'],
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.ylabel('')
plt.savefig('static/images/staten_island.png')
plt.close()

