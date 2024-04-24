<script lang="ts">
	import CredentialCard from '$lib/components/credentialCard.svelte';
	import { FRONTEND_URL } from '$lib/config.js';
	import { page } from '$app/stores';
	import { redirect } from '@sveltejs/kit';
	import TitleCard from '$lib/components/TitleCard.svelte';
	import { enhance } from '$app/forms';
	import { generateRandomPassword } from '$lib/utils';

	export let data;
	let website = '';
	let password = '';
	let error = '';
	let is_error = false;

	let credentials = data.credentials;

	const hasSessionToken = $page.url.searchParams.has('session');
	if (!hasSessionToken) {
		throw redirect(301, '/');
	}
	const sessionToken = $page.url.searchParams.get('session');
	if (!sessionToken) {
		throw redirect(301, '/');
	}

	async function submitNewCredential() {
		const data = {
			website: website,
			password: password
		};
		console.log(data);
		console.log(JSON.stringify(data));
		const posted = await fetch(`${FRONTEND_URL}/api/v1/credentials`, {
			method: 'POST',
			body: JSON.stringify(data),
			headers: {
				Authorization: `Bearer ${sessionToken}`,
				'Content-Type': 'application/json'
			}
		});
		console.log(await posted.json());
		if (posted.status != 201) {
			is_error = true;
			error = 'Problem Boy!';
		}
		window.location.reload();
	}
</script>

<svelte:head>
	<title>Sotera Dashboard</title>
</svelte:head>

<section class="">
	<TitleCard />
	<div class="credential-card-container">
		{#each credentials as credential, i}
			<CredentialCard
				website={credential.website}
				password={credential.password}
				card_id={credential.id}
				session={sessionToken}
			/>
		{/each}
	</div>
	<div>
		{#if is_error}
			{error}
		{/if}
	</div>
	<div class="credential-add-container">
		<h4 class="credential-add-text">Add a New Credential!</h4>
		<form on:submit={submitNewCredential} use:enhance method="POST" class="credential-form">
			<input
				name="website"
				bind:value={website}
				placeholder="Website URL"
				class="credential website-input"
			/>
			<input
				name="password"
				bind:value={password}
				placeholder="Password"
				type="password"
				class="credential"
			/>
			<button type="submit" class="">Add</button>
			<button
				on:click={() => {
					password = generateRandomPassword(21);
				}}>Generate Random Password!</button
			>
		</form>
	</div>
</section>

<style>
	.credential-card-container {
		margin-top: 10vh;
		display: flex;
		flex-direction: row;
		justify-content: space-around;
	}
	.credential-add-container {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.credential-add-text {
		font-family:
			system-ui,
			-apple-system,
			BlinkMacSystemFont,
			'Segoe UI',
			Roboto,
			Oxygen,
			Ubuntu,
			Cantarell,
			'Open Sans',
			'Helvetica Neue',
			sans-serif;
		color: #ed9455;
		font-size: 20px;
	}
	.credential {
		font-family: monospace;
	}
</style>
