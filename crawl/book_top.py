from crawl.crawl_tools import CrawlTools
import re

class BookTop:

    def __init__(self,start=0):
        self.url = 'https://book.douban.com/top250?start=' + str(start)

        self.crawl = CrawlTools(self.url)
        self.items = []

    def make(self):
        for table in self.__tables():
           item = {
               'book' : self.__book_name(table),
               'link' : self.__link(table),
               'subject' : self.__subject(table),
               'author' : self.__author(table),
               'pic' : self.__pic(table),
               'rating_num': self.__rating_num(table)

           }
            # 添加到 items 里
           self.items.append(item)
        return self.items

    def items(self):
        return self.items

    def __tables(self):
        return self.crawl.soup().select('.indent table')

    def __book_name(self,table):
        return table.select('.pl2 a')[0]['title']

    def __author(self,table):
        return self.crawl.trim(table.select('.pl')[0].get_text())

    def __link(self,table):
        return table.select(".pl2 a")[0]['href']

    def __subject(self,table):
        link = self.__link(table)
        return re.search(r'(?<=/subject/)\d+', link).group()

    def __pic(self,table):
        return table.select("td a img")[0]['src']

    def __rating_num(self,table):
       return table.select("span.rating_nums")[0].get_text()

# t = BookTop()
# print(t.make())