<script lang="ts">
	import type { Usuario } from '$lib/types';

	/**
	 * @file Componente para mostrar las acciones del usuario (Iniciar/Cerrar Sesión, Panel).
	 * @description Se crea para evitar la duplicación de código en la cabecera (DRY).
	 */

	type Props = {
		usuario: Usuario | null;
		/** El modo de visualización para aplicar los estilos correctos. */
		modo: 'escritorio' | 'movil';
		/** Callback opcional para ejecutar al hacer clic en un enlace. */
		onEnlaceClick?: () => void;
	};

	let { usuario, modo, onEnlaceClick = () => {} }: Props = $props();
</script>

{#if usuario}
	<a
		href="/panel"
		onclick={onEnlaceClick}
		class={modo === 'escritorio'
			? 'text-sm font-semibold text-gray-700 transition-colors hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400'
			: 'block rounded-lg px-3 py-2 text-base font-medium text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-800'}
	>
		Panel
	</a>
	<form action="/cerrar-sesion" method="POST">
		<button
			type="submit"
			class={modo === 'escritorio'
				? 'rounded-lg bg-gray-200 px-4 py-2 text-sm font-semibold text-gray-800 transition-colors hover:bg-gray-300 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600'
				: 'block w-full rounded-lg bg-gray-200 px-3 py-2 text-center font-semibold text-gray-800 transition-colors hover:bg-gray-300 dark:bg-gray-700 dark:text-white'}
		>
			Cerrar Sesión
		</button>
	</form>
{:else}
	<a
		href="/iniciar-sesion"
		onclick={onEnlaceClick}
		class={modo === 'escritorio'
			? 'rounded-lg bg-blue-600 px-4 py-2 text-sm font-semibold text-white transition-all hover:bg-blue-700 hover:shadow-lg hover:shadow-blue-500/20'
			: 'block rounded-lg bg-blue-600 px-3 py-2 text-center font-semibold text-white transition-colors hover:bg-blue-700'}
	>
		Iniciar Sesión
	</a>
{/if}
