import type { LayoutServerLoad } from './$types';

/**
 * @file Carga de datos del layout raíz del lado del servidor.
 * @description Responsable de tomar los datos del
 * usuario (que fueron inyectados en `event.locals` por el hook principal en `src/hooks.server.ts`)
 * y exponerlos de forma segura al árbol de componentes de SvelteKit.
 *
 * Cada página de la aplicación tendrá acceso a `data.usuario`, permitiendo
 * renderizar la UI de forma condicional (ej. mostrar "Panel" vs. "Iniciar Sesión").
 */
export const load: LayoutServerLoad = async ({ locals }) => {
	// Si el usuario no está autenticado, 'locals.usuario' será `null`.
	return {
		usuario: locals.usuario
	};
};
