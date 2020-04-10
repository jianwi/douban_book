from crawl.crawl_tools import CrawlTools
import json

class Search():

    def __init__(self,keyword):
        self.url = 'https://book.douban.com/j/subject_suggest?q=' + str(keyword)
        self.crawl = CrawlTools(self.url)
        self.items = []

    def make(self):
        js = self.crawl.get()
        self.items = json.loads(js)
        return self.items



# t = Search('php')
# print(t.make()[0])