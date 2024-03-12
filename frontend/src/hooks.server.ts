import { FRONTEND_URL } from '$lib/config';
import { redirect, type Handle } from '@sveltejs/kit';

const validateUser = async (session: string): Promise<boolean> => {
	const isValid = await fetch(`${FRONTEND_URL}/api/v1/auth/verify`, {
		method: 'POST',
		headers: {
			Authorization: `Bearer ${session}`
		}
	});
	if (isValid.status == 401) {
		return false;
	}
	return await isValid.json();
};

export const handle: Handle = async ({ event, resolve }) => {
	const { params, url } = event;

	if (url.pathname == '/') {
		return resolve(event);
	}

	if (url.pathname == '/dashboard') {
		console.log(url.searchParams);
		const session = url.searchParams.get('session');
		if (!session) {
			throw redirect(301, '/');
		}
		if (!(await validateUser(session))) {
			throw redirect(301, '/');
		}
		event.locals.session = session;
		// console.log(page)
	}

	const response = await resolve(event);

	return response;
};
