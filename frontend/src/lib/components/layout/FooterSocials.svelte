<script lang="ts">
	/**
	 * @file Componente que renderiza la sección de enlaces a redes sociales.
	 * @description Su única responsabilidad es mostrar la lista de iconos sociales,
	 * importando los datos desde un archivo de configuración separado para mantener
	 * el código limpio y mantenible (SRP, DRY).
	 */

	import { socials } from '$lib/config/socials';

	/** Clases base de Tailwind CSS aplicadas a todos los iconos para consistencia. */
	const baseClasses =
		'text-gray-400 transition-colors focus:ring-2 focus:ring-offset-2 focus:outline-none';
</script>

<section aria-labelledby="footer-social">
	<h3
		id="footer-social"
		class="text-sm font-semibold tracking-wider text-gray-900 uppercase dark:text-white"
	>
		Síguenos
	</h3>
	<ul class="mt-4 flex space-x-4">
		{#each socials as social (social.name)}
			<li>
				<a
					href={social.href}
					target="_blank"
					rel="noopener noreferrer"
					aria-label={social.name}
					class="{baseClasses} {social.hoverClass}"
				>
					<svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
						<path d={social.path} />
					</svg>
				</a>
			</li>
		{/each}
	</ul>
</section>
