from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time, json

STARTUP_DELAY= 5
NEXT_PAGE_DELAY= 5
WAIT_AFTER_ELEMENTS_LOADED= 2
DELAY_TO_CHECK_IF_NEW_ELEMENT_IS_VISIBLE= 1
LOAD_SPECIFIC_RESULT_DELAY= 4
BACK_TO_MAIN_LIST_DELAY= 3

def control_browser_and_get_html(base_url,Search_Query):

    """
    This function is responsible for browser automation and also, to call the "getExtractedData" function
    The output of this function will give a list of html, which are processed by the other function "get_store_data"
    in file Store_Data.....    
    """
    
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.find_element(By.XPATH, '//input[@class="gLFyf"]').send_keys(Search_Query)
    driver.find_element(By.XPATH, '//input[@class="gLFyf"]').send_keys(Keys.ENTER)
    time.sleep(WAIT_AFTER_ELEMENTS_LOADED)
    driver.find_element(By.XPATH, '//a[@class="tiS4rf Q2MMlc"]').click()
    time.sleep(WAIT_AFTER_ELEMENTS_LOADED)
    LIST_HTML = getExtractedData(driver, driver.current_url)

    return LIST_HTML

def getExtractedData(driver, url):
    more_page= True
    time.sleep(WAIT_AFTER_ELEMENTS_LOADED)

    list_html = []
    while more_page:
        
        time.sleep(NEXT_PAGE_DELAY)

        html= driver.page_source
        soup= BeautifulSoup(html, 'html.parser')

        time.sleep(WAIT_AFTER_ELEMENTS_LOADED)

        number_of_search= soup.find('div', attrs={'class': 'rlfl__tls rl_tls'}).find_all('div', attrs={'jscontroller': 'AtSb'})
        print("Number of Result: {}".format(len(number_of_search)))

        for search in number_of_search:
            print(search.get('id'))

            time.sleep(WAIT_AFTER_ELEMENTS_LOADED)

            tab= search.get('id')

            try:
                driver.find_element(By.ID, str(tab)).click()

            except NoSuchElementException:
                print("Not able to locate the element")
            
            time.sleep(WAIT_AFTER_ELEMENTS_LOADED)

            html= driver.page_source

            soup= BeautifulSoup(html, "html.parser")

            details_tab = soup.find('div', attrs= {"class": "xpdopen"})
            list_html.append(details_tab)
            #get_store_data(details_tab)
            #return storeDetails
            #print(storeDetails)

        next_btn= soup.find('a', attrs={"id": 'pnnext'})
        if next_btn is not None:
            more_page= True
            driver.find_element(By.ID, 'pnnext').click()
        else:
            print("End of Results")
            more_page= False

    return list_html