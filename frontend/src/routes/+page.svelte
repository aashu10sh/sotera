<script lang="ts">
	import { type Token } from '$lib/types/token';
	import { FRONTEND_URL } from '$lib/config';
	import logo from '$lib/assets/sotera_logo.png';
	import { session_store } from '$lib/session';

	let user_token: string = '';
	let is_error: boolean = false;
	let error: string = '';

	async function handleSubmit(token: Token) {
		const response = await fetch(`${FRONTEND_URL}/api/v1/auth/login`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(token)
		});

		console.log(response.status);
		const tokens = await response.json();
		const session = await session_store();
		session?.set(tokens.key);

		window.location = `/dashboard?session=${tokens.key}`;
	}
	async function extract_auth_tokens(): Promise<Token> {
		const token = user_token;
		const decoded = atob(token);
		const isJson = isJsonString(decoded);
		console.log('Is Json', isJson);
		if (!isJson) {
			is_error = true;
			error = 'Invalid Token! Json Decode Error';
		}
		console.log(decoded);
		const decoded_obj = JSON.parse(decoded);
		if (!decoded_obj || !decoded_obj.key_id || !decoded_obj.nonce) {
			error = 'Cannot Decode to Valid Required Value. ';
		}
		console.log('Decoded Obj');
		console.log(decoded_obj);
		return {
			key_id: decoded_obj?.key_id,
			nonce: decoded_obj?.nonce
		};
	}

	async function main() {
		const auth_token = await extract_auth_tokens();
		await handleSubmit(auth_token);
	}

	function isJsonString(str: string): boolean {
		try {
			JSON.parse(str);
		} catch (e) {
			console.log('The Json Parse Error is ', e);
			console.log(e);
			return false;
		}
		return true;
	}
</script>

<svelte:head>
	<title>Sotera Login</title>
</svelte:head>

<section class="main">
	<div
		class=""
	>
		<h1 class="header">Sotera</h1>
			<div class="child">

				<img class="" src={logo} alt="Sotera Logo" />
				<code class="">Authentication Simplified!</code>
			</div>
			<div class="form-container">
				<form on:submit={main}>
					<div class="text-input">
						<input
							bind:value={user_token}
							type="text"
							placeholder="Your One Time Auth Key!"
							class=""
						/>
					</div>
					<button type="submit" class=""
						>Submit</button
					>
				</form>
			
		</div>
		{#if is_error}
			<span class="error">{error}</span>
		{/if}
	</div>
</section>

<style lang="postcss">
	.main{
		display: flex;
		align-items: center;
		flex-direction: column;
		justify-content: center;
	}
	.header{
		font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		color: white;
		text-align: center;
		font-size: 50px;
		padding: 10px;

	}
	.child{
		color:white;
		display:flex;
		flex-direction: column;
		gap:20px;
		justify-content: center;
		align-items: center;
		font-size:18px;

	}
	.form-container{
		margin-top:30px;
		display:flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		
	}
	.form-container>form{
		display:flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.text-input{
		margin-bottom:10px;
	}
	
	.error{
		color:red;
	}
</style>
