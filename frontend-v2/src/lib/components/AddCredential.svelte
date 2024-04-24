<script lang="ts">
	import { generateString, BACKEND_URL } from "$lib/utils";

    let website = "";
    let password = "";

    function generateRandomPassword() : string {
        return generateString(21);
    }
    async function addPassword(){
        fetch(`${BACKEND_URL}/v1/credentials`)
    }

</script>


<form >
    <input type="text" bind:value={website} placeholder="Website URL"> 
    <input type="password" bind:value={password} placeholder="Password">
    <button on:click={generateRandomPassword}>Generate Random Password</button>
    <button on:click={async () => {

    }}> Add Password</button>
</form>