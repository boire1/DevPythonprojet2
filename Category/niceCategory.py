import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from csv import writer

'''
pages=range(1,10)
for page in pages:
    response= requests.get('http://books.toscrape.com/catalogue/page-' + str(page) + '.html')

'''
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
            
            
            # basecat = "http://books.toscrape.com/catalogue/category/books"+cat_of_book+cat_of_index
            
            # get_url = requests.get(basecat)
            # soup2 = BeautifulSoup(get_url.text, 'html.parser')
            # for h3 in soup.find_all('h3'):
            #     for a in h3.find_all('a'):
            #         title_count = (a.get('title'))
            #         print(title_count)
            # for thing in soup2.find('h3'):
            #     print(thing)
            #   .contents[0] 
            
            # get_first_ul = soup2.find('ul', {"class": "nav-list"})
            
            # get_ul = get_first_ul.find('ul')
            
            # list_books_category = get_ul.find_all('li')
            # print(list_books_category )
    with open('niceCategory.csv', 'a', encoding='utf8', newline='') as cat_f_csv:
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
                       
                       
                    
        # category = soup.find('h1').get_text()
        
        # for li in list_books_category:
        #     category_name_in_link = li.find('a').contents[0]
        #     print(category_name_in_link)
        #    ('a').contents[0]
            
    """
            
            title = []
	for h3 in soup.find_all('h3'):
		for a in h3.find_all('a'):
			title_count = (a.get('title'))
			title.append(title_count)
            
        """
    '''
        category = soup.find('h1').get_text()
	print('\n' + 'Books in: ' + category + '\n')

        
        '''    
    
    # print(response)                  





            # cat_link_total = basecat2+category_name_in_link.replace("../", '')
            # soupcategorie=BeautifulSoup(cat_link_total,'html.parser')
            # find_title_cat=soupcategorie.find('a')['href']
            # print(find_title_cat)    
                
            
            
            
            # get_Url_Cat = requests.get(cat_link_total)
            
            # soup3 = BeautifulSoup(get_Url_Cat.text, 'html.parser')
            
            # soup_h1 = soup3.find("h1").text
            
            # for name in soup3.findAll("h3"):
            #     name_1=name.get_text().strip()
            #     name_str=str(name)
            
            # print(cat_link_total)
        