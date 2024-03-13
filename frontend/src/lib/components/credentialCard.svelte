
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

    async function copy_to_clipboard(){
        // Get the text field// For mobile devices

   // Copy the text inside the text field
          navigator.clipboard.writeText(password);
    }
</script>

<section class="w-[20rem] mb-10 ">
    <div class="border-2 bg-[#7ee7c2] text-black rounded-xl flex flex-col justify-center items-center gap-2 p-2">
        <h2 class="">{website}</h2>
        <input value={password}  type="password"/>
        <button on:click={deleteCredential}>Delete Credential</button>
        <button on:click={copy_to_clipboard}>Copy</button>
    </div>
</section>
