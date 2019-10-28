from bs4 import BeautifulSoup

def read_file():
    file = open("intro_to_soup_html.html")
    data = file.read()
    file.close()
    return data


# make soup
# Syntax = BeautifulSoup(html_data, parser)
# our parser is lxml or html.parser

html_file = read_file()

soup = BeautifulSoup(html_file, 'lxml')

# soup prettify
print(soup.prettify())