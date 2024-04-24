<script>
	import { redirect } from '@sveltejs/kit';
	import {goto} from "$app/navigation";
	import { page } from '$app/stores'
	import CredentialList from '$lib/components/CredentialList.svelte';
	import TitleCard from '$lib/components/TitleCard.svelte';
    const session = $page.url.searchParams.get('session')
	if (!session){
		goto("/missing")
	}
</script>

<TitleCard />
<CredentialList />
