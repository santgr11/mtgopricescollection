# -*- coding: utf-8 -*-
import scrapy

#Defining a list of the cards to use in multiple places.
cardslist = []

class PricebotSpider(scrapy.Spider):
    name = 'pricebot'
    allowed_domains = ['www.goatbots.com']
    start_urls = []
    
    cards = open("collection.txt")
    each = cards.readlines()
   
    #Adding the cards to the list from the txt file
    for line in each[4:-1]:
        name = line[60:-4]
        if name not in cardslist:
            cardslist.append(name)
        
    base = "https://www.goatbots.com/card/"
    
    #Here we create a link for every card to append to the start_urls
    for card in cardslist:
        fcard = card.replace(",", "")
        fcard = fcard.replace(" ", "-")
        fcard = fcard.replace("\\", "")
        fcard = fcard.replace('"', "")
        start_urls.append(base + fcard)
        
        
        
    def parse(self, response):
        #extracting content
        
        price = response.css(".price_value::text").extract_first()
        
        for item in zip(price):
            a = 0
            scraped_data = {
                'card' : cardslist[a],
                'price' : item[0]
            }
            a += 1
        
        yield scraped_data