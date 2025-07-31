<script lang="ts">
	/**
	 * @file Layout global de la aplicación.
	 * @description Este componente envuelve cada página de la aplicación. Su principal
	 * responsabilidad es renderizar el `Header` y pasarle los datos del usuario
	 * (que vienen de `$page.data`) para que pueda mostrar un estado de UI
	 * condicional (ej. "Iniciar Sesión" vs "Mi Panel").
	 *
	 * También se encarga de importar los estilos globales de la aplicación.
	 */
	import '../app.css';
	import Header from '$lib/components/layout/Header.svelte';
	import Footer from '$lib/components/layout/Footer.svelte';
	import type { PageData } from './$types';
	import type { Snippet } from 'svelte';

	let { data, children }: { data: PageData; children: Snippet } = $props();
</script>

<div class="flex min-h-screen flex-col bg-gray-50 transition-colors duration-300 dark:bg-gray-900">
	<Header usuario={data.usuario} />

	<main class="flex-grow font-sans">
		{@render children()}
	</main>

	<Footer />
</div>

<style>
	:global(html) {
		transition:
			background-color 0.3s ease,
			color 0.3s ease;
	}
</style>
