import requests
from bs4 import BeautifulSoup
url = "Google.com"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

# soup =  BeautifulSoup(resposne.text,"lxml")