<script lang="ts">
	/**
	 * @file Componente que renderiza el formulario de registro.
	 * @description Su única responsabilidad es mostrar los campos de entrada,
	 * gestionar el estado de carga (`isLoading`) y mostrar los errores de validación
	 * que recibe como props.
	 */
	import { enhance } from '$app/forms';
	import FormInput from '$lib/components/ui/FormInput.svelte';
	import SubmitButton from '$lib/components/ui/SubmitButton.svelte';

	type FormState = {
		nombre?: string;
		email?: string;
		error?: string;
		errors?: {
			nombre?: string;
			email?: string;
			password?: string;
		};
	};

	let { form }: { form?: FormState } = $props();
	let estaCargando = $state(false);
	let passwordValue = $state('');
	let showPassword = $state(false);
</script>

<form
	method="POST"
	use:enhance={() => {
		estaCargando = true;
		return async ({ update }) => {
			await update();
			if (form?.errors) {
				passwordValue = '';
			}
			estaCargando = false;
		};
	}}
	class="space-y-6"
>
	<FormInput
		name="nombre"
		label="Nombre Completo"
		value={form?.nombre || ''}
		error={form?.errors?.nombre}
	/>
	<FormInput
		name="email"
		label="Correo Electrónico"
		type="email"
		value={form?.email || ''}
		error={form?.errors?.email}
	/>
	<FormInput
		name="password"
		label="Contraseña"
		type="password"
		bind:value={passwordValue}
		error={form?.errors?.password}
		isPassword={true}
		bind:showPassword
	/>

	{#if form?.error}
		<p class="mt-2 text-sm text-red-600 dark:text-red-400">{form.error}</p>
	{/if}

	<SubmitButton isLoading={estaCargando}>Registrarse</SubmitButton>
</form>

<p class="mt-8 text-center text-sm text-gray-600 dark:text-gray-400">
	¿Ya tienes una cuenta?
	<a href="/iniciar-sesion" class="font-medium text-blue-600 hover:underline dark:text-blue-400"
		>Inicia sesión</a
	>
</p>
