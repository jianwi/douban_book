from crawl.crawl_tools import CrawlTools
import re

class Reviews():

    def __init__(self,subject,start=0):
        self.url = 'https://book.douban.com/subject/'+ str(subject) +'/reviews?start=' + str(start)
        self.crawl = CrawlTools(self.url)
        self.items = []

    def make(self):
        for review in self.__review_list():
            item = {
                'code' : self.__code(review),
                'name' : self.__author(review),
                'avatar' : self.__avatar(review),
                'star' : self.__star(review),
                'name' : self.__name(review),
                'review_short' : self.__review_short(review)
            }
            self.items.append(item)
        print(self.items)

    def __review_list(self):
        return self.crawl.soup().select('div.review-list>div')

    def __avatar(self,review):
        return review.select('.main-hd a.avator img')[0]['src']

    def __author(self, review):
        return review.select('a.name')[0].get_text()

    def __star(self,review):
        star_class = review.select('a.name+span')[0]['class']
        star_class_str = "".join(star_class)
        return re.search(r'\d',star_class_str).group()

    def __name(self,review):
        return review.select('.main-bd h2 a')[0].get_text()

    def __review_short(self,review):
        return review.select('div.review-short div.short-content')[0].get_text()

    def __code(self,review):
        review_id = review.select('div.review-short')[0]['id']
        return re.search(r'\d+', review_id).group()



# t = Reviews(1007305,25)
# (t.make())