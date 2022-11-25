import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from csv import writer


pages=range(1,51)
for page in pages:

    # url=f"http://books.toscrape.com/catalogue/page-"+str(page)+".html"

    response= requests.get('http://books.toscrape.com/catalogue/page-' + str(page) + '.html')

    soup=BeautifulSoup(response.text,'html.parser')


    links = []

    listings = soup.find_all(class_="product_pod")
    for listing in listings:
        book_link = listing.find("h3").a.get("href")
        # print(book_link)
        base_url = "https://books.toscrape.com/catalogue/"
        base_url_image = "https://books.toscrape.com/"
        complete_link = base_url + book_link
        links.append(complete_link)
        # print(complete_link)
        
    # extract info from each link  extraction des données [titre,prix, stock etc... ]
        for link in links:
            response = requests.get(link).text
            book_soup = BeautifulSoup(response, "html.parser")

            title = book_soup.find(class_="col-sm-6 product_main").h1.text.strip()
            # print(title)
            category = book_soup.find('ul', class_="breadcrumb").find_next('a')
            categorie_1 = category.find_next('a')
            categorie_ok = categorie_1.find_next('a')
            cat = categorie_ok['href']
            cat = cat.replace("../", '')
            cat_of_index = cat[-10:]
            cat_of_book = cat[14:-10]
            catego_book = categorie_ok.get_text().strip()
            
          
    with open('niceCategory2.csv', 'a', encoding='utf8', newline='') as cat_f_csv:
            thewriter = csv.writer(cat_f_csv, delimiter=',')
            header = ['Title ', 'Category']
            thewriter.writerow(header)
            
            
            
            basecat2 = "https://books.toscrape.com/catalogue/category/books/"
            for h3 in book_soup.find_all('h3'):
                for a in h3.find_all('a'):
                    title_count = (a.get('title'))
                    
                    pinfo=[title_count,catego_book]
                    df=pd.DataFrame(data=pinfo) 
                    
                    thewriter.writerow(pinfo) 
                       
                       
        
    
    
   