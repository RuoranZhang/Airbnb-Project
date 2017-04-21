def getting_comments(id):
    import pandas as pd
    import numpy as np
    
    datafile='table/reviews_2.csv'
    df=pd.read_csv(datafile,index_col='listing_id')
    pd.set_option('display.max_colwidth', -1)
    #df
    
    text_string=str(df.loc[id]['comments'])
    remove_text=['\n'+str(id),'listing_id','\n','\\r','\\n',"\'"]
    #print(y)
    for word in remove_text:
        text_string=text_string.replace(word,' ') 
        
    word_list = text_string.split()
    for word in word_list:
        if len(word) < 7:
            text_string = text_string.replace(' '+word+' ',' ',1) 
    return text_string

def word_cloud(id):
    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    text_string=getting_comments(id)
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color='white',width=1200,height=1000,max_words=20).generate(text_string)


    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('static/images/word_could.png')
    plt.close()
    #return plt.savefig('static/images/word_could.png')
