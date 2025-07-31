<script lang="ts">
	/**
	 * @file Componente que muestra la sección de la marca en el pie de página.
	 * @description Compone el logo reutilizable y añade el eslogan de la marca.
	 */
	import Logo from './Logo.svelte';
</script>

<section class="space-y-4" aria-labelledby="footer-brand">
	<h2 id="footer-brand" class="sr-only">Marca</h2>

	<Logo as="div" size="grande" />

	<p class="max-w-xs text-sm text-gray-600 dark:text-gray-400">Protegiéndote a cada paso.</p>
</section>
