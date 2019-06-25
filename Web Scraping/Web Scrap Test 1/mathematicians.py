from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    attemps to get the content at 'url' by making
    an HTTP GET request. if the content-type of response is 
    some kind of html/xml return the text content, 
    otherwise return none
    """
    """
    (CLOSING()) function ensures that any network 
    resources are freed when they go out of scope in that
    with block. Using lcosing() like that is good practice
    and helps to prevent fatal erros and network timeouts
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

    
def is_good_response(resp):
    """
    returns True if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
    and content_type is not None
    and content_type.find('html') > -1)


def log_error(e):
    """
    It iss always a good idea to log erros.
    this function just prints them, but you can make it do anything
    """
    print(e)


