from crawl.crawl_tools import CrawlTools
import re


class Review():
    def __init__(self,code):
        self.url = 'https://book.douban.com/review/' + str(code)
        self.crawl = CrawlTools(self.url).soup()

    def make(self):
        return self.__content()

    def __content(self):
        return str(self.crawl.select('div#link-report>div.review-content')[0])


t = Review(12425970)
print(t.make())