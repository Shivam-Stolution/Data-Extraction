from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import threading

class DataFeed:

    STARTUP_DELAY= 5
    WAIT_FOR_LOAD= 2

    def __init__(self, query):
        self.query= query
        t= threading.Thread(target= self.start_now)
        t.start()
    
    def start_now(self):
        with sync_playwright() as sp:
            browser= sp.firefox.launch()
            page= browser.new_page()
            page.goto('https://www.google.com')
            page.query_selector("//input[@class='gLFyf']").fill("Taco Bell in  11100 New Jersey USA")
            page.keyboard.press("Enter")
            page.get_by_text("More Locations").click()
            page.wait_for_selector('div[class= "yf"]')
            self.startScraping(page)
    
    def get_store_data(self, page):
        soup = page.inner_html('div[class="main"]')
        html = BeautifulSoup(soup, 'html.parser')

        HOURS = []
        # Name_of_the_store = soup.find('div', attrs={'class': "SPZz6b"}).get_text()
        # Address = soup.find('span', attrs={'class': "LrzXr"}).get_text()
        # #print("Name of Resturant: {} and Address: {}".format(name, address))
        
        try:
            Name_of_the_store = html.find('div',class_= "SPZz6b").text

        except AttributeError:
            Name_of_the_store = "NA"
        #rating of the store

        try:
            Rating = html.find('span',class_ ="yi40Hd YrbPuc").text

        except AttributeError:
            Rating = 'NA'
        #Store-Type

        try:
            Store_type = html.find('div',class_="zloOqf kpS1Ac vk_gy").text 

        except AttributeError:
            Store_type = "NA"

        # Description of the Store
        try:
            Description_store =  html.find('div',class_="ElGe3c").text

        except AttributeError:
            Description_store = 'NA'
        # Address
        try:
            Address = html.find('span',class_="LrzXr").text

        except AttributeError:
            Address = "NA"
        # location url on google-maps
        try: 
            Location = html.find('div',class_ ="wDYxhc NFQFxe").a['href']

        except:
            Location = 'NA'
        # Phone Number
        try :
            Phone_number = html.find('span',class_ = "LrzXr zdqRlf kno-fv").span.text

        except AttributeError:
            Phone_number = "NA"
        # Hours of the store
        try:
            hours = []
            hour_data_L1 = html.find('div',{"jscontroller": "ncqIyf"})
            hours_data = hour_data_L1.find('table',class_= "WgFkxc CLtZU")
            table_hours = hours_data.find_all('tr')
            for days in table_hours:
                hours.append(days.text)
            HOURS.append(hours)

        except AttributeError:
            hours = []
            HOURS.append('NA')


        # Store details in dict.
        Store_details = {"Name_of_the_store":Name_of_the_store,
                "Rating": Rating,
            "Store_type":Store_type,
            "Description_store":Description_store,
                        "Address":Address,
                        "Location":Location,
                        "Phone_number":Phone_number,
                        "hours":HOURS
                        }
        
        print(Store_details)
        page.click('div[class="QU77pf"]')


    def startScraping(self, page):
        page.query_selector("//input[@class='gLFyf']").fill(self.query)
        page.keyboard.press("Enter")
        more_page= True
        COUNT= 0
        #while more_page:
        for i in range(0,1):
            time.sleep(self.STARTUP_DELAY)
            page.wait_for_selector('div[class= "yf"]')
            html= page.inner_html('div.rlfl__tls.rl_tls')
            soup= BeautifulSoup(html, 'html.parser')
            search_list= soup.find_all('div', attrs= {'jscontroller': 'AtSb'})
            for search in search_list:
                COUNT = COUNT + 1
                try:
                    time.sleep(self.WAIT_FOR_LOAD)
                    rest_id= search.get('id')
                    # print("Query {} and ID: {}".format(self.query, rest_id))
                    page.click('div[id= {}]'.format(rest_id))
                    page.wait_for_selector('div[class="QU77pf"]')
                    self.get_store_data(page)
                except:
                    print("Waiting Error")
            try:
                more_page= True
                page.click('a[id="pnnext"]')
            except:
                print("Number of Stores Scrapped of Query({}): {}".format(COUNT, self.query))
                more_page= False



query_list= ["7-Eleven in New Jersey USA", "Dunkin Donuts in New Jersey USA", "McDonal's in New Jersey USA", "Burger King in New Jersey USA"]
# i=0
# while i< len(query_list):
#     DataFeed(query_list[i])
#     i = i + 1

DataFeed(query_list[1])
DataFeed(query_list[2])
