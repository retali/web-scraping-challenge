from splinter import Browser
import requests
from bs4 import BeautifulSoup as bsp
from pprint import pprint
import pandas as pan
from markupsafe import Markup, escape

def init_browser():
    # Set Executable Path & Initialize Chrome Browser\
     executable_path = {'executable_path': 'chromedriver.exe'}
     browser = Browser('chrome', **executable_path, headless=False)
     return browser

data_web =  {}
images_urls = []

def scpeNews():    
    browser_news = init_browser()
    urlnews = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser_news.visit(urlnews)
    browser_news.is_element_present_by_css("ul.item_list li.slide", wait_time=0.5)
    resulhtml = browser_news.html
    soup_news = bsp(resulhtml, 'html.parser')
    latestNewsParagraph = (soup_news.find_all('div', class_='article_teaser_body'))[0].get_text()
    latestNewsTitle = (soup_news.find_all('div', class_='content_title'))[0].get_text()
    latestNewsDate = (soup_news.find_all('div', class_="list_date"))[0].get_text()   
    data_web["latestNewsParagraph"] = latestNewsParagraph
    data_web["latestNewsTitle"] = latestNewsTitle
    data_web["latestNewsDate"] = latestNewsDate
    browser_news.quit()
    return data_web
    
def scpeImage():
    browser_image = init_browser() 
    url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser_image.visit(url_image)
    html_image=browser_image.html
    soup_image = bsp(html_image, 'html.parser')   
    image = (soup_image.find_all('div', class_='carousel_items')[0].a.get('data-fancybox-href'))
    images = 'https://www.jpl.nasa.gov'+ image
    data_web['featImage'] = images
    browser_image.quit()
    return data_web
    
    
def scpeFacts():
    df = pan.read_html("https://space-facts.com/mars/")[0]
    df.columns=["Description", "Value"]
    df.set_index("Description", inplace=True)
    data_web['mars_facts'] = df.to_html(classes="table table-striped")    
    return data_web

        
def scpe_Cerberus():
    browser_Cerberus = init_browser()
    url_Cerberus = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser_Cerberus.visit(url_Cerberus)
    html_Cerberus=browser_Cerberus.html
    soup_Cerberus = bsp(html_Cerberus, 'html.parser')
    url_Cerberus = (soup_Cerberus.find_all('div', class_='downloads')[0].li.a.get('href'))
    images_urls.append([{"title": "Cerberus Hemisphere", "img_url": url_Cerberus}])
    data_web['images_urls']=images_urls
    browser_Cerberus.quit()
    return data_web
    
def scpe_Schiaparelli(): 
    browser_Schiaparelli = init_browser()
    url_Schiaparelli = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser_Schiaparelli.visit(url_Schiaparelli)
    html_Schiaparelli=browser_Schiaparelli.html
    soup_Schiaparelli = bsp(html_Schiaparelli, 'html.parser')
    url_Schiaparelli = (soup_Schiaparelli.find_all('div', class_='downloads')[0].li.a.get('href'))
    images_urls.append([{"title": "Schiaparelli Hemisphere", "img_url": url_Schiaparelli}])
    data_web['images_urls']=images_urls
    browser_Schiaparelli.quit()
    return data_web
    
def scpe_yrtisMajor():        
    browser_yrtisMajor = init_browser()
    url_yrtisMajor = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser_yrtisMajor.visit(url_yrtisMajor)
    html_yrtisMajor=browser_yrtisMajor.html
    soup_yrtisMajor = bsp(html_yrtisMajor, 'html.parser')
    url_yrtisMajor = (soup_yrtisMajor.find_all('div', class_='downloads')[0].li.a.get('href'))
    images_urls.append([{"title": "Syrtis Major Hemisphere", "img_url": url_yrtisMajor}])
    data_web['images_urls']=images_urls
    browser_yrtisMajor.quit()
    return data_web
        
def scpe_VallesMarineris():     
    browser_VallesMarineris = init_browser()
    url_VallesMarineris = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser_VallesMarineris.visit(url_VallesMarineris)
    html_VallesMarineris=browser_VallesMarineris.html
    soup_VallesMarineris = bsp(html_VallesMarineris, 'html.parser')
    url_VallesMarineris= (soup_VallesMarineris.find_all('div', class_='downloads')[0].li.a.get('href'))
    images_urls.append([{"title": "Valles Marineris Hemisphere", "img_url": url_VallesMarineris}])
    data_web['images_urls']=images_urls
    browser_VallesMarineris.quit()
    return data_web
