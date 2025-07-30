/**
 * @file Contiene la configuración de contenido para la página de inicio.
 * @description centralizar datos estáticos como este en un archivo
 * de configuración hace que el contenido sea más fácil de gestionar y modificar
 * sin tener que tocar la lógica de los componentes de Svelte (Clean Code).
 */
export const seccionesInfo = [
	{
		title: 'Visión',
		content:
			'Ser una aplicación confiable y ampliamente utilizada para garantizar la seguridad de las personas en sus trayectos diarios, mediante la tecnología y la solidaridad comunitaria.',
		delay: 100
	},
	{
		title: 'Misión',
		content:
			'Proveer una plataforma que permita a cualquier persona sentirse acompañada virtualmente en momentos de inseguridad, activando alertas en tiempo real hacia contactos de confianza o vecinos cercanos.',
		delay: 200
	},
	{
		title: '¿Para qué sirve?',
		content:
			'CaminaSeguro permite al usuario activar un "modo riesgo" si se siente inseguro mientras se desplaza. Esta señal alerta a un familiar o vecino, quien puede acompañarlo de forma virtual y recibir su ubicación en tiempo real.',
		delay: 300
	}
];