CaminaSeguro

CaminaSeguro es una aplicación web cuyo propósito es acompañar virtualmente al usuario cuando este se sienta inseguro al desplazarse. Permite activar un modo de riesgo que alerta a familiares o vecinos, quienes pueden monitorear su situación en tiempo real.

Estilos de programación usados

Durante la implementación de los módulos del sistema se aplicaron varios estilos de programación que responden a buenas prácticas de ingeniería de software.

El estilo cookbook se utilizó en el archivo riesgo.ts, donde se aplica una lógica sencilla y directa para determinar el nivel de riesgo en función de la hora del día. Por ejemplo, si la hora es menor que 5, se devuelve un mensaje de alto riesgo. Este tipo de condicionales directos son característicos del estilo cookbook.

if (hora < 5) {
	return {
		nivel: 'alto',
		mensaje: 'Es madrugada. Evita caminar solo y activa el modo seguro.'
	};
}

El estilo pipeline se encuentra en el archivo +page.svelte, donde se observa un flujo lineal de acciones: al montar el componente se evalúa el riesgo, se obtienen los datos y luego se actualiza la interfaz. Esta secuencia de procesamiento en etapas es propia del estilo pipeline.

onMount(() => {
	const resultado = evaluarRiesgo();
	mensaje = resultado.mensaje;
	nivel = resultado.nivel;
});

También se aplica el estilo restful o reactivo en la interfaz. En +page.svelte, la presentación se basa directamente en variables de estado (nivel, mensaje) que cambian en tiempo real. Este enfoque permite que la UI reaccione automáticamente a los datos, sin manipulación directa del DOM.

<p class="text-sm mt-1 text-red-400 uppercase">Nivel de riesgo: {nivel}</p>
<p class="mt-2 text-lg italic text-yellow-300">{mensaje}</p>

Por último, se implementó el estilo de manejo de errores (error/exception handling) en riesgo.ts. En caso de que ocurra una excepción al obtener la hora actual, esta se captura y se registra usando console.error, y se devuelve un mensaje por defecto que indica al usuario que active el modo seguro. Esto permite mantener el flujo del sistema sin interrupciones graves y notificar adecuadamente la falla.

catch (error) {
	console.error('Error en evaluarRiesgo:', error);
	return {
		nivel: 'alto',
		mensaje: 'No se pudo calcular el riesgo. Activa el modo seguro por precaución.'
	};
}

En conjunto, estos estilos permiten construir un sistema robusto, claro y mantenible, que separa adecuadamente lógica y presentación, y responde correctamente ante eventos inesperados.
