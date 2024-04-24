<script lang="ts">
	import { FRONTEND_URL } from '$lib/config';
	export let website: string;
	export let password: string;
	export let card_id: number;
	export let session: string;
	async function deleteCredential() {
		const response = await fetch(`${FRONTEND_URL}/api/v1/credentials/${card_id}`, {
			method: 'DELETE',
			headers: {
				Authorization: `Bearer ${session}`
			}
		});
		if (response.status != 200) {
			alert('Could Not Delete!');
		}
		window.location.reload();
	}

	async function copy_to_clipboard() {
		navigator.clipboard.writeText(password);
	}
</script>

<div class="container">
	<h2 class="website">
		{website}
	</h2>
	<input type="password" class="input" value={password} disabled />
	<input type="hidden" value={card_id} />
	<div class="button-container">
		<button class="copy-button" on:click={copy_to_clipboard}> Copy </button>
		<button
			class="delete-button"
			on:click={async () => {
				await deleteCredential();
			}}
		>
			Delete
		</button>
	</div>
</div>

<style>
	.container {
		display: flex;
		/* margin:  1px solid white; */
		border: 1px solid white;
		flex-direction: column;
		background-color: white;
		padding: 5vh;
		width: 100;
		border-radius: 4vh;
		background-color: #872341;
		/* height: 20vh; */
	}
	.button-container {
		display: flex;
		justify-content: center;
		padding: 10px;
	}
	.website {
		color: white;
		font-family: monospace;
	}
	.button-container button {
		margin: 10px;
		padding: 2vh;
		width: 10vh;
		border-radius: 1vh;
	}
	.copy-button {
		background-color: #f05941;
		color: white;
	}
	.delete-button {
		background-color: #be3144;
		color: white;
	}
	.input {
		font-family: monospace;
	}
</style>
