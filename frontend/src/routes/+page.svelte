<script lang="ts">
	/**
	 * @file Página de inicio (landing page) de la aplicación.
	 * @description Actúa como un "Componente Contenedor". Su única
	 * responsabilidad es obtener datos (evaluando el riesgo y cargando la config)
	 * y pasarlos a los componentes de presentación (`RiskIndicator`, `InfoCard`).
	 */
	import { onMount } from 'svelte';
	import AOS from 'aos';
	import 'aos/dist/aos.css';
	import { evaluarRiesgo, type Riesgo } from '$lib/services/riesgo';
	import { seccionesInfo } from '$lib/config/landingPage';
	import RiskIndicator from '$lib/components/landing/Riskindicator.svelte';
	import InfoCard from '$lib/components/landing/InfoCard.svelte';

	let mensaje = $state('Evaluando el entorno...');
	let nivel = $state<Riesgo | null>(null);

	onMount(() => {
		AOS.init({ once: true, duration: 800, offset: 50 });
		const resultado = evaluarRiesgo();
		mensaje = resultado.mensaje;
		nivel = resultado.nivel;
	});
</script>

<svelte:head>
	<title>CaminaSeguro - Seguridad en tus trayectos</title>
	<meta name="description" content="Aplicación de seguridad personal con alertas en tiempo real" />
</svelte:head>

<div class="px-4 py-12">
	<div class="mx-auto max-w-4xl space-y-10">
		<RiskIndicator {mensaje} {nivel} />

		{#each seccionesInfo as section (section.title)}
			<InfoCard title={section.title} content={section.content} delay={section.delay} />
		{/each}
	</div>
</div>
