<script lang="ts">
	import { ShieldAlert } from 'lucide-svelte';
	import Card from '$lib/components/ui/Card.svelte';

	async function activarAlerta() {}
</script>

<Card class="h-full w-full">
	{#snippet header()}
		<h2 class="text-center text-xl font-bold text-gray-800 dark:text-white">
			¿Te Sientes en Riesgo?
		</h2>
	{/snippet}

	<div class="flex h-full flex-grow items-center justify-center p-4">
		<button
			on:click={activarAlerta}
			class="focus:ring-opacity-75 relative flex h-52 w-52 transform flex-col items-center justify-center rounded-full bg-red-600 text-white shadow-2xl transition-transform duration-300 hover:scale-110 focus:ring-4 focus:ring-red-400 focus:outline-none sm:h-64 sm:w-64"
			aria-label="Activar alerta de emergencia"
		>
			<span
				class="absolute inline-flex h-full w-full animate-ping rounded-full bg-red-500 opacity-75"
			></span>

			<ShieldAlert class="h-20 w-20 sm:h-24 sm:w-24" />
			<span class="mt-2 text-xl font-bold tracking-wider sm:text-2xl">¡ALERTA!</span>
		</button>
	</div>
</Card>
