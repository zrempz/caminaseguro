<script lang="ts">
	/**
	 * @file Componente que muestra la ubicación del usuario en un mapa.
	 * @description SOLID (SRP): Encapsula toda la complejidad de la geolocalización
	 * y la renderización del mapa, interactuando con un servicio (`mapService`)
	 * y manejando sus propios estados (cargando, error, éxito).
	 */
	import { onMount, tick } from 'svelte';
	import { MapPin } from 'lucide-svelte';
	import { obtenerUbicacionActual, inicializarMapa } from '$lib/services/mapService';
	import Card from '$lib/components/ui/Card.svelte';

	let contenedorMapa: HTMLDivElement;
	let mensajeEstado: string | null = 'Obteniendo tu ubicación...';

	onMount(async () => {
		try {
			const ubicacion = await obtenerUbicacionActual();
			mensajeEstado = null;

			await tick();

			await inicializarMapa(contenedorMapa.id, ubicacion);
		} catch (error: unknown) {
			// Manejo de errores detallado y específico para Geolocation API.
			if (error instanceof GeolocationPositionError) {
				switch (error.code) {
					case 1:
						mensajeEstado = 'Permiso denegado. Actívalo en los ajustes de tu navegador.';
						break;
					case 2:
						mensajeEstado = 'Ubicación no disponible (sin señal GPS o de red).';
						break;
					case 3:
						mensajeEstado = 'Se agotó el tiempo de espera para obtener la ubicación.';
						break;
				}
			} else if (error instanceof Error) {
				mensajeEstado = error.message;
			} else {
				mensajeEstado = 'Ha ocurrido un error inesperado.';
			}
		}
	});
</script>

<Card class="h-full w-full">
	{#snippet header()}
		<div class="flex items-center justify-center gap-3">
			<MapPin class="h-6 w-6 text-blue-600 dark:text-blue-400" />
			<h2 class="text-xl font-bold text-gray-800 dark:text-white">Tu Ubicación Actual</h2>
		</div>
	{/snippet}

	<div class="h-96 w-full rounded-lg bg-gray-200 dark:bg-gray-700">
		{#if mensajeEstado}
			<div
				class="flex h-full items-center justify-center p-4 text-center font-semibold text-yellow-600 dark:text-yellow-400"
			>
				<p>{mensajeEstado}</p>
			</div>
		{:else}
			<div id="mapa-ubicacion-usuario" bind:this={contenedorMapa} class="h-full w-full"></div>
		{/if}
	</div>
</Card>
