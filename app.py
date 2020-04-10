from flask import Flask
from flask import jsonify
from crawl.search import Search
from crawl.book_top import BookTop
from crawl.reviews import Reviews

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/search/<book_name>')
def search(book_name):
    search = Search(book_name)
    return jsonify(search.make())


@app.route('/top250')
def top250():
    top250 = BookTop()
    return jsonify(top250.make())


@app.route('/top250/<start>')
def top250_goto(start):
    top250 = BookTop(start)
    return jsonify(top250.make())


@app.route('/book/<subject>')
def book_info(subject):
    book = Reviews(subject)
    return jsonify(book.make())


if __name__ == '__main__':
    app.run()
