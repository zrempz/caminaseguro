<script lang="ts">
	/**
	 * @file Componente principal del pie de página.
	 * @description Ensambla las diferentes secciones del footer (marca, enlaces, sociales)
	 * importando todos los datos desde un archivo de configuración central.
	 */
	import FooterBrand from './FooterBrand.svelte';
	import FooterLinkColumn from './FooterLinkColumn.svelte';
	import FooterSocials from './FooterSocials.svelte';
	import { exploreLinks, legalLinks, copyright } from '$lib/config/footer';

	const currentYear = new Date().getFullYear();
</script>

<footer class="border-t border-gray-200 bg-gray-50 dark:border-gray-800 dark:bg-gray-900">
	<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
		<div class="py-12 md:py-16">
			<div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-4">
				<FooterBrand />
				<FooterLinkColumn title="Explorar" links={exploreLinks} />
				<FooterLinkColumn title="Legal" links={legalLinks} />
				<FooterSocials />
			</div>

			<div class="mt-12 border-t border-gray-200 pt-8 dark:border-gray-800" role="contentinfo">
				<p class="text-center text-sm text-gray-500 dark:text-gray-400">
					© {currentYear}
					{copyright.brandName}. {copyright.message}
				</p>
			</div>
		</div>
	</div>
</footer>

<style>
	footer {
		transition:
			background-color 0.3s ease,
			border-color 0.3s ease;
	}
</style>
