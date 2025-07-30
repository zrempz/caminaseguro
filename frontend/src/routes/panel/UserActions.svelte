<script lang="ts">
	/**
	 * @file Componente con las acciones disponibles para el usuario en el panel.
	 * @description SOLID (SRP): Su única responsabilidad es mostrar botones de acción
	 * como "Editar Perfil" y "Cerrar Sesión".
	 */
	import { Edit, LogOut } from 'lucide-svelte';
</script>

<div class="rounded-2xl bg-white p-6 shadow-lg sm:p-8 dark:bg-gray-800">
	<div class="flex flex-col gap-4 sm:flex-row">
		<button
			class="flex w-full items-center justify-center gap-3 rounded-lg bg-blue-600 px-6 py-3 font-semibold text-white shadow-md transition-all hover:bg-blue-700"
		>
			<Edit class="h-5 w-5" />
			Editar Perfil
		</button>
		<form action="/cerrar-sesion" method="POST" class="w-full">
			<button
				type="submit"
				class="flex w-full items-center justify-center gap-3 rounded-lg bg-gray-200 px-6 py-3 font-semibold text-gray-800 transition-all hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-200"
			>
				<LogOut class="h-5 w-5" />
				Cerrar Sesión
			</button>
		</form>
	</div>
</div>
