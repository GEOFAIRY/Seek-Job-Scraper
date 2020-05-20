import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self):
        pass

    def run(self):
        print('Webscraper Started')
        self.getSite()

    def getSite(self):
        r = requests.get(
            'https://www.seek.co.nz/software-developer-jobs/in-Wellington-Central-Wellington?sortmode=ListedDate'
        )
        soup = BeautifulSoup(r.content)
        print(soup.prettify())
