<script lang="ts">
	/**
	 * @file Componente para mostrar la tarjeta de perfil del usuario.
	 * @description SOLID (SRP): La responsabilidad única de este componente es renderizar
	 * la información de bienvenida (nombre y email) del usuario que ha iniciado sesión.
	 * Recibe los datos del usuario a través de propiedades (props) para mantenerlo desacoplado.
	 */
	import { User } from 'lucide-svelte';
	import type { PageData } from './$types';

	let { usuario }: { usuario: PageData['usuario'] } = $props();

	/**
	 * Lógica para obtener el primer nombre se maneja en el script,
	 * no directamente en el HTML, manteniendo el template limpio y declarativo.
	 */
	const primerNombre = usuario.nombre.split(' ')[0];
</script>

<div class="rounded-2xl bg-white p-6 shadow-lg sm:p-8 dark:bg-gray-800">
	<div class="flex flex-col items-center gap-6 text-center md:flex-row md:gap-8 md:text-left">
		<div
			class="flex h-24 w-24 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 ring-4 ring-blue-500/50 md:h-32 md:w-32 dark:bg-blue-900/50"
		>
			<User class="h-12 w-12 text-blue-600 md:h-16 md:w-16 dark:text-blue-300" />
		</div>
		<div>
			<h1 class="text-3xl font-bold text-gray-900 md:text-4xl dark:text-white">
				¡Hola, {primerNombre}!
			</h1>
			<p class="mt-1 text-base text-gray-500 md:text-lg dark:text-gray-400">{usuario.email}</p>
		</div>
	</div>
</div>
