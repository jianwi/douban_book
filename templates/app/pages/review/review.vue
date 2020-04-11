<template>
	<view>
		<!-- 书信息  -->
		<view></view>
		<!-- 作者信息 -->
		<view></view>
		<!-- 书评内容 -->
		<view class="review-content">
			<view class="uni-h3 uni-center">{{ title }}</view>
			
			<view class="uni-flex uni-row avatar-container">
				<image :src="author.avatar" class="avatar" mode="aspectFit"></image>
				<text class="uni-h5">{{ author.name }}</text>
				
				<text class="uni-h5" style="margin-left: 20upx;">评《{{ book.name }}》</text>
			</view>
			
			<rich-text class="review-content" :nodes="review"></rich-text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				book: {},
				review: '',
				title: '',
				author: {}
			}
		},
		methods: {

		},
		onLoad(e) {
			console.log(e)
			uni.request({
				url: "http://47.102.212.210:5000/review/" + e.code,
				success: (res) => {
					this.review = res.data.data.content
					this.book = res.data.data.book
					this.author = res.data.data.author
					this.title = res.data.data.title
				}
			})
		}
	}
</script>

<style>
	.review-content {
		padding: 15upx;
	}
	.avatar {
		width: 28px;
		height: 28px;
		border-radius: 14px;
		margin-right: 14px;
	}
	
	.avatar-container {
		padding: 3px;
		align-items: center;
		justify-content: center;
		margin-top: 18upx;
		margin-bottom: 15upx;
	}
</style>
