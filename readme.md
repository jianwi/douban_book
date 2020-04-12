# 豆瓣书评爬虫项目
## 目录/文件说明
crawl目录为爬虫目录
	book_top.py 爬取 豆瓣读书top250
	review.py 爬取书评信息
	reviews.py 爬取书评列表
	search.py 图书搜索
	crawl_tools.py 封装的爬虫工具类

templates 目录为前端文件
	app 是 uniapp 应用 ，使用 Hbuilderx 即可发布为手机app
	
app.py 是 flask 启动文件，在这个文件里定义了api路由

## 使用
### 确保你已经安装了以下包
	flask, requests, bs4, flask_cors
	
	可以根据报错提示安装缺少的包

### 安装
```shell
git clone https://github.com/jianwi/douban_book.git
python -m flask run host=0.0.0.0
	
```

运行完成后访问 ,你的服务器ip地址:5000 看到hello world,运行成功


	
### 路由说明
1. /search/书名  --- 搜索书
2. /top250  --- 豆瓣读书前250排行榜
3. /top250/start  --- 分页s,tart 是从第多少个开始
4. /book/subject  ---  书评列表,subject 从以上接口中获取
5. /book/subject/start  --- 书评列表分页 ,start 同 3
6. /review/code  ---  书评详细信息，code 从 5 中获取


