<script lang="ts">
	import Credential from './Credential.svelte';
</script>

<section class="credential-card-container">
	<Credential website="https://youtube.com" password="deerhackrocks" id="21" />
	<Credential website="https://deerhack.deerwalk.edu.np" password="deerhackrocks" id="21" />
	<Credential website="https://facebook.com" password="hahaha" id="1" />
	<Credential website="https://deerwalk.edu.np" password="yesdeerhackyes" id="3" />
</section>

<style>
	.credential-card-container {
		margin-top: 10vh;
		display: flex;
		flex-direction: row;
		justify-content: space-around;
	}
</style>
