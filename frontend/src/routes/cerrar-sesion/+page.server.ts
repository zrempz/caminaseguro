import { redirect } from '@sveltejs/kit';
import type { Actions, PageServerLoad } from './$types';

// Esta página no se renderiza, solo gestiona la acción.
export const load: PageServerLoad = async () => {
	throw redirect(303, '/');
};

export const actions: Actions = {
	default: async ({ cookies }) => {
		// Borramos la cookie de sesión para desautenticar al usuario.
		cookies.delete('jwt', { path: '/' });
		throw redirect(303, '/iniciar-sesion');
	}
};
