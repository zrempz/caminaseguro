<script lang="ts">
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte';

  import '../styles/global.css';

  let { children } = $props();
</script>

<Header />

<main>
  {@render children()}
</main>

<Footer />

<style>
  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    padding-top: 90px;
  }
</style>
