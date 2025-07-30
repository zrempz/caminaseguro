<script lang="ts">
	/**
	 * @prop {string} name - Atributo 'name' para el FormData.
	 * @prop {string} label - Texto para el <label>.
	 * @prop {string} value - Valor del campo, enlazable con `bind:value`.
	 * @prop {string} [type='text'] - Tipo del input.
	 * @prop {string} [error] - Mensaje de error a mostrar.
	 * @prop {boolean} [isPassword=false] - Indica si es un campo de contraseña para mostrar el ícono del ojo.
	 * @prop {boolean} [showPassword] - Estado de visibilidad de la contraseña, enlazable.
	 */
	let {
		name,
		label,
		value = $bindable(),
		type = 'text',
		error = '',
		isPassword = false,
		showPassword = $bindable()
	}: {
		name: string;
		label: string;
		value: string;
		type?: string;
		error?: string;
		isPassword?: boolean;
		showPassword?: boolean;
	} = $props();
</script>

<div>
	<label for={name} class="block text-sm font-medium text-gray-900 dark:text-gray-200"
		>{label}</label
	>
	<div class="relative mt-2">
		<input
			id={name}
			{name}
			{type}
			bind:value
			class="block w-full rounded-md border-0 bg-white/5 px-3 py-1.5 text-gray-900 shadow-sm ring-1 ring-gray-300 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-blue-600 focus:ring-inset dark:bg-white/5 dark:text-white dark:ring-white/10"
			class:ring-red-500={error}
			aria-invalid={!!error}
		/>
		{#if isPassword}
			<button
				type="button"
				onclick={() => (showPassword = !showPassword)}
				class="absolute inset-y-0 right-0 flex items-center pr-3"
				aria-label="Alternar visibilidad de contraseña"
			>
			</button>
		{/if}
	</div>
	{#if error}
		<p class="mt-2 text-sm text-red-600">{error}</p>
	{/if}
</div>
