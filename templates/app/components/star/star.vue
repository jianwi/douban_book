<template>
	<view class="uni-flex star-container">
		<text v-for="i in star_count">
			♥
		</text>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		props:['stars'],
		computed:{
			star_count(){
				console.log(this)
				return parseInt(this.stars)
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.star-container{
		align-items: center;
		color: red;
	}
</style>
