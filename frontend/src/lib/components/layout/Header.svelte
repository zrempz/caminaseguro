<script lang="ts">
	import { fly } from 'svelte/transition';
	import Logo from './Logo.svelte';
	import NavLinks from './HeaderNavLinks.svelte';
	import BotonMenuMovil from './HeaderBotonMovil.svelte';
	import UserActions from './UserActions.svelte';
	import type { Usuario } from '$lib/types';

	/**
	 * @file Componente de cabecera principal y navegación del sitio.
	 * @description Es responsive y maneja el estado de autenticación del usuario.
	 * Orquesta componentes más pequeños como Logo, NavLinks y UserActions,
	 * siguiendo el principio de Composición sobre Herencia.
	 */

	let { usuario }: { usuario: Usuario | null } = $props();

	const TRANSITION_DURATION = 200;
	const TRANSITION_Y_OFFSET = -20;
	const ENLACES_NAVEGACION = [
		{ href: '/features', texto: 'Características' },
		{ href: '/about', texto: 'Sobre Nosotros' }
	];

	let abierto = $state(false);
	const cerrarMenu = () => {
		abierto = false;
	};

	/**
	 * Efecto para mejorar la accesibilidad: Cierra el menú al presionar la tecla 'Escape'.
	 */
	$effect(() => {
		const handleKeydown = (e: KeyboardEvent) => {
			if (e.key === 'Escape') cerrarMenu();
		};
		window.addEventListener('keydown', handleKeydown);
		return () => window.removeEventListener('keydown', handleKeydown);
	});

	/**
	 * Efecto para mejorar la experiencia de usuario: Cierra el menú al hacer scroll.
	 */
	$effect(() => {
		const handleScroll = () => {
			if (abierto) cerrarMenu();
		};
		window.addEventListener('scroll', handleScroll);
		return () => window.removeEventListener('scroll', handleScroll);
	});
</script>

<header
	class="fixed top-0 right-0 left-0 z-50 w-full bg-white/80 shadow-sm backdrop-blur-lg transition-shadow duration-300 dark:bg-gray-900/80"
	class:shadow-lg={abierto}
>
	<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
		<div class="flex h-16 items-center justify-between">
			<Logo />

			<nav class="hidden items-center gap-6 md:flex">
				<NavLinks enlaces={ENLACES_NAVEGACION} modo="escritorio" />
				<UserActions {usuario} modo="escritorio" />
			</nav>

			<div class="md:hidden">
				<BotonMenuMovil bind:abierto />
			</div>
		</div>
	</div>

	{#if abierto}
		<div
			transition:fly={{ y: TRANSITION_Y_OFFSET, duration: TRANSITION_DURATION }}
			id="menu-movil"
			class="border-t border-gray-200 bg-white/95 backdrop-blur-lg md:hidden dark:border-gray-700 dark:bg-gray-900/95"
		>
			<nav class="space-y-3 px-4 pt-2 pb-4">
				<NavLinks enlaces={ENLACES_NAVEGACION} modo="movil" onEnlaceClick={cerrarMenu} />
				<UserActions {usuario} modo="movil" onEnlaceClick={cerrarMenu} />
			</nav>
		</div>
	{/if}
</header>

<div class="h-16"></div>
