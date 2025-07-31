<script lang="ts">
	type Enlace = {
		href: string;
		texto: string;
	};

	/**
	 * @prop enlaces - Array de objetos de enlace a renderizar.
	 * @prop modo - Define el estilo de los enlaces ('escritorio' o 'movil').
	 * @prop onEnlaceClick - Callback opcional que se ejecuta al hacer clic en un enlace.
	 */
	let {
		enlaces,
		modo,
		onEnlaceClick = () => {}
	}: {
		enlaces: Enlace[];
		modo: 'escritorio' | 'movil';
		onEnlaceClick?: () => void;
	} = $props();

	// Clases base compartidas
	const clasesBase = 'font-medium transition-colors';

	// Clases específicas por modo
	const clasesModo = {
		escritorio:
			'text-sm text-gray-700 hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400',
		movil:
			'block rounded-lg px-3 py-2 text-base text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-800'
	};
</script>

{#each enlaces as enlace (enlace.href)}
	<a href={enlace.href} class="{clasesBase} {clasesModo[modo]}" onclick={onEnlaceClick}>
		{enlace.texto}
	</a>
{/each}
