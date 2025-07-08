<script lang="ts">
	import { User, Edit, LogOut } from 'lucide-svelte';
	import type { PageData } from './$types';

	let { data } = $props<{ data: PageData }>();

	// Usamos $state para que la UI reaccione si los datos cambian en el cliente.
	let usuario = $state(data.usuario);
</script>

<div class="mx-auto w-full max-w-2xl">
	<!-- Tarjeta principal del panel de usuario -->
	<div class="rounded-2xl bg-white p-8 shadow-lg md:p-12 dark:bg-gray-800">
		<!-- Sección de Información del Perfil -->
		<div class="flex flex-col items-center gap-8 md:flex-row">
			<!-- Avatar del Usuario -->
			<div
				class="flex h-32 w-32 flex-shrink-0 items-center justify-center rounded-full bg-gray-200 ring-4 ring-blue-500/50 dark:bg-gray-700"
			>
				{#if usuario.urlAvatar}
					<img
						src={usuario.urlAvatar}
						alt="Foto de perfil de {usuario.nombre}"
						class="h-full w-full rounded-full object-cover"
					/>
				{:else}
					<User class="h-16 w-16 text-gray-500 dark:text-gray-400" />
				{/if}
			</div>

			<!-- Información del Usuario -->
			<div class="text-center md:text-left">
				<h1 class="text-4xl font-bold text-gray-800 dark:text-white">
					Hola, {usuario.nombre.split(' ')[0]}!
				</h1>
				<p class="mt-1 text-lg text-gray-500 dark:text-gray-400">{usuario.correo}</p>
			</div>
		</div>

		<!-- Divisor -->
		<hr class="my-8 border-gray-200 dark:border-gray-700" />

		<!-- Sección de Acciones -->
		<div class="flex flex-col gap-4 sm:flex-row">
			<button
				class="flex w-full items-center justify-center gap-3 rounded-lg bg-blue-600 px-6 py-3 font-bold text-white shadow-md transition-all hover:bg-blue-700"
			>
				<Edit class="h-5 w-5" />
				Editar Perfil
			</button>
			<button
				class="flex w-full items-center justify-center gap-3 rounded-lg bg-gray-200 px-6 py-3 font-bold text-gray-800 transition-all hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-200 dark:hover:bg-gray-600"
			>
				<LogOut class="h-5 w-5" />
				Cerrar Sesión
			</button>
		</div>
	</div>
</div>
