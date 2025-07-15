<script lang="ts">
	<!-- import Header from '$lib/components/Header.svelte'; -->
	<!-- import Footer from '$lib/components/Footer.svelte'; -->
	import '../../app.css';
</script>

<div class="min-h-screen bg-gray-100 font-sans dark:bg-gray-900">
	<Header />

	<main class="flex items-center justify-center p-4 md:p-8">
		<slot />
	</main>

	<Footer />
</div>

