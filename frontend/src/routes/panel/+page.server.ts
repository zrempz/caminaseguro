import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

/**
 * @file Carga los datos del lado del servidor para la página del panel de usuario.
 * @description Antes de renderizar la página,
 * este script verifica si el objeto `locals.usuario` (inyectado por el hook)
 * existe. Si no existe, significa que el usuario no está autenticado, y se le
 * redirige a la página de inicio de sesión.
 */
export const load: PageServerLoad = async ({ locals }) => {
	// Verificamos si el usuario fue cargado por el hook.
	if (!locals.usuario) {
		throw redirect(303, '/iniciar-sesion');
	}

	// Si está autenticado, pasamos los datos del usuario a la página para que los renderice.
	return {
		usuario: locals.usuario
	};
};
