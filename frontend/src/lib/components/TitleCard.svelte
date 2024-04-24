<script lang="ts">
	export const prerender = false;
	const APP_NAME: string = 'Sotera';
	const APP_SUBTEXT: string = 'A fingerprint based authentication system.';
</script>

<section>
	<div class="container">
		<div class="title">
			{APP_NAME}
		</div>
		<div class="subtext">
			{APP_SUBTEXT}
		</div>
	</div>
</section>

<style>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		color: #ed9455;
	}

	.title {
		font-weight: 900;
		width: 100;
		padding-top: 3vh;
		/* margin:5vh; */
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
		font-size: 60px;
	}
	.subtext {
		font-family: monospace;
		/* padding: 2vh; */
		padding-top: 2vh;
		font-weight: bold;
	}
</style>
