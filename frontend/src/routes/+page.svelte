<script lang="ts">
	import { type Token } from '$lib/types/token';
	import { FRONTEND_URL } from '$lib/config';
	import logo from '$lib/assets/sotera_logo.png';
	import { session_store } from '$lib/session';
	import { redirect } from '@sveltejs/kit';

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

<section class="h-screen relative">
	<div
		class="parent border-2 rounded-xl border-slate-900 text-white flex flex-col justify-center items-center border-white top-[50%] left-[50%] translate-y-[50%] w-[20%] translate-x-[200%]"
	>
		<h1 class="text-5xl mb-5">Sotera</h1>
		<div class="child">
			<div class="sibling rounded-xl mb-1">
				<img class="w-full" src={logo} alt="Sotera Logo" />
			</div>
			<div class="sibling text-center mb-4">
				<code class="">Authentication Simplified!</code>
			</div>
			<div class="pb-12">
				<form on:submit={main}>
					<div class="">
						<input
							bind:value={user_token}
							type="text"
							placeholder="Your One Time Auth Key!"
							class="sibling border rounded-md focus:outline-none p-2 text-black"
						/>
					</div>
					<button type="submit" class="bg-white mt-3 w-[100%] p-2 text-black rounded-md"
						>Submit</button
					>
				</form>
			</div>
		</div>
		{#if is_error}
			<span class="text-red-600">{error}</span>
		{/if}
	</div>
</section>

<style lang="postcss">
</style>
