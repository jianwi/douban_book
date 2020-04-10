from crawl.crawl_tools import CrawlTools


class BookTop:

    def __init__(self):
        self.url = 'https://book.douban.com/top250'

        self.crawl = CrawlTools(self.url)
        self.items = []

    def make(self):
        for table in self.__tables():
           item = {
               'book' : self.__author(table),
               'link' : self.__link(table),
               'author' : self.__author(table),
               'pic' : self.__pic(table)
           }

            # 添加到 items 里
           self.items.append(item)
        return self.items

    def __getInfo(self):
        return self.items

    def __tables(self):
        return self.crawl.soup().select('.indent table')

    def __book_name(self,table):
        return table.select('.pl2 a')[0]['title']

    def __author(self,table):
        return self.crawl.trim(table.select('.pl')[0].get_text())

    def __link(self,table):
        return table.select(".pl2 a")[0]['href']

    def __pic(self,table):
        return table.select("td a img")[0]['src']