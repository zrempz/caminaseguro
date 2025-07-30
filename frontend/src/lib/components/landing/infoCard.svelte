<script lang="ts">
	/**
	 * @file Componente para mostrar una tarjeta de información con animación.
	 * @description SOLID (SRP): Su única responsabilidad es renderizar una sección
	 * de texto con un título. Recibe todos sus datos como props, haciéndolo
	 * completamente reutilizable y agnóstico al contexto.
	 */
	type Props = {
		title: string;
		content: string;
		delay: number;
	};
	let { title, content, delay }: Props = $props();
</script>

<section
	class="rounded-xl bg-white/80 p-6 shadow-lg backdrop-blur-sm dark:bg-gray-800/80"
	data-aos="fade-up"
	data-aos-delay={delay}
	role="article"
>
	<h2 class="mb-3 text-xl font-semibold text-blue-600 dark:text-blue-400">{title}</h2>
	<p class="leading-relaxed text-gray-700 dark:text-gray-300">{content}</p>
</section>