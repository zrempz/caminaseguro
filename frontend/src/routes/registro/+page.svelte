<script lang="ts">
	/**
	 * @file Página de registro de usuarios.
	 * @description ARQUITECTURA: Actúa como un "Componente Contenedor" que orquesta
	 * la vista. Renderiza condicionalmente el formulario de registro o el mensaje
	 * de éxito basándose en el estado devuelto por la acción del servidor (`form`).
	 */
	import Card from '$lib/components/ui/Card.svelte';
	import RegistrationForm from '$lib/components/auth/RegistrationForm.svelte';
	import RegistrationSuccess from '$lib/components/auth/RegistrationSuccess.svelte';

	type FormState = {
		nombre?: string;
		email?: string;
		error?: string;
		errors?: {
			nombre?: string;
			email?: string;
			password?: string;
		};
		success?: boolean;
		message?: string;
	};

	let { form }: { form?: FormState } = $props();
</script>

<svelte:head>
	<title>Registro - CaminaSeguro</title>
</svelte:head>

<div class="flex flex-grow items-center justify-center p-4">
	<Card>
		{#snippet header()}
			<div class="text-center">
				<h1 class="text-2xl font-bold text-gray-900 dark:text-white">Crear una Cuenta</h1>
				<p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
					Únete a CaminaSeguro para proteger tus trayectos.
				</p>
			</div>
		{/snippet}

		{#if form?.success && form.message}
			<RegistrationSuccess message={form.message} />
		{:else}
			<RegistrationForm {form} />
		{/if}
	</Card>
</div>
