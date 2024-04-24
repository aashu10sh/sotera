import { redirect } from '@sveltejs/kit';
import { page } from '$app/stores'

export function load() {
    // const session = 
    const urlParams = new URLSearchParams(window.location.search);
    const isSession = urlParams.has('session');
    if (!isSession){
		redirect(302,"/missing")
    }
	// }
    // throw redirect(302, '/redirect-to-this-url');
}