// SOLID (SRP): La única responsabilidad de este hook es gestionar la sesión
// del usuario en cada petición del lado del servidor.
import type { Handle } from '@sveltejs/kit';
import { BACKEND_API_BASE_URL } from '$env/static/private';
import type { Usuario } from '$lib/types';

/**
 * @file Hook del lado del servidor que se ejecuta en cada petición.
 * @description Su única responsabilidad es interceptar las peticiones, verificar si
 * existe un token JWT en las cookies, validarlo contra el backend y, si es
 * válido, inyectar los datos del usuario en `event.locals`.
 */

export const handle: Handle = async ({ event, resolve }) => {
	const token = event.cookies.get('jwt');
	event.locals.usuario = null;

	if (token) {
		try {
			// Validar token
			const response = await fetch(`${BACKEND_API_BASE_URL}/api/auth/usuario/`, {
				headers: {
					Authorization: `Bearer ${token}`
				}
			});

			if (response.ok) {
				const usuario: Usuario = await response.json();
				event.locals.usuario = usuario;
			}
		} catch {
			event.locals.usuario = null;
		}
	}

	return resolve(event);
};
