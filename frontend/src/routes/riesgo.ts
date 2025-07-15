export type Riesgo = 'bajo' | 'medio' | 'alto';

export interface ResultadoRiesgo {
	nivel: Riesgo;
	mensaje: string;
}

export function evaluarRiesgo(): ResultadoRiesgo {
	try {
		const hora: number = new Date().getHours();

		if (isNaN(hora)) throw new Error('Hora inválida');

		if (hora < 5) {
			return {
				nivel: 'alto',
				mensaje: 'Es madrugada. Evita caminar solo y activa el modo seguro.'
			};
		}

		if (hora < 18) {
			return {
				nivel: 'medio',
				mensaje: 'Es de día. Mantente alerta en zonas desconocidas.'
			};
		}

		return {
			nivel: 'alto',
			mensaje: 'Es de noche. Camina acompañado o usa la app en modo seguro.'
		};
	} catch (error) {
		console.error('Error en evaluarRiesgo:', error);
		return {
			nivel: 'alto',
			mensaje: 'No se pudo calcular el riesgo. Activa el modo seguro por precaución.'
		};
	}
}