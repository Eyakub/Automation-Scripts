from bs4 import BeautifulSoup

def read_file():
    file = open('three-sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

# .contents
body = soup.body
children = [child for child in body.contents if child != '\n' ]
# print (children)

# .descendants -- returns us all the children of the said tag
for index, child in enumerate(soup.head.descendants):
    print(index)
    print(child if child != '\n' else '')
