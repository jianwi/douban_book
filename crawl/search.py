from crawl.crawl_tools import CrawlTools
import json


class Search:

    def __init__(self,keyword):
        self.url = 'https://book.douban.com/j/subject_suggest?q=' + str(keyword)
        self.crawl = CrawlTools(self.url)
        self.items = []

    def make(self):
        books = json.loads(self.crawl.get())
        items = []
        for book in books:

            if book['type'] == 'a':
                continue

            items.append({
                'book': book['title'],
                'subject': book['id'],
                'pic': book['pic'],
                'link': book['url'],
                'author': book['author_name']
            })
        self.items = items
        return self.items



# t = Search('php')
# print(t.make())