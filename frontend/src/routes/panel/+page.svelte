<script lang="ts">
	/**
	 * @file Página principal del Panel de Usuario (Dashboard).
	 * @description  Este componente actúa como
	 * un "Contenedor". Su única responsabilidad es organizar la disposición de los
	 * componentes de presentación que conforman el dashboard.
	 */
	import type { PageData } from './$types';
	import UserProfile from './UserProfile.svelte';
	import AlertButton from './AlertButton.svelte';
	import LocationMap from './LocationMap.svelte';
	import UserActions from './UserActions.svelte';

	let { data }: { data: PageData } = $props();
</script>

<svelte:head>
	<title>Panel de Usuario - CaminaSeguro</title>
</svelte:head>

<div class="mx-auto grid w-full max-w-6xl grid-cols-1 gap-8 px-4 md:grid-cols-2">
	<div class="md:col-span-2">
		<UserProfile usuario={data.usuario} />
	</div>

	<div class="flex items-center justify-center">
		<AlertButton />
	</div>

	<div class="flex items-center justify-center">
		<LocationMap />
	</div>

	<div class="md:col-span-2">
		<UserActions />
	</div>
</div>
