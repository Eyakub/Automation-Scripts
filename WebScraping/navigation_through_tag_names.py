from bs4 import BeautifulSoup

def read_file():
    file = open('three-sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

title = soup.title
body = soup.body
for child in body.contents:
    print(child if child is not None else '', end='\n\n\n\n')
