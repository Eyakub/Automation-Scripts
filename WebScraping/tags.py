from bs4 import BeautifulSoup

def read_file():
    file = open("tags_html.html")
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')


# accessing tag
meta = soup.meta


# tag methods
'''
name 
-- attributes
.get() method
dictionary
'''

# modify attributes
body = soup.body
body['style'] = "some style"
print(body['style'])
print(body['class'])