<template>
	<view>
		reviews
	</view>
</template>

<script>
	export default {
		data() {
			return {
				reviews: [],
				book: {},
			}
		},
		methods: {
			
		},
		onLoad(e) {
			console.log(e)
			uni.request({
				url:"http://47.102.212.210:5000/book/" + e.id,
				success: (res) => {
					this.reviews = res.data.data.items
					this.book = res.data.data.book
				}
			})
		}
	}
</script>

<style>

</style>
