<template>
	<view>
		<view class="uni-flex uni-row uni-page-body" style="padding: 10upx;">
			<view class="uni-flex-item uni-center">
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
			<view style="margin: auto;margin-top: 30upx;margin-bottom: 35upx;border-radius: 10px;padding: 15upx;" class="title uni-center uni-padding-wrap uni-h4 uni-bg-blue">
				{{ message }}
			</view>
		</view>


		<view class="uni-flex uni-column">
			<view class="review-container uni-flex-item uni-padding-wrap" v-for="(review,index) in reviews" :key="index">
				<view class="avatar-container uni-flex">
					<image class="avatar" :src="review.avatar" mode="aspectFit"></image>
					<view class="uni-flex uni-column">
						<view class="uni-flex base-center uni-row">
							<text class="uni-h5">{{ review.author }}</text>
							<text style="margin: 5px;">
								<star stars='5'></star>
							</text>
						</view>
						<text class="review-title" @click="goReviewDetail" :data-code="review.code">
							{{ review.name }}
						</text>

					</view>

				</view>
				<view>
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
				reviews: [],
				book: {},
				message: '书评列表'
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
			console.log(e)
			uni.request({
				url: "http://47.102.212.210:5000/book/" + e.id,
				success: (res) => {
					this.reviews = res.data.data.items
					this.book = res.data.data.book
				}
			})
		},
		onReachBottom() {
			console.log('到底了')
			uni.request({
				url: ""
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
		padding-bottom: 5px;
		margin-bottom: 9px;
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
		font-size: 1.2em;
		font-weight: 800;
		color: #0069D9;
	}

	.base-center {
		display: flex;
		align-items: center;
	}
</style>
