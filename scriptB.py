from requests_html import HTMLSession 
import requests
from uuid import uuid4
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
import time
import sys



booklinks= []
baceurl = 'https://www.amazon.com/'
headers= {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


for x in range (1,200):
   url= (f'https://www.amazon.com/s?i=magazines&rh=n%3A599858&fs=true&page={x}&qid=1614191749&ref=sr_pg_2')
   r=requests.get('http://localhost:8000/render.html', params = {'url':url, 'wait':3})
   soup = BeautifulSoup(r.content, 'html.parser')
   try:
      card = soup.find('div', class_="s-main-slot s-result-list s-search-results sg-row")
   except:
      pass
  

   try:
      sell = card.find ('div', class_='sg-col-4-of-12 sg-col-4-of-16 sg-col sg-col-4-of-20')
   except:
      pass
   try:   
      for sell in card.find_all('span', ({'class':'rush-component'})):
         try:
            for link in sell.find_all('a', href = True):
               try:
                  booklinks.append(baceurl + link['href'])
                  print(len(booklinks))
     
               except:
                  pass

                   
         except:
            pass
         
   except: 
      pass    


  



csv_file = open('TableB.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ID', 'Title', 'Publisher', 'Format', 'Subject','reviews'])
     

   
for link in booklinks:
    url=link
    r=requests.get('http://localhost:8000/render.html', params = {'url':url, 'wait':3})
    soup = BeautifulSoup(r.content, 'html.parser')
    ID = str(uuid4())
    
    try:
      page = soup.find('div', ({'id':'centerCol'}))
    except:
       page =''


    try:
      Div = page.find('div', ({'id':'titleSection'}))
    except:
       Div= ''


    
    try:
       div= page.find('div', ({'id': 'titleSection'}))
    except:
       div=''



    try:
      h1= div.find('h1', ({'id': 'title'}))
    except:
       h1 =''


    try:
       rev=page.find('div',({'id':'averageCustomerReviews'}))
    except:
       rev=''


    try:
       form=h1.find('span', ({'class':'a-size-medium a-color-secondary'}))
    except:
       form =''


    try:
       test =soup.find('div',({'id':'detailBulletsWrapper_feature_div'}))
    except:
       test=''


    try:
      sub = test.find('ul',({'class':'a-unordered-list a-nostyle a-vertical zg_hrsr'}))
    except:
       sub=''


    
    try:   
      subj = sub.find('li').span
    except:
      subj = ''

    
    try:
        Title= str (form.previousSibling).strip()
    except:
       Title = 'NA'

    try:
       publisher= Div.find('span',({'class':'author notFaded'})).a.text

    except:
      publisher = 'NA'
    
    try:
       forme=h1.find('span', ({'class':'a-size-medium a-color-secondary'})).text
    except:
       forme ='NA'
   
    try:
       subject =subj.find('a').text.strip()
    except:
       subject = 'NA'
    try:
      reviews = rev.find('a',{'id': 'acrCustomerReviewLink'}).text.strip()
    except:
       reviews ='NA'  
    
    Magazinee = {
        'ID': ID,
        'Title': Title,
        'Publisher': publisher,
        'Format': forme,
        'Subject': subject,
        'reviews': reviews
        }
   
    try:
      csv_writer.writerow([ID ,Title, publisher, forme, subject, reviews])
    except:
       pass
     
csv_file.close
