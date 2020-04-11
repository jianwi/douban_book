<template>

	<view class="content">
		
		<view class="uni-form-item">
			<input type="text" class="uni-input bottom-border" placeholder="请输入书籍名称搜索" />
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
		</view>


		<view class="text-area">

		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				books: [{
					'name': 'xx'
				}]
			}
		},
		onLoad() {
			uni.request({
				url: 'http://47.102.212.210:5000/top250',
				success: (res) => {
					this.books = res.data.data
				}
			})
		},
		methods: {
			reviewsList(data){
				console.log(data)
				uni.navigateTo({
					url:'../reviews/reviews?id=' + data.currentTarget.dataset.subject
				})
			}

		}
	}
</script>

<style>
	.book-container {
		flex-wrap: wrap;
		padding: 20rpx;
	}

	.book {
		border: solid 1px #D1ECF1;
		margin: 1px;
	}

	image {
		margin: 1upx 1px;
		width: 300upx;
	}
</style>
