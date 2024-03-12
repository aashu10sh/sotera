import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import type { Credential } from '$lib/types/credential';
import { FRONTEND_URL } from '$lib/config';

const validateToken = async (session: string) => {};

const getCredentials = async (session: string) => {
	const data = await fetch(`${FRONTEND_URL}/api/v1/credentials`, {
		method: 'GET',
		headers: {
			Authorization: `Bearer ${session}`
		}
	});
	const json_data = await data.json();
	let final: Credential[] = [];
	for (let element of json_data) {
		final.push({
			id: element.id,
			user_id: element.user_id,
			website: element.website,
			password: element.password
		});
	}
	return final;
};

export const load: PageServerLoad = async ({ locals }) => {
	if (!locals.session) {
		throw redirect(303, '/');
	}
	const session = locals.session;
	const credentials: Credential[] = await getCredentials(session);
    console.log('credentials are : ')
	console.log(credentials);
	return {
		credentials: credentials
	};
};
