<script lang="ts">
	/**
	 * @file Componente que muestra el mensaje de éxito tras el registro.
	 * @description Su única responsabilidad es informar al usuario y gestionar
	 * la redirección automática a la página de inicio de sesión tras un breve
	 * periodo de tiempo.
	 */
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';

	let { message }: { message: string } = $props();
	const TIMEOUT = 3000;

	onMount(() => {
		const timer = setTimeout(() => {
			goto('/iniciar-sesion');
		}, TIMEOUT);

		return () => clearTimeout(timer);
	});
</script>

<div class="rounded-md bg-green-50 p-4 text-center dark:bg-green-900/20">
	<h3 class="text-sm font-medium text-green-800 dark:text-green-300">¡Registro Completado!</h3>
	<p class="mt-2 text-sm text-green-700 dark:text-green-400">{message}</p>
	<p class="mt-2 text-xs text-gray-500 dark:text-gray-400">Serás redirigido en 3 segundos...</p>
</div>
