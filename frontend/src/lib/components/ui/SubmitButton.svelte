<script lang="ts">
	import type { Snippet } from 'svelte';

	/**
	 * @prop {Snippet} children - El contenido del botón.
	 * @prop {boolean} [isLoading=false] - Si es `true`, muestra un spinner.
	 */
	let {
		children,
		isLoading = false
	}: {
		children: Snippet;
		isLoading?: boolean;
	} = $props();
</script>

<button
	type="submit"
	disabled={isLoading}
	class="flex w-full justify-center rounded-lg bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:outline-none disabled:cursor-not-allowed disabled:opacity-50"
>
	{#if isLoading}{:else}
		{@render children()}
	{/if}
</button>
