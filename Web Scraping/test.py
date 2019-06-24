from bs4 import BeautifulSoup
import requests

url = "https://facebook.com"

# getting the webpage, creating a response object
response = requests.get(url)

# extracting the source code of the page
data = response.text

# passing the source code to Beautiful soup to create 
# beautiful soup object of it
soup = BeautifulSoup(data, 'html.parser')

# extracting all the <a> tags into a list
tags = soup.find_all('a')

# Extracting URLs from the attribute href in the <a>
for tag in tags:
    print(tag.get('href'))