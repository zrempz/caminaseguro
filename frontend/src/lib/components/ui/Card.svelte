<script lang="ts">
	import type { Snippet } from 'svelte';

	/**
	 * @prop {Snippet} children - El contenido principal de la tarjeta.
	 * @prop {Snippet} [header] - Contenido opcional para la cabecera.
	 * @prop {string} [class] - Clases CSS adicionales para el contenedor principal.
	 */
	let {
		children,
		header,
		class: extraClasses = ''
	}: {
		children: Snippet;
		header?: Snippet;
		class?: string;
	} = $props();
</script>

<div
	class="flex w-full max-w-md flex-col rounded-xl bg-white p-8 shadow-lg dark:bg-gray-800 {extraClasses}"
>
	{#if header}
		{@render header()}
	{/if}
	<div class="mt-8 flex-grow">
		{@render children()}
	</div>
</div>
