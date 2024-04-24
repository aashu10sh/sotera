<script lang="ts">
	export let website: string;
	export let id: string;
	export let password: string;
	async function deleteCredential(id: string, session: string) {
		console.log('Deleting ID : ', id);
	}
</script>

<div class="container">
	<h2 class="website">
		{website}
	</h2>
	<input type="password" class="input" value={password} disabled />
	<input type="hidden" value={id} />
	<div class="button-container">
		<button class="copy-button"> Copy </button>
		<button
			class="delete-button"
			on:click={async () => {
				await deleteCredential(id, 'asads');
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
