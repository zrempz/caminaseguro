import { fail } from '@sveltejs/kit';
import { z } from 'zod';
import { BACKEND_API_BASE_URL } from '$env/static/private';
import type { Actions } from './$types';
/**
 * @file Maneja la lógica del servidor para el registro de usuarios.
 * @description Define el esquema de validación y la acción del formulario.
 */

const esquemaRegistro = z.object({
	nombre: z.string().min(3, { message: 'El nombre debe tener al menos 3 caracteres.' }),
	email: z.email({ message: 'El formato del email no es válido.' }),
	password: z.string().min(8, { message: 'La contraseña debe tener al menos 8 caracteres.' })
});

/**
 * Llama al endpoint de registro del backend.
 * @param datos - Los datos del usuario validados.
 * @returns Una promesa que se resuelve si la llamada es exitosa.
 * @throws Un error con el mensaje del backend si la respuesta no es OK.
 */
async function registrarUsuario(datos: z.infer<typeof esquemaRegistro>) {
	const response = await fetch(`${BACKEND_API_BASE_URL}/api/auth/registro/`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(datos)
	});

	if (!response.ok) {
		const errorData = await response.json();
		throw new Error(errorData.error || 'Ocurrió un error al registrar la cuenta.');
	}
}

export const actions: Actions = {
	default: async ({ request }) => {
		const formData = await request.formData();
		const data = Object.fromEntries(formData);

		const resultadoValidacion = esquemaRegistro.safeParse(data);

		const datosDeEntrada = { nombre: data.nombre, email: data.email };

		if (!resultadoValidacion.success) {
			const errores = z.treeifyError(resultadoValidacion.error);
			return fail(400, {
				nombre: data.nombre,
				email: data.email,
				errors: {
					nombre: errores.properties?.nombre?.errors,
					email: errores.properties?.email?.errors,
					password: errores.properties?.password?.errors
				}
			});
		}

		try {
			await registrarUsuario(resultadoValidacion.data);
		} catch (error) {
			return fail(500, {
				...datosDeEntrada,
				error: error instanceof Error ? error.message : 'Error desconocido en el servidor.'
			});
		}

		return {
			success: true,
			message: '¡Te has registrado con éxito! Revisa tu email para verificar tu cuenta.'
		};
	}
};
