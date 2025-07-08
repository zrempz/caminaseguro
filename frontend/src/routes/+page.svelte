<script lang="ts">
  import { fade } from 'svelte/transition';
  import AOS from 'aos';
  import 'aos/dist/aos.css';
  import { onMount } from 'svelte';
  import { evaluarRiesgo } from './riesgo';

  let mensaje = '';
  let nivel = '';

  onMount(() => {
    AOS.init({ once: true, duration: 1000 });
    const resultado = evaluarRiesgo();
    mensaje = resultado.mensaje;
    nivel = resultado.nivel;
  });
</script>

<main class="bg-gray-900 text-white min-h-screen px-4 py-12 font-sans">
  <div class="max-w-4xl mx-auto space-y-10">

    <div class="text-center" data-aos="zoom-in">
      <h1 class="text-4xl font-bold">CaminaSeguro</h1>
      <p class="mt-2 text-lg italic text-yellow-300">{mensaje}</p>
      <p class="text-sm mt-1 text-red-400 uppercase">Nivel de riesgo: {nivel}</p>
    </div>

    <section class="bg-white/10 backdrop-blur p-6 rounded-xl shadow-md" data-aos="fade-up">
      <h2 class="text-2xl font-semibold text-yellow-400 mb-2">Visión</h2>
      <p>
        Ser una aplicación confiable y ampliamente utilizada para garantizar la seguridad de las personas en sus trayectos diarios, mediante la tecnología y la solidaridad comunitaria.
      </p>
    </section>

    <section class="bg-white/10 backdrop-blur p-6 rounded-xl shadow-md" data-aos="fade-up">
      <h2 class="text-2xl font-semibold text-yellow-400 mb-2">Misión</h2>
      <p>
        Proveer una plataforma que permita a cualquier persona sentirse acompañada virtualmente en momentos de inseguridad, activando alertas en tiempo real hacia contactos de confianza o vecinos cercanos.
      </p>
    </section>

    <section class="bg-white/10 backdrop-blur p-6 rounded-xl shadow-md" data-aos="fade-up">
      <h2 class="text-2xl font-semibold text-yellow-400 mb-2">¿Para qué sirve la app?</h2>
      <p>
        CaminaSeguro permite al usuario activar un "modo riesgo" si se siente inseguro mientras se desplaza. Esta señal alerta a un familiar o vecino, quien puede acompañarlo de forma virtual y recibir su ubicación en tiempo real.
      </p>
    </section>

  </div>
</main>
