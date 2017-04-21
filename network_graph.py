

def get_lat_lng_host(id):
    import pandas as pd
    import numpy as np
    datafile='table/listings.csv'
    df=pd.read_csv(datafile,'utf-8',engine='python',delimiter=',',index_col='id')
    #pd.set_option('display.max_columns',100)
    #df
    lat=df.loc[id]['latitude']
    lng=df.loc[id]['longitude']
    return str(lat)+','+str(lng)



def network_graph(id,mode):
    tourist_arbnb=['Central Park','Times Square', 'Empire State Building','World Trade Center','Statue of Liberty','High Line', 'Brooklyn Bridge','Airbnb']
    
    #latlons=''
    #for i in tourist_arbnb[:-1]:
        #latlon=get_geolocation_data(i,' New York')
        #latlons += latlon + '|'
    latlons='40.7711329,-73.97418739999999|40.759011,-73.9844722|40.7484405,-73.98566439999999|40.7118011,-74.0131196|40.6892494,-74.04450039999999|40.7479925,-74.0047649|40.7060855,-73.9968643|'
    latlon=get_lat_lng_host(id) #get the lat_lng for airbnb location
    latlons += latlon + '|'
   
    AUTH_KEY ="AIzaSyAva9CqAks4H3YBGvC3PT8wkqw3KOJS7QY"
   
    distance_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='
    distance_url+=latlons
    distance_url+='&destinations='
    distance_url+=latlons
    #Set the mode walking, driving, cycling
    #mode='driving' #'walking'
    distance_url+='&mode='+mode
    
    distance_url+='&key='
    distance_url+=AUTH_KEY
    #print(distance_url)
    
    import networkx as nx
    import numpy as np
    import matplotlib.pyplot as plt
    import requests
    data=requests.get(distance_url).json()
   

    all_rows = data['rows']
    
    tourist_arbnb_graph=nx.Graph()
    tourist_arbnb_graph.add_nodes_from(tourist_arbnb)
    origin = tourist_arbnb[-1]
    weight_list=list()
    duration_list=list()
    for j in range(len(all_rows[-1]['elements'][1:])):
        duration = all_rows[-1]['elements'][j]['duration']['text'] #value in seconds
        weight=float(all_rows[-1]['elements'][j]["distance"]['text'][:-2])
        destination =tourist_arbnb[j]
        #tourist_arbnb_graph.add_edge(origin,destination,weight=1/weight,duration=duration)
        tourist_arbnb_graph.add_edge(origin,destination)
        weight_list.append(str(weight)+'km')
        duration_list.append(duration)
        #print(origin,'->',destination,'->','->',str(weight)+'km','->',duration)
    #nx.draw(tourist_arbnb_graph)
    x=list((origin,j) for j in tourist_arbnb[:-1])
    weight_duration=list((x,y) for x,y in zip(weight_list,duration_list))
    ww={z:y for z,y in zip(x,weight_duration)}
    
    from urllib import request
    from io import BytesIO
    from PIL import Image
    from PIL import ImageOps

    img1=Image.open('picture/central.jpg')
    img2=Image.open('picture/time_squre.jpg')
    img3=Image.open('picture/emp.jpg')
    img4=Image.open('picture/world_trade_center.jpg')
    img5=Image.open('picture/statue.jpg')
    img6=Image.open('picture/high_line_park.jpg')
    img7=Image.open('picture/brooklyn.jpg')
    img8=Image.open('picture/arbnb.jpg')

    tourist_arbnb_graph.node['Central Park']['image']=img1
    tourist_arbnb_graph.node['Times Square']['image']=img2
    tourist_arbnb_graph.node['Empire State Building']['image']=img3
    tourist_arbnb_graph.node['World Trade Center']['image']=img4
    tourist_arbnb_graph.node['Statue of Liberty']['image']=img5
    tourist_arbnb_graph.node['High Line']['image']=img6
    tourist_arbnb_graph.node['Brooklyn Bridge']['image']=img7
    tourist_arbnb_graph.node['Airbnb']['image']=img8

    pos=nx.spring_layout(tourist_arbnb_graph,scale=1.5)
    #nx.draw_networkx_edge_labels(tourist_arbnb_graph,pos,ww)

    fig=plt.figure(figsize=(20,20))
    ax=plt.subplot(111)
    plt.axis('off')
    
    #elarge=[(u,v) for (u,v,d) in tourist_arbnb_graph.edges(data=True) if d['weight']>10]
    #esmall=[(u,v) for (u,v,d) in tourist_arbnb_graph.edges(data=True) if d['weight']<=10]
    
    ax.set_aspect('equal')
    #nx.draw_networkx_edges(tourist_arbnb_graph,pos,edgelist=elarge,ax=ax,color='b',style='dashed')
    nx.draw_networkx_edges(tourist_arbnb_graph,pos,ax=ax,color='b',style='dashed')
    nx.draw_networkx_edge_labels(tourist_arbnb_graph,pos,ww,ax=ax,font_color='r',font_size=25)

    plt.xlim(-0.5,1.5)
    plt.ylim(-0.5,1.5)

    trans=ax.transData.transform
    trans2=fig.transFigure.inverted().transform

    piesize=0.08 # this is the image size
    p2=piesize/2.0
    for n in tourist_arbnb_graph:
       xx,yy=trans(pos[n]) # figure coordinates
       xa,ya=trans2((xx,yy)) # axes coordinates
       a = plt.axes([xa-p2,ya-p2, piesize, piesize])
       a.set_aspect('equal')
       a.imshow(tourist_arbnb_graph.node[n]['image'])
       a.axis('off')
    if mode=='driving':
        plt.savefig('static/images/network_graph_driving.png', dpi=200)
        plt.close()
        return None
    elif mode=='walking':
        plt.savefig('static/images/network_graph_walking.png',dpi=200)
        plt.close()
        recom_list=list()
        for key,value in ww.items():
            if float(value[0][:-2])<=2:
                recom_list.append((key[1],'walking'))
            else:
                recom_list.append((key[1],'driving'))
    return recom_list







