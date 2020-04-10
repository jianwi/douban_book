import requests
from bs4 import BeautifulSoup


class CrawlTools():

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }

    def __init__(self, url):
        self.url = url

    def trim(self, text):
        return "".join(text.split())

    def get(self):
        res = requests.get(self.url, headers=self.headers)
        return res.text

    def soup(self):
        return BeautifulSoup(self.get(), 'html.parser')

    def __index__(self):
        return self.soup()

