<template>
	<view class="content">
		<view class="uni-form-item">
			<input type="text" @confirm="searchBook" class="uni-input bottom-border" placeholder="请输入书籍名称搜索" />
		</view>

		<view class="title uni-center uni-padding-wrap uni-h4 uni-bg-blue">
			{{ message }}
		</view>

		<view class="uni-flex flex-row book-container uni-center">
			<view class="uni-flex-item" v-for="(book,index) of books" :data-subject="book.subject" @click="reviewsList">
				<view class="book">
					<view>
						<image mode="aspectFit" :src="book.pic"></image>
					</view>
					<view>
						<text class="uni-h4">{{ book.book }}</text>
					</view>
					<view>
						评分 ：<text>{{ book.rating_num }}</text>
					</view>
					<view>
						<text class="uni-h5">{{ book.author }}</text>
					</view>
				</view>
			</view>
			<view v-show="!search_book" class="book uni-flex-item uni-padding-wrap">
				加载中。。。请稍后
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				books: [],
				start: 0,
				message: '豆瓣读书 Top 250',
				search_book: false,
			}
		},
		onLoad() {
			this.loadBooks()
		},
		onReachBottom() {
			console.log('触底')
			if (this.search_book) return
			this.start += 25
			uni.request({
				url: 'http://47.102.212.210:5000/top250/' + this.start,
				success: (res) => {
					this.books = this.books.concat(res.data.data)
				}
			})
		},
		methods: {
			loadBooks() {
				uni.request({
					url: 'http://47.102.212.210:5000/top250',
					success: (res) => {
						this.books = res.data.data
					}
				})
			},
			reviewsList(data) {
				console.log(data)
				uni.navigateTo({
					url: '../reviews/reviews?id=' + data.currentTarget.dataset.subject
				})
			},
			searchBook(data) {
				var value = data.target.value
				if (value == "") {
					this.start = 0
					this.books = []
					this.message = '豆瓣读书 Top 250'
					this.search_book = false
					this.loadBooks()
					return
				}
				// console.log(data)
				this.message = '搜索结果'
				this.search_book = true
				uni.request({
					url: 'http://47.102.212.210:5000/search/' + value,
					success: (res) => {
						this.books = res.data.data
						if(this.books.length == 0){
							this.message = "没有搜索到任何结果。。。"
						}
					},
					fail() {
						this.message = '发生了错误，请稍后再试'
					}
				})
			}

		}
	}
</script>

<style>
	input {
		border: #20C997 solid 1px;
		margin: 20rpx;
	}

	.book-container {
		flex-wrap: wrap;
		padding: 20rpx;
	}

	.book {
		border: solid 1px #D1ECF1;
		margin: 1px;
		min-height: 50upx;
	}

	image {
		margin: 1upx 1px;
		width: 300upx;
	}

	.title {
		margin: 10rpx;
		padding: 15rpx;
		border-radius: 10px;
	}
</style>
