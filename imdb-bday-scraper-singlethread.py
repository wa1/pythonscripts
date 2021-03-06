# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:03:57 2016

@author: Erik
"""

from urllib import request
from lxml import html
#from lxml import etree
import requests
#import bs4 as soup
import datetime
import os.path
import sys

imdb_bday_url = 'http://www.imdb.com/search/name?birth_day={0}&birth_month={1}&refine=birth_monthday'
imdb_base_url = 'http://www.imdb.com'
imdb_list_xpath = '//*[@id="main"]/table/tr/td[@class="name"]/a' #removed tbody, http://stackoverflow.com/questions/32015083/python-xpath-returns-an-empty-list#comment51932748_32015083
imdb_img_xpath = '//*[@id="name-poster"]/@src'
imdb_birthyear_xpath = '//*[@id="name-born-info"]/time/a[2]'
#imdb_deathyear_xpath = '//*[@id="name-death-info"]/time/a[2]'
#imdb_birthdate_xpath = '//*[@id="name-born-info"]/time/@datetime'
#imdb_deathdate_xpath = '//*[@id="name-death-info"]/time/@datetime'

app_dir =  "c:\\users\\erik.lundin\\desktop\\imdb_scraper\\{0}"
app_dir_fw = "c:/users/erik.lundin/desktop/imdb_scraper/{0}"

start_date = datetime.date(2016,1,1) # use 2016 since it's a leap year, other than that it's just an arbitrary value for year since year is irrelevant
end_date = datetime.date(2016,1,4) #(2016,1,2)
delta = datetime.timedelta(days=1) # set the iteration step to 1 day
persons_per_bday = 5

bdays = list() # the root node of the data to generate
d = start_date # d holds the current date iteration

while d <= end_date: # For each day, create a birthday object containing its date and an array of 5 birthday peeps    
    bday_temp = {} # Reset birthday object
    bday_temp["persons"] = list()
                                                             
    stamp = d.strftime("%d/%m");
    str_day = d.strftime("%d");
    str_month = d.strftime("%m"); 
    bday_temp["date"] = stamp    
    
    print("Starting downloads for " + stamp + 
          ". URL: " + imdb_bday_url.format(str_day, str_month))
    
    imdb_page = requests.get(imdb_bday_url.format(str_day,str_month)) # Get the web page content
    page_tree = html.fromstring(imdb_page.content) # Get the html tree
    elements = page_tree.xpath(imdb_list_xpath) # Get a list of html elements, each person in the listing       
    
    x = 0
    x_max = persons_per_bday
    while x < x_max: # Loop through the first 5 persons in the listing, for x in range(0, persons_per_bday) replaced with while in order to solve problem where there is no image
        try:        
            person_temp = {} # Reset person object       
            person_temp["url"] = imdb_base_url + elements[x].attrib.get('href') # Get the link to the person's imdb page       
            person_temp["name"] = elements[x].text # Get the person's name         
            print(person_temp["name"])
            
            imdb_person_page = requests.get(person_temp["url"]) # Get the web page content
            person_tree = html.fromstring(imdb_person_page.content) # Get the html tree
            img_url = person_tree.xpath(imdb_img_xpath) # Get image src URL 
            img_type = os.path.splitext(img_url[0])[1] # Get the file extension part
            img_name = person_temp["name"].replace(" ", "") + img_type # Make a file name out of the person's full name
            request.urlretrieve(img_url[0], app_dir.format(img_name))
            person_temp["img"] = img_name
                        
            person_birthyear = person_tree.xpath(imdb_birthyear_xpath) # Get birthyear
            
            bday_temp["persons"].append(person_temp)
            x+=1;
        except: 
            print(">>>")
            print("Unexpected error:", sys.exc_info()[0])
            print("< < <")
            x_max+=1
            if x_max >= 20:
                print("Too many retries, can't find 5 persons, exiting loop for the given day")
                break
    
    bdays.append(bday_temp) # Add to birthday list
    d += delta # Go to next day
        
print(bdays)

import json
with open(app_dir_fw.format('birthdays.json'), 'w') as outfile:
    json.dump(bdays, outfile, indent=4, sort_keys=True) # indent=4, sort_keys=True
    
    
    
    
    
#tree = etree.HTML(imdb_page.text)
#element = tree.xpath('//*[@id="main"]/table/tr/td[@class="name"]/a/text()')
#print(element)
#content = etree.tostring(element[0])

###########

    #print('name: ' + person_name + ', url: ' + person_url)
#tree = soup.BeautifulSoup(imdb_page.content, 'lxml')

#actor = {}
#actor["name"] = "Erik Lundin"
#actor["year"] = 1234
#actor["img"] = "erik.jpg"
#
#actor2 = {}
#actor2["name"] = "Kalle Kula"
#actor2["year"] = 5678
#actor2["img"] = "kalle.jpg"
#
#actor3 = {}
#actor3["name"] = "Urban Turbo"
#actor3["year"] = 1122
#actor3["img"] = "urban.jpg"
#
#persons = list()
#persons.append(actor)
#persons.append(actor2)
#persons2 = list()
#persons2.append(actor3)
#
#birthday = {}
#birthday["date"] = "01/01"
#birthday["persons"] = persons
#
#birthday2 = {}
#birthday2["date"] = "02/01"
#birthday2["persons"] = persons2
#
#birthdays = list()
#birthdays.append(birthday)
#birthdays.append(birthday2)
#print(birthdays)

#img_url = "https://www.google.se/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png";
#img_dir =  "c:\\users\\erik.lundin\\desktop\\scrapy\\{0}.jpg"
#img_name = "imagename"
#request.urlretrieve(img_url, img_dir.format(img_name))