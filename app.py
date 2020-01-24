# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:40:57 2020

@author: 154014
"""



#Importing necessary libraries
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, jsonify 
import os
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer

#import request
app = Flask(__name__) # initialize the flask app with the name app

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')



@app.route('/showImages')
@cross_origin()
def displayImages():
    list_Images = os.listdir('static')
    print('list_Images')
    
    try:
        if(len(list_Images)>0):
            return render_template('showImage.html', user_images = list_Images)
        else:
            return "Images are not present"
        
    except Exception as e:
        print("No images found", e)
        return "Please try with a different search keyword"


@app.route('/searchImages', methods = ['Get','POST'])
def searchImage():
    if request.method == 'POST':
        #assigning te value of the input keyword to the variable
        search_term = request.form['keyword']
        
    else:
        print("Please enter something")
        
    imageScrapperUtil = BusinessLayer## Instantiate a object for ScrapperImage Class
    imageScrapper = ScrapperImage()
    list_images = os.listdir('static')
    
    imageScrapper.delete_downloaded_images(list_images) ##Delete the old image before search
    
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    
    lst_images = imageScrapperUtil.downloadImages(search_term, header)
    return displayImages()
    
    



if __name__ =="__main__":
    app.run(host = "127.0.0.1", port = 8000)