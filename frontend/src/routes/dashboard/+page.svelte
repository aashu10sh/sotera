<script lang="ts">
    import CredentialCard from '$lib/components/credentialCard.svelte';
	import { FRONTEND_URL } from '$lib/config.js';
    import { page } from '$app/stores';
	import { redirect } from '@sveltejs/kit';
	export let data;
    let website = "";
    let password = "";
    let error  = "";
    let is_error = false;

	let credentials = data.credentials;
    
    const hasSessionToken = $page.url.searchParams.has('session');
    if (!hasSessionToken){
        throw redirect(301, '/');
    }
    const sessionToken = $page.url.searchParams.get('session');
    if (!sessionToken){
        throw redirect(301, '/');   
    }

    async function submitNewCredential(){
        const data = {
            website:website,
            password:password
        }
        console.log(data)
        console.log(JSON.stringify(data));
        const posted = await fetch(`${FRONTEND_URL}/api/v1/credentials`,{
            method:"POST",
            body:JSON.stringify(data),
            headers:{
                "Authorization": `Bearer ${sessionToken}`,
                'Content-Type': 'application/json'
            }
        })
        console.log(await posted.json())
        if (posted.status != 201){
            is_error = true;
            error = "Problem Boy!"
        }
        window.location.reload()
    }
    
</script>

<section class="text-white bg-black relative">
    <h1 class="text-center mb-16 mt-10 text-lg">SOTERA</h1>
    <div class="mb-16 flex flex-col justify-center items-center gap-2">
        <h4> Add a New Credential!</h4>
        <form on:submit={submitNewCredential}  method="POST" class="text-black">
            <input name="website" bind:value={website} placeholder="Website URL">
            <input name="password" bind:value={password} placeholder="Password" type="password" >
            <button type="submit" class="text-black bg-white">Add</button>
        </form>
    </div>
    <div class="flex gap-5 justify-center items-center w-[80%] mx-auto">
        {#each credentials as credential, i}
            <CredentialCard website={credential.website} password={credential.password} card_id={credential.id} session={sessionToken}/>
        {/each}
    </div>
    <div>
        {#if is_error}
            {error}
        {/if}
    </div>
</section>


