export type Riesgo = 'bajo' | 'medio' | 'alto';

export function evaluarRiesgo(): { nivel: Riesgo; mensaje: string } {
	const hora = new Date().getHours();

	let nivel: Riesgo;
	let mensaje: string;

	if (hora >= 0 && hora < 5) {
		nivel = 'alto';
		mensaje = 'Es de madrugada. Te recomendamos evitar caminar solo y compartir tu ubicación.';
	} else if (hora >= 5 && hora < 18) {
		nivel = 'medio';
		mensaje = 'Día activo. Mantente alerta a tu entorno.';
	} else {
		nivel = 'alto';
		mensaje = 'Es de noche. Si te sientes inseguro, activa el modo de emergencia.';
	}

	return { nivel, mensaje };
}