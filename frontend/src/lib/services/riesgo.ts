export type Riesgo = 'bajo' | 'medio' | 'alto';

/**
 * Evalúa el nivel de riesgo basado en la hora actual
 *
 * @returns Objeto con nivel de riesgo y mensaje contextual
 */
export function evaluarRiesgo(): { nivel: Riesgo; mensaje: string } {
	const hora = new Date().getHours();

	const reglas: Record<Riesgo, { horas: number[]; mensaje: string }> = {
		bajo: {
			horas: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
			mensaje: 'Zona segura. Mantén precauciones básicas.'
		},
		medio: {
			horas: [18, 19, 20],
			mensaje: 'Día activo. Mantente alerta a tu entorno.'
		},
		alto: {
			horas: [...Array(6).keys(), 21, 22, 23],
			mensaje: 'Evita caminar solo. Comparte tu ubicación.'
		}
	};

	for (const [nivel, { horas, mensaje }] of Object.entries(reglas)) {
		if (horas.includes(hora)) {
			return { nivel: nivel as Riesgo, mensaje };
		}
	}

	return { nivel: 'alto', mensaje: 'Precaución extrema recomendada.' };
}