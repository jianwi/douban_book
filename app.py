from flask import Flask
from flask import jsonify
from crawl.search import Search
from crawl.book_top import BookTop
from crawl.reviews import Reviews
from crawl.review import Review
# 同源策略
from flask_cors import CORS

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/search/<book_name>')
def search(book_name):
    search = Search(book_name)
    return resp(search.make())


@app.route('/top250')
def top250():
    top250 = BookTop()
    return resp(top250.make())


@app.route('/top250/<start>')
def top250_goto(start):
    top250 = BookTop(start)
    return resp(top250.make())


@app.route('/book/<subject>')
def book_info(subject):
    book = Reviews(subject)
    return resp(book.make())


@app.route('/review/<code>')
def review(code):
    review = Review(code)
    return resp(review.make())


def resp(data):
    return jsonify({
        'code': 200,
        'message': 'success',
        'data': data
    })


if __name__ == '__main__':
    app.run()

# 同源策略
CORS(app, resources={r"/*": {"origins": "*"}})
