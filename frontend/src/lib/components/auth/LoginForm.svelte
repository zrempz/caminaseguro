<script lang="ts">
	/**
	 * @file Componente que renderiza el formulario de inicio de sesión.
	 * @description Su única responsabilidad es mostrar los campos, gestionar el
	 * estado de carga y mostrar los errores que recibe como props.
	 */
	import { enhance } from '$app/forms';
	import FormInput from '$lib/components/ui/FormInput.svelte';
	import SubmitButton from '$lib/components/ui/SubmitButton.svelte';

	type FormState = {
		email?: string;
		error?: string;
		errors?: {
			email?: string;
			password?: string;
		};
	};

	let { form }: { form?: FormState } = $props();

	let email = $state(form?.email || '');
	let password = $state('');
	let showPassword = $state(false);
	let isLoading = $state(false);
</script>

<form
	method="POST"
	use:enhance={() => {
		isLoading = true;
		return async ({ update }) => {
			await update();
			isLoading = false;
		};
	}}
	class="space-y-6"
>
	<FormInput
		name="email"
		label="Correo Electrónico"
		type="email"
		bind:value={email}
		error={form?.errors?.email}
	/>
	<FormInput
		name="password"
		label="Contraseña"
		type="password"
		bind:value={password}
		error={form?.errors?.password}
		isPassword={true}
		bind:showPassword
	/>

	{#if form?.error}
		<p class="text-sm text-red-600 dark:text-red-400">{form.error}</p>
	{/if}

	<div class="text-right">
		<a
			href="/recuperar-contrasena"
			class="text-sm font-medium text-blue-600 hover:underline dark:text-blue-400"
			>¿Olvidaste tu contraseña?</a
		>
	</div>

	<SubmitButton {isLoading}>Acceder</SubmitButton>
</form>

<p class="mt-8 text-center text-sm text-gray-600 dark:text-gray-400">
	¿Aún no tienes cuenta?
	<a href="/registro" class="font-medium text-blue-600 hover:underline dark:text-blue-400"
		>Regístrate aquí</a
	>
</p>
