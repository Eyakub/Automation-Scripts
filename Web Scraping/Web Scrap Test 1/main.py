from mathematicians import simple_get
from bs4 import BeautifulSoup

# raw_html = open('mathematicians_html.html').read()
# raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')

# html = BeautifulSoup(raw_html, 'html.parser')
# for p in html.select('p'):
#     if p['id'] == 'walrus':
#         print(p.text)
# for i, li in enumerate(html.select('li')):
#     print(i+1, li.text)
def get_names():
    url = "http://www.fabpedigree.com/james/mathmen.htm"
    response = simple_get(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)
    raise Exception('Error retrieving contents at {}'.format(url))


def get_hits_on_name(name):
    url_root="https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/Henri_Poincar%C3%A9"
    response = simple_get(url_root.format(name))

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        hit_link = [a for a in html.select('a')
                    if a['href'].find('latest-60') > -1]
        if len(hit_link) > 0:
            # strip commas
            link_text = hit_link[0].text.replace(', ', '')
            try:
                # convert to integer
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))
            
    log_error('No pageviews found for {}'.format(name))
    return None


if __name__=='__main__':
    print('Getting the list of names...')
    names = get_names()
    print('...Done.\n')

    results = []
    print('Getting stats for each name...')
    for name in names:
        try:
            hits = get_hits_on_name(name)
            if hits is None:
                hits = -1
            results.append((hits, name))
        except:
            results.append((-1, name))
            log_error('Error encountered while processing {}, skipping'.format(name))
    print('...done\n')
    results.sort()
    results.reverse()

    if len(results) > 5:
        top_marks = results[:5]
    else:
        top_marks = results
    
    print('\nThe most popular mathematicians are: \n')
    for (mark, mathematician) in top_marks:
        print('{} with {} pageviews'.format(mathematician, mark))
    no_results = len([res for res in results if res[0] == -1])
    print('\nBut we did not find results for '
        '{} mathematicians on the list'.format(no_results)) 
   