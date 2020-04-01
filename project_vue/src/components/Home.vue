<template>
	<div>
		<h1>Авторизация</h1>
		<button @click='gologin'>Вход</button>
	</div>
</template>

<script>
	export default {
		name: 'Home',
		methods: {
			gologin(){
				this.$router.push({name:'login'})
			},
		},
	}
</script>

<style scoped>
</style>
