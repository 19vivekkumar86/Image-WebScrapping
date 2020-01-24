# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:18:45 2020

@author: 154014
"""

from scrapperImage.ScrapperImage import ScrapperImage

class BusinessLayer:
    keyWord = ""
    fileLoc = ""
    image_name = ""
    header = ""
    
    def downloadImages(keyWord, header):
        imgScrapper = ScrapperImage
        url = imgScrapper.createImageURL(keyWord)
        rawhtml  = imgScrapper.scrap_html_data(url, header)
        
        imageURLList = imgScrapper.getImageURLList(rawhtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList, keyWord, header)
        
        return masterListOfImages