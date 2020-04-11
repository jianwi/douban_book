from crawl.crawl_tools import CrawlTools
import re


class Review():
    def __init__(self,code):
        self.url = 'https://book.douban.com/review/' + str(code)
        self.crawl = CrawlTools(self.url).soup()

    def make(self):

        return {
            'title': self.__title(),
            'content': self.__content(),
            'book': self.__book()
        }

    def __content(self):
        return str(self.crawl.select('div#link-report>div.review-content')[0])

    def __title(self):
        return self.crawl.select('div.article>h1>span')[0].get_text()

    def __book(self):
        aside = self.crawl.select('div.sidebar-info-wrapper')[0]
        book_info_list = aside.select('div.subject-info ul.info-list li.info-item')

        name = aside.select('div.subject-title a')[0].get_text()
        pic = aside.select('div.subject-img a img')[0]['src']
        author = book_info_list[0].select('span.info-item-val')[0].get_text()
        publisher = book_info_list[1].select('span.info-item-val')[0].get_text()
        prize = book_info_list[2].select('span.info-item-val')[0].get_text()
        pages = book_info_list[4].select('span.info-item-val')[0].get_text()
        date = book_info_list[5].select('span.info-item-val')[0].get_text()

        return {
            'name': name,
            'pic': pic,
            'author': author,
            'publish': publisher,
            'prize': prize,
            'pages': pages,
            'date': date
        }


# t = Review(12425970)
# print(t.make())