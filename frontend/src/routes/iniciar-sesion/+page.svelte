<script lang="ts">
	/**
	 * @file Página de inicio de sesión.
	 * @description Renderiza la estructura de la tarjeta y pasa los
	 * datos del formulario (`form`) al componente hijo `LoginForm`.
	 */
	import Card from '$lib/components/ui/Card.svelte';
	import LoginForm from '$lib/components/auth/LoginForm.svelte';

	type FormState = {
		email?: string;
		error?: string;
		errors?: {
			email?: string;
			password?: string;
		};
	};

	let { form }: { form?: FormState } = $props();
</script>

<svelte:head>
	<title>Iniciar Sesión - CaminaSeguro</title>
</svelte:head>

<div class="flex flex-grow items-center justify-center p-4">
	<Card>
		{#snippet header()}
			<div class="text-center">
				<h1 class="text-2xl font-bold text-gray-900 dark:text-white">Iniciar Sesión</h1>
				<p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
					Accede a tu cuenta para continuar.
				</p>
			</div>
		{/snippet}

		<LoginForm {form} />
	</Card>
</div>
