<script lang="ts">
	import { draw } from 'svelte/transition';

	/**
	 * @prop abierto - El estado del menú, enlazado bidireccionalmente (bind:abierto).
	 */
	let { abierto = $bindable() }: { abierto: boolean } = $props();
</script>

<button
	onclick={() => (abierto = !abierto)}
	class="rounded-md p-2 text-gray-700 transition-colors hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-800"
	aria-label="Alternar menú de navegación"
	aria-expanded={abierto}
	aria-controls="menu-movil"
>
	<svg
		class="h-6 w-6 transition-transform duration-300"
		class:rotate-90={abierto}
		fill="none"
		stroke="currentColor"
		viewBox="0 0 24 24"
	>
		{#if abierto}
			<path
				in:draw={{ duration: 200, delay: 100 }}
				out:draw={{ duration: 200 }}
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width={2}
				d="M6 18L18 6M6 6l12 12"
			/>
		{:else}
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width={2}
				d="M4 6h16M4 12h16M4 18h16"
			/>
		{/if}
	</svg>
</button>

<style>
	.rotate-90 {
		transform: rotate(90deg);
	}
</style>
