import requests 
import uuid
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
import time


baceurl='https://www.overdrive.com'


headers= {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

booklinks= []
for x in range(1,2):
    url= 'https://www.overdrive.com/search?autoLibrary=t&autoRegion=f&f-formatClassification=Magazine&showAvailable=False&page={}'.format(x)
    r=requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    #print(r.encoding)
    
#### Grabe the Links in each card######
    body=soup.find('body')
    main=body.find('div', role='main')
    container=main.find('div', class_='title-result-row__details')
    
    #print(main.prettify())
   

    for title in main.find_all('h3', class_='title-result-row__title'):
        try:
            for link in title.find_all('a', href = True):
                try:
                    booklinks.append(baceurl + link['href'])
                    print(len(booklinks))
                except:
                    ""
        except:
            link =""

time.sleep(2)

csv_file = open('TableA.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ID', 'Title', 'Publisher', 'Manufacture', 'reviews'])

    
for link in booklinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    ID = uuid.uuid1()
    try:
        maainer = soup.find('div', role='main')
    except:
        maainer = ''
    try:    
        sec = maainer.find('div', class_='breadcrumbs-container header')
    except:
        sec = ''
    try:
        li1 = sec.find("li",({'class': "breadcrumbs__crumb"}))
    except:
        lil = ''
    try:
        li2 = li1.find_next_sibling("li",({'class': "breadcrumbs__crumb"}))
    except:
        li2 = ''

    try:
        con = maainer.find('div',({'class': "mobile-metadata-column"}))
    except:
        con = ''

    try:
        manu = con.find('div',({'class': "metadata_container"}))
    except:
        manu =''

    try:
        serie = manu.find_next_sibling('div',({'class': "metadata_container"}))
    except:
        serie =''
    try:
        share = serie.find_next_sibling('div',({'class': "metadata_container"}))
    except:
        share =''
   
    try:
        subjects = share.find_next_sibling('div',({'class': "metadata_container"}))
    except:
        subjects =''
    
    try:
        subjec = subjects.find_next_sibling('div',({'class': "metadata_container"}))
    except:
        subjec = ''

    try:
        dic = con.find('div',({'class': "metadata_container star-ratings"}))
    except:
        dic=''
    
    try:
        title = li2.find_next_sibling("li",({'class': "breadcrumbs__crumb"})).a.text
    except:
        title="NA"

    try:
        Publisher  = serie.find_next_sibling('div',({'class': "metadata_container"})).p.text
    except:
        Publisher="NA"

    try:
        form = con.find('div',({'class': "metadata_container"})).p.text
    except:
        form = 'NA'

    try:
        subject = subjec.find('a',({'class': "subject_link"})).text.strip()
    except:
        subject = 'none'

    Magazinee = {
        'ID': ID.hex,
        'Title': title,
        'Publisher': Publisher,
        'Format': form,
        'Subject': subject,
        }
   
    try:
        csv_writer.writerow([ID.hex ,title, Publisher, form, subject])
    except:
        ''
     
csv_file.close
    
   


   


 











   