# -*- coding: utf-8 -*-
import scrapy
import os
from mtgo.items import MtgoItem

#Defining a list of the cards to use in multiple places.
cardslist = []

class PricebotSpider(scrapy.Spider):
    name = "pricebot"
    allowed_domains = ['www.goatbots.com']
    start_urls = []
    
    
    path = os.path.join("collections", "collection2.txt")
    cards = open(path)
    each = cards.readlines()
   
    #Adding the cards to the list from the txt file
    for line in each[4:-1]:
        card = line[60:-4]
        card = card.replace(",", "").lower()
        card = card.replace(" ", "-")
        card = card.replace("\\", "")
        card = card.replace('"', "")
        card = card.replace("\'", "")        
        if card[-2:] == "-/":
            card = card[:-2]
        card = card.replace("/", "-")
        if card not in cardslist and card not in ("forest", "plain", "island", "swamp", "mountain"):            
            cardslist.append(card)
        
    base = "https://www.goatbots.com/card/"
    
    #Here we create a link for every card to append to the start_urls
    for card in cardslist:        
        start_urls.append(base + card)
     
            
    def parse(self, response):
        #extracting content
        item = MtgoItem()
        
        item["name"] = response.url[30:]
                           
        try:
            item["price"] = int(response.css(".price_value::text").extract_first())
        except ValueError:
            item["price"] = response.css(".price_value::text").extract_first()
        
        yield item 