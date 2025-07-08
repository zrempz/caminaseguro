<script lang="ts">
	import '../../app.css';

	let { children } = $props();
</script>

<div class="min-h-screen bg-gray-100 font-sans dark:bg-gray-900">
	<main class="flex items-center justify-center p-4 md:p-8">
		{@render children()}
	</main>
</div>
