from bs4 import BeautifulSoup
import requests
import csv


URL = "https://learntocodetogether.com/top-150-leetcodes-best-practice-problems/"


def scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    with open('leetcode_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['h2', 'url', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        divs = soup.find_all("div", class_="entry-content")

        for div in divs:
            h2_tags = div.find_all('h2')
            for h2 in h2_tags:

                li_tags = h2.find_next_sibling('ol').find_all('li')
                for li in li_tags:
                    url = li.find('a')['href']
                    name = li.find('strong').text

                    writer.writerow({'h2': h2.text, 'url': url, 'name': name})


scrap(url=URL)
