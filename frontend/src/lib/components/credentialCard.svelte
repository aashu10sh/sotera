
<script lang="ts">
	import { FRONTEND_URL } from "$lib/config";
    export let website : string ;
    export let password : string ;
    export let card_id : number;
    export let session : string;
    async function deleteCredential(){
        const response = await fetch(`${FRONTEND_URL}/api/v1/credentials/${card_id}`,{
            method:"DELETE",
            headers:{
                "Authorization": `Bearer ${session}`
            }
        });
        if (response.status != 200 ){
            alert("Could Not Delete!")
        }
        window.location.reload();
    }
</script>

<section class="mb-24">
    <h2 class="text-white">{website}</h2>
    <code class="text-white">{password}</code>
    <button on:click={deleteCredential}>Delete Credential</button>

</section>
