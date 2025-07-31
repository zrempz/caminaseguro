<script lang="ts">
	/**
	 * @file Componente para renderizar una columna de enlaces en el pie de página.
	 * @description Su única responsabilidad es mostrar un título y una lista de enlaces
	 * que se le pasan como propiedades. Es reutilizable para cualquier sección del footer.
	 * @author Tu Nombre
	 */

	/**
	 * Define la estructura de un enlace individual.
	 */
	type Link = {
		/** La URL a la que apunta el enlace. */
		href: string;
		/** El texto visible del enlace. */
		text: string;
	};

	/**
	 * Propiedades que el componente espera recibir desde su padre.
	 */
	type Props = {
		/** El título de la columna (ej. "Soluciones", "Compañía"). */
		title: string;
		/** Un array de objetos de tipo Link para renderizar en la lista. */
		links: Link[];
	};

	let { title, links }: Props = $props();

	/**
	 * Genera un ID único para el título de la sección.
	 * Se utiliza para mejorar la accesibilidad, conectando la sección (`<section>`)
	 * con su título (`<h3>`) a través del atributo `aria-labelledby`.
	 */
	const titleId = `footer-col-${title.toLowerCase().replace(/\s+/g, '-')}`;

	const linkClasses =
		'text-sm text-gray-600 transition-colors hover:text-blue-600 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:outline-none dark:text-gray-400 dark:hover:text-blue-400';
</script>

<section aria-labelledby={titleId}>
	<h3
		id={titleId}
		class="text-sm font-semibold tracking-wider text-gray-900 uppercase dark:text-white"
	>
		{title}
	</h3>
	<ul class="mt-4 space-y-3">
		{#each links as link (link.href)}
			<li>
				<a href={link.href} class={linkClasses}>
					{link.text}
				</a>
			</li>
		{/each}
	</ul>
</section>
