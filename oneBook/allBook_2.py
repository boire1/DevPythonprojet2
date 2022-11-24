# from bs4 import  BeautifulSoup
# import requests
# import re

# gpu = input("what product do you to search for ? ")

# url = f"https://www.newegg.ca/p/pl?d={gpu}&N=4131"
# page = requests.get(url)
# soup=BeautifulSoup(page.text,'html.parser')

# page_text = soup.find(class_="list-tool-pagination-text").strong
# pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

# for page in range (1, pages+1):
    
#     url = f"https://www.newegg.ca/p/pl?d={gpu}&N=4131&page={page}"
#     page = requests.get(url)
#     soup=BeautifulSoup(page.text,'html.parser') 
#     items = soup.find_all(text=re.compile(gpu))
#     for item in items:
#        parent=item.parent
#        if parent.name !="a":
#             #print(pages)
#             link = parent['href']
#             price=item.find_parent(class_="price-current").strong.string
#             next_parent=item.find_parent(class_="item-container").strong.string
#             print(price)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




# pages = [str(i) for i in range(1,4)] # de 1 a 51
# for page in pages:
#     response= requests.get(f'http://books.toscrape.com/catalogue/page-' + page + '.html')

#000000000000000000000000000000000000000000000000000000000000    



from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv
from csv import writer


# np.arange(1,10)

all_book=[]



links = []
books=[] 
pages=range(1,2)
for page in pages:
    response= requests.get('http://books.toscrape.com/catalogue/page-' + str(page) + '.html')
     


    soup= BeautifulSoup(response.text,"html.parser")
                                         



    listings= soup.find_all(class_="product_pod")
    for listing in listings:                                   
        book_link= listing.find("h3").a.get("href")
        base_url ="https://books.toscrape.com/catalogue/"
        base_url_image="https://books.toscrape.com/"
        complete_link = base_url + book_link
        links.append(complete_link)
        for l in links:
            liens=l    
          

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


for link in links:
    response = requests.get(link).text
    book_soup = BeautifulSoup(response,"html.parser")
    
    title = book_soup.find(class_="col-sm-6 product_main").h1.text.strip()

    price = book_soup.find(class_="col-sm-6 product_main").p.text.strip()[1:]
    
    stock = book_soup.find(class_="instock availability").text.strip()
    
    book_rating=book_soup.find("p", class_="star-rating").attrs.get("class")[1]
    
    description = book_soup.select('article > p')[0].text
    # product_description = book_soup.find("div", {"id": "product_description"}).find_next("p").get_text()
        
    category=book_soup.find('ul',class_="breadcrumb").find_next('a')
    
    
    categorie_1=category.find_next('a')
    categorie_ok=categorie_1.find_next('a')
    catego_book=categorie_ok.get_text().strip()
        
    
    

   
#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    # info=[title,catego_book]

    #url_image= book_soup.find(class_="item active").find_next()
    link_image = book_soup.find("div", {"class": "item active"}).find("img")
    # On établit l'url complète

    image_url = base_url_image + link_image['src'].replace("../", '')
    
    tableau_book=book_soup.find("table",{"class":"table table-striped"})
    
    tableau_book_clean=tableau_book.text
    
    tab_bk_UPC=(tableau_book.text[6:20] )

    
    # print(tableau_book_clean)
    

    bk_price_excl_tva=(tableau_book.text[62:68])
    bk_price_incl_tva=(tableau_book.text[89:95])

    

    tabl_book_avality=(tableau_book.text[132:150])
    
    tableau_reviews=(tableau_book_clean[167:180]).strip()

    
    # 

        
     
    info=[title,tab_bk_UPC,catego_book,price,
    tableau_reviews,stock,bk_price_excl_tva,bk_price_incl_tva,image_url,book_rating,description,l]
    books.append(info) 

# thewriter.writerow(info)


    

    with open('allBooks_2.csv', 'w',encoding='utf8', newline='' ) as ff_csv:
        thewriter = csv.writer(ff_csv, delimiter=',')
        header=['Title ','Num_Upc ','Category ','Price', 'Reviews', 'Available', '(Price exl tva)',
                '(Price inc tva)','Image Link','Rating ', 'Description','Link of the book']
        
        thewriter.writerow(header)
        thewriter.writerows(books)
    
      
# print(books)

    #     "N°Upc":tab_bk_UPC,
    #     "Category":catego_book,
    #     "Price":price,
    #     "Reviews":tableau_reviews,
    #     "Available":stock,
    #     "(Price exl tva)":bk_price_excl_tva,
    #     "(Price inc tva)":bk_price_incl_tva,
    #     "Image":image_url,
    #     "Rating":book_rating,
    #     }
    
    # all_book.append(book)
     