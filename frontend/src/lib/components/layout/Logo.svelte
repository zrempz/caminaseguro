<script lang="ts">
	/**
	 * @file Componente reutilizable para mostrar el logotipo y nombre de la marca.
	 * @description Se puede renderizar como un enlace o un div simple y en diferentes tamaños
	 * para ser usado en la cabecera, pie de página, etc. (DRY, SRP).
	 */

	type Props = {
		/** Define el tamaño del logo y el texto. */
		size?: 'normal' | 'grande';
		/** Define si el componente raíz es un enlace 'a' o un 'div'. */
		as?: 'a' | 'div';
	};

	let { size = 'normal', as = 'a' }: Props = $props();

	const src = '/favicon.svg';
	const alt = 'Logotipo de CaminaSeguro';
	const href = '/';

	const sizeClasses = {
		normal: {
			img: 'h-8 w-8',
			text: 'text-xl sm:text-2xl'
		},
		grande: {
			img: 'h-10 w-10',
			text: 'text-xl'
		}
	};
	const currentClasses = sizeClasses[size];
</script>

<svelte:element
	this={as}
	{href}
	class="flex shrink-0 items-center gap-3"
	aria-label={as === 'a' ? 'Página de inicio' : undefined}
>
	<img {src} {alt} class={currentClasses.img} width="40" height="40" />
	<span class="font-bold text-gray-900 dark:text-white {currentClasses.text}"> CaminaSeguro </span>
</svelte:element>
