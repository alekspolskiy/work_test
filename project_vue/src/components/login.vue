<template>
	<div>
		<input v-model='login' type='text' placeholder='Логин'/>
		<input v-model='password' type='password' placeholder='Пароль'/>
		<button @click='setlogin'>Войти</button>
	</div>
</template>

<script>
	import $ from 'jquery'

	export default {
		name: 'login',
		data(){
			return{
				login: '',
				password: '',
			}
		},
		methods: {
			setlogin(){
				$.ajax({
					url: 'http://127.0.0.1:8000/api/v1/auth_token/token/login/',
					type: 'POST',
					data: {
						username: this.login,
						password: this.password
					},

					success: (response) => {
						console.log(response.auth_token)
						alert('good')
						sessionStorage.setItem("auth_token", response.auth_token)
					},
					error: (response) => {
					
						if (response.status === 400){
						alert('Неверно')

						}
					}
				}) 
			},
		}
	}
</script>

<style scoped>
</style>
