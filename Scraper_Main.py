import Browser_Automation
import Store_Data
base_url = "https://www.google.com"
Search_Query = "pharmacy in 1008 Newyork"

Html_data = Browser_Automation.control_browser_and_get_html(base_url,Search_Query)
Store_Data.get_store_data(Html_data)
