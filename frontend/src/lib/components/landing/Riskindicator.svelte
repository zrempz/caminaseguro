<script lang="ts">
	/**
	 * @file Componente para mostrar el banner de nivel de riesgo.
	 * @description SOLID (SRP): La única responsabilidad de este componente es
	 * renderizar el estado del riesgo (mensaje y nivel). No sabe de dónde vienen
	 * los datos, solo cómo mostrarlos.
	 */
	import type { Riesgo } from '$lib/services/riesgo';

	type Props = {
		mensaje: string;
		nivel: Riesgo | null;
	};

	let { mensaje, nivel }: Props = $props();

	/**
	 * Centralizacion de la configuración de estilos para cada nivel de riesgo.
	 */
	const ESTILOS_RIESGO = {
		bajo: {
			bg: 'bg-green-500/90 text-white',
			ping: 'bg-green-300',
			dot: 'bg-green-500'
		},
		medio: {
			bg: 'bg-yellow-500/90 text-gray-900',
			ping: 'bg-yellow-300',
			dot: 'bg-yellow-500'
		},
		alto: {
			bg: 'bg-red-600/90 text-white',
			ping: 'bg-red-300',
			dot: 'bg-red-500'
		}
	} as const;

	/**
	 * Estado derivado para calcular los estilos.
	 * El estilo se actualiza automáticamente cuando 'nivel' cambia.
	 */
	const estiloActual = $derived(
		nivel ? ESTILOS_RIESGO[nivel] : { bg: 'bg-gray-600', ping: '', dot: '' }
	);
</script>

<section class="text-center" role="banner" data-aos="zoom-in" data-aos-duration="1000">
	<h1 class="text-4xl font-bold text-gray-900 sm:text-5xl dark:text-white">CaminaSeguro</h1>
	<p class="mt-3 text-lg text-gray-600 dark:text-gray-300">
		{mensaje}
	</p>

	{#if nivel}
		<div
			class="mt-6 inline-flex items-center gap-2 rounded-full px-5 py-2.5 text-sm font-semibold transition-all {estiloActual.bg}"
			role="status"
			aria-live="polite"
			aria-atomic="true"
		>
			<span class="relative flex h-3 w-3">
				<span
					class="absolute inline-flex h-full w-full animate-ping rounded-full opacity-75 {estiloActual.ping}"
				></span>
				<span class="relative inline-flex h-3 w-3 rounded-full {estiloActual.dot}"></span>
			</span>
			Nivel de riesgo: {nivel}
		</div>
	{/if}
</section>