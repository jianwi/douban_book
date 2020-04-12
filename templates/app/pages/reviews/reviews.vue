<template>
	<view>
		<view v-show="book" class="uni-flex uni-row uni-page-body" style="padding: 10upx;">
			<view v-show="book" class="uni-flex-item uni-center">
				<image class="book_pic" :src="book.pic" mode="aspectFit"></image>
			</view>

			<view class="uni-flex-item uni-column uni-flex  uni-container" style="padding-top: 12upx;">
				<text class="uni-h3">{{ book.name }}</text>
				<text class="uni-h5">{{ book.author }}</text>
				<text class="uni-h5">{{ book.publish }}</text>
				<text class="uni-h5">价格： {{ book.prize }}</text>
				<text class="uni-h5">页数：{{ book.pages }}</text>
				<text class="uni-h5">出版时间: {{ book.date }}</text>
			</view>
		</view>
		
		<view class="uni-center">
			<view style="margin: auto;margin-top: 30upx;margin-bottom: 35upx;border-radius: 10px;padding: 15upx;" class="title uni-center uni-padding-wrap uni-h4 bg-gray">
				{{ message }}
			</view>
		</view>


		<view v-show="reviews" class="uni-flex uni-column">
			<view class="review-container uni-flex-item uni-padding-wrap" v-for="(review,index) in reviews" :key="index">
				<view class="avatar-container uni-flex">
					<image class="avatar" :src="review.avatar" mode="aspectFit"></image>
					<view class="uni-flex uni-column">
						<view class="uni-flex base-center uni-row">
							<text class="uni-h5" style="margin-left: 30upx;font-size: 1.3em;">{{ review.author }}</text>
							<text style="margin: 35upx;">
								<star stars='5'></star>
							</text>
						</view>
					</view>
				</view>
				<view>
					<view class="review-title" @click="goReviewDetail" :data-code="review.code">
						{{ review.name }}
					</view>
					{{ review.review_short }}
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import star from '../../components/star/star.vue'
	export default {
		data() {
			return {
				reviews: null,
				book: null,
				message: '书评列表',
				subject:'',
				start: 0,
				hasMore: true,
			}
		},
		components: {
			star
		},
		methods: {
			goReviewDetail(e) {
				console.log(e)
				var code = e.currentTarget.dataset.code

				uni.navigateTo({
					url: '../review/review?code=' + code
				})
			}
		},
		onLoad(e) {

			this.subject = e.id
			uni.showLoading({
				title:"加载中，请稍后"
			})
			uni.request({
				url: "http://47.102.212.210:5000/book/" + e.id,
				success: (res) => {
					if(res.statusCode == 500) {
				
						uni.showToast({
							icon:'none',
							title:"抱歉！此书还没有书评",						
						})
					}
					this.reviews = res.data.data.items
					this.book = res.data.data.book
					uni.hideLoading()
				},
				fail() {
					this.message = '此书没有书评'
				}
			})
		},
		onReachBottom() {
			console.log('到底了')
			if(!this.hasMore) return
			uni.showLoading({
				title:'正在拼命加载中...'
			})
			this.start += 20
			uni.request({
				url:  "http://47.102.212.210:5000/book/" + this.subject +'/' + this.start,
				success: (res) => {
					if(res.statusCode == 500) {
						this.hasMore = false
						uni.showToast({
							icon:'none',
							title:"抱歉！没有更多书评了",						
						})
					}
					this.reviews = this.reviews.concat(res.data.data.items)
					uni.hideLoading()
				}
			})
		}
	}
</script>

<style>
	.book_pic {
		width: 255upx;
		height: 355upx;
		margin: 2px;
	}

	.review-container {
		border-bottom: 2px #9FCDFF dashed;
		padding-bottom: 25upx;
		margin-bottom: 35upx;
	}

	.avatar {
		width: 60px;
		height: 60px;
		border-radius: 30px;
		margin-right: 10px;
	}

	.avatar-container {
		padding: 3px;
		align-items: center;
	}

	.review-title {
		font-size: 1.3em;
		font-weight: 800;
		color: #000000;
	}

	.base-center {
		display: flex;
		align-items: center;
	}
	.bg-gray{
		background-color: #d5df07;
		color: white;
	}
</style>
