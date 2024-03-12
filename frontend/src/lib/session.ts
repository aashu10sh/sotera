import { readable, writable } from 'svelte/store';
import { browser } from '$app/environment';
export const ssr = false;

async function session_store() {
	if (!browser) return; //ONLY
	const storedSession = localStorage.getItem('session');
	const session = writable(storedSession);
	session.subscribe((value) => {
		localStorage.setItem('session', value || '');
	});
	return session;
}

export { session_store };
