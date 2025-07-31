<script lang="ts">
	/**
	 * @file Layout para la sección del panel de usuario.
	 * @description Este layout envuelve todas las páginas que están dentro de '/panel'.
	 */
	import '../../app.css';
</script>

<div class="min-h-screen bg-gray-100 font-sans dark:bg-gray-900">
	<main class="flex items-center justify-center p-4 md:p-8">
		<slot />
	</main>
</div>
