def get_store_data(COMBINED_HTML):

    Name_of_the_store =[]
    Rating =[]
    Store_type =[]
    Description_store = []
    Address =[]
    Location =[]
    Phone_number= []
    Summary_of_store = []
    #HOURS = []
    
    for html in COMBINED_HTML:
    
    # name of the store
        try:
            Name_of_the_store.append(html.find('div',class_= "SPZz6b").text)

        except AttributeError:
            Name_of_the_store.append('NA')

        #rating of the store
        try:
            Rating.append(html.find('span',class_ ="yi40Hd YrbPuc").text)

        except AttributeError:
            Rating.append('NA')
        #Store-Type

        try:
            Store_type.append(html.find('div',class_="zloOqf kpS1Ac vk_gy").text)

        except AttributeError:
            Store_type.append('NA')
        # Description of the Store
        try:
            Description_store.append(html.find('div',class_="ElGe3c").text)

        except AttributeError:
            Description_store.append('NA')
        # Address
        try:
            Address.append(html.find('span',class_="LrzXr").text)

        except AttributeError:
            Address.append('NA')
        # location url on google-maps
        try: 
            Location.append(html.find('div',class_ ="wDYxhc NFQFxe").a['href'])

        except:
            Location.append('NA')
        # Phone Number
        try :
            Phone_number.append(html.find('span',class_ = "LrzXr zdqRlf kno-fv").span.text)

        except AttributeError:
            Phone_number.append('NA')
        # Hours of the store
#         try:
#             hours = []
#             hour_data_L1 = html.find('div',{"jscontroller": "ncqIyf"})
#             hours_data = hour_data_L1.find('table',class_= "WgFkxc CLtZU")
#             table_hours = hours_data.find_all('tr')
#             for days in table_hours:
#                 hours.append(days.text)
#             HOURS.append(hours)

#         except AttributeError:
#             hours = []
#             hours.append('NA')

        # Review of the store.....
#         try:
#             Review = html.find('div',class_ ="nNlnIb")
#             all_reviews = Review.find_all('div')
#             Reviews = []
#             for review in all_reviews:
#                 review_text = review.text
#                 if review_text != None and review_text not in Reviews and review_text!='More Google reviews':
#                     Reviews.append(review_text)
#         except AttributeError:
#             Reviews = []
#             Reviews.append("NA")
        # Summary from the resraunts
        try:
            Summary_of_store.append(html.find("div", {"jscontroller": "EqEl2e"}).text)
        except AttributeError:
            Summary_of_store.append('NA')

        # Menu offered by the store
#         try:
#             Menu_item = html.find('div',class_ = "JZUrec").find_all('div',class_ = "gq9CCd")
#             #list to store the menu of the store..
#             Menu_of_store = []
#             for i in range(0,len(Menu_item)): 
#                 Menu_of_store.append(Menu_item[i].text)

#         except AttributeError:
#             Menu_of_store = []
#             Menu_item= None

        # Store details in dict.
    Store_details = {"Name_of_the_store":Name_of_the_store,
             "Rating": Rating,
            "Store_type":Store_type,
           "Description_store":Description_store,
                     "Address":Address,
                     "Location":Location,
                     "Phone_number":Phone_number,
# #                      "hours":hours,
# #                      "Reviews":Reviews,
#                      "Service_option" : "XX",
# #                          "Menu_of_store":Menu_of_store,
#                      "Summary_of_store":Summary_of_store
           }
    Data_store = pd.DataFrame(Store_details)
    return Data_store