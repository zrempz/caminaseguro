import { fail, redirect } from '@sveltejs/kit';
import { treeifyError, z } from 'zod';
import { dev } from '$app/environment';
import { BACKEND_API_BASE_URL } from '$env/static/private';
import type { Actions } from './$types';

const COOKIE_LIFETIME = 60 * 60 * 24; // 1 dia
/**
 * @file Maneja la lógica del servidor para el inicio de sesión de usuarios.
 * @description Aplica Clean Code al separar la lógica de la API en una función
 * dedicada, haciendo que la acción principal sea más clara y fácil de mantener.
 */
const esquemaLogin = z.object({
	email: z.email({ message: 'Por favor, introduce un email válido.' }),
	password: z.string().min(1, { message: 'La contraseña es obligatoria.' })
});

/**
 * Llama al endpoint de login del backend para autenticar al usuario.
 * @param datos - Las credenciales del usuario ya validadas.
 * @returns El token JWT si la autenticación es exitosa.
 * @throws Un error con un mensaje específico si la autenticación falla.
 */
async function autenticarUsuario(datos: z.infer<typeof esquemaLogin>): Promise<string> {
	const response = await fetch(`${BACKEND_API_BASE_URL}/api/auth/login/`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(datos)
	});

	if (!response.ok) {
		throw new Error('El correo o la contraseña son incorrectos.');
	}

	const { token } = await response.json();
	return token;
}

export const actions: Actions = {
	default: async ({ request, cookies }) => {
		const formData = await request.formData();
		const data = Object.fromEntries(formData);

		const resultadoValidacion = esquemaLogin.safeParse(data);

		if (!resultadoValidacion.success) {
			const errores = treeifyError(resultadoValidacion.error);
			return fail(400, {
				email: data.email,
				errors: {
					email: errores.properties?.email?.errors,
					password: errores.properties?.password?.errors
				}
			});
		}

		try {
			const token = await autenticarUsuario(resultadoValidacion.data);

			cookies.set('jwt', token, {
				path: '/',
				httpOnly: true,
				secure: !dev,
				sameSite: 'strict',
				maxAge: COOKIE_LIFETIME
			});
		} catch (error) {
			const mensajeError =
				error instanceof Error ? error.message : 'Error desconocido en el servidor.';

			return fail(error instanceof Error && error.message.includes('incorrectos') ? 401 : 500, {
				email: data.email,
				error:
					mensajeError === 'Failed to fetch'
						? 'No se pudo conectar con el servidor. Inténtalo más tarde.'
						: mensajeError
			});
		}

		throw redirect(303, '/panel');
	}
};
