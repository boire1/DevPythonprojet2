from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv
from csv import writer
import os
import requests # to get image from the web
import shutil # to save it locally


# np.arange(1,10)

all_book=[]




pages=range(1,51)
for page in pages:
    response= requests.get('http://books.toscrape.com/catalogue/page-' + str(page) + '.html')
   
   
      
    # page = requests.get(url)
    soup= BeautifulSoup(response.text,"html.parser")

    # with open('Image.csv', 'w',encoding='utf8', newline='' ) as image_ff_csv:
    #     thewriter = csv.writer(image_ff_csv, delimiter=',')
    #     header=['Title ','Image Link']
        # thewriter.writerow(header)
        

        # get all book links

    links = []
        
    listings= soup.find_all(class_="product_pod")
    for listing in listings:
        book_link= listing.find("h3").a.get("href")
        base_url ="https://books.toscrape.com/catalogue/"
        base_url_image="https://books.toscrape.com/"
        complete_link = base_url + book_link
        links.append(complete_link)
        
    # extract info from each link
    for link in links:
        response = requests.get(link).text
        book_soup = BeautifulSoup(response,"html.parser")
        
        title = book_soup.find(class_="col-sm-6 product_main").h1.text.strip()
    
    
        
        
    
        
    
        #url_image= book_soup.find(class_="item active").find_next()
        link_image = book_soup.find("div", {"class": "item active"}).find("img")
        

        image_url = base_url_image + link_image['src'].replace("../", '')
        image_alt= base_url_image + link_image['alt'].replace("../", '')
        
        image_alt=image_alt[27:]
        
    
        


## Set up the image URL and filename

        filename = image_url.split("/")[-1]
        filename=filename[-4:]
        name_mg=image_alt
        filename=image_alt+filename
        
        
        
        r = requests.get(image_url, stream = True)
        # os.mkdir(os.path.join(os.getcwd(),courant))
        # write image
        #open(path + '/' + imgTitle, 'wb').write(imageBinary.content)
    
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            # os.chdir(os.mkdir(os.path.join(os.getcwd(),courant)))
            # Open a local file with wb ( write binary ) permission.
        try:    
            with open("Images/"+filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image telecharger avec sucess: ',filename)
        except:    
            
                print('Image ne peut être telecharger')    
                
        print(filename)        
                
                        
                
        
            
        book ={"Title":title,            
            "Image":image_url,
            }
        all_book.append(book)
        
        info=[title,image_url]
    
 


    
    
    
    
