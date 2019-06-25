from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing

url = "http://www.fabpedigree.com/james/mathmen.htm"
response = simple_get