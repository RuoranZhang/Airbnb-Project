from flask import Flask, render_template, flash, request, url_for, redirect


#from content_management import Content
from suggestion import suggest_a_place
from suggestion import price_per_person

from data_frame import listings

from word_cloud import word_cloud
from word_cloud import getting_comments

from network_graph import get_lat_lng_host
from network_graph import network_graph

from properties_and_compare import prop
from percentile import pctl 
from percentile import df 

from price import price
import numpy as np
import matplotlib.pyplot as plt




#name_id=suggest_a_place(accommodates,neighbourhood_group_cleansed,min_price,max_price,first_prefer,second_prefer,third_prefer,fourth_prefer)

app=Flask(__name__)


@app.route('/')
def homepage():
	return render_template("main.html")

@app.route('/heatmap/')
def heatmap():
	return render_template("heatmap.html")

@app.route('/for_host/')#methods=['GET','POST'])
def for_host():
	if request.method == 'POST':
		x1 = request.form.get('neighbourhood')
		x2 = request.form.get('room_type')
		x3 = request.form.get('accommodates')
		x4 = request.form.get('bathrooms')
		x5 = request.form.get('bedrooms')
		x6 = request.form.get('cleanliness')
		x7 = request.form.get('communication')
		x8 = request.form.get('location')
		x9 = price(x1,x2,x3,x4,x5,x6,x7,x8)
	return render_template("hostparams.html") 

@app.route('/price_recommendation/',methods=['GET','POST'])
def price_recommendation():
	if request.method == 'POST':
		x1 = request.form.get('neighbourhood')
		x2 = request.form.get('room_type')
		x3 = request.form.get('accommodates')
		x4 = request.form.get('bathrooms')
		x5 = request.form.get('bedrooms')
		x6 = request.form.get('cleanliness')
		x7 = request.form.get('communication')
		x8 = request.form.get('location')
		x9 = price(x1,x2,x3,x4,x5,x6,x7,x8)

		
		labels_2016 = ['transport','clean','quiet','host']
		values = [0.67, 0.34, 0.75, 0.55]
		colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
		explode = (0, 0, 0.1, 0)
		plt.figure(figsize=(10, 10))
		plt.pie(values, explode=explode, labels=labels_2016, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
		plt.savefig('static/images/key_word.png')
		plt.close()
		
		
	return render_template('hostoutput.html',neighbourhood=x1,room_type=x2,accommodates=x3,bathrooms=x4,bedrooms=x5,cleanliness=x6,communication=x7,location=x8,price=x9)

@app.route('/for_rent/')
def for_rent():
	return render_template("for_rent.html") 


@app.route('/find_a_place/',methods=['GET','POST'])
def find_a_place():
	error=""
	#if method=="POST":
	if request.method =='POST':
		accommodates=request.form.get('accommodates')
		neighbourhood_group_cleansed=request.form.get('neighbourhood_group_cleansed')
		min_price=request.form.get('min_price')
		max_price=request.form.get('max_price')
		first_prefer=request.form.get('first_prefer')
		second_prefer=request.form.get('second_prefer')
		third_prefer=request.form.get('third_prefer')
		fourth_prefer=request.form.get('fourth_prefer')
		if accommodates is not None and neighbourhood_group_cleansed is not None and min_price is not None and max_price is not None and first_prefer is not None and second_prefer is not None and third_prefer is not None and fourth_prefer is not None:
			i_list,nam_list,pictur_list,price_list=suggest_a_place(accommodates=int(accommodates), neighbourhood_group_cleansed= neighbourhood_group_cleansed, min_price= int(min_price), max_price= int(max_price),first_prefer=first_prefer, second_prefer= second_prefer, third_prefer= third_prefer, fourth_prefer= fourth_prefer)	
	print(pictur_list)
	return render_template("find_a_place.html",id_list_=i_list,name_list_=nam_list,picture_list_=pictur_list,price_list_=price_list) 

@app.route('/find_a_place/<id>', methods=['GET','POST'])
def show_user_profile(id):
	
	id = int(id)
	word_cloud_ = word_cloud(id)


	df=listings()
	network_graph_1= network_graph(id,'driving')
	network_graph_2= network_graph(id,'walking')
	info_dict,summary_=prop(id)
	pctl_list=pctl(id)

	return render_template("content.html",id=id ,df=df, info_dict=info_dict, summary_=summary_, recom_list=network_graph_2, word_cloud_=word_cloud_,network_graph_1=network_graph_1, pctl_list=pctl_list)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')


   
	

if __name__=='__main__':
	app.debug = True
	app.run()



