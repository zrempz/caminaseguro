/**
 * @file Archivo central para las definiciones de tipos y modelos de datos de la aplicación.
 */

/**
 * Representa la estructura de un usuario autenticado en la aplicación.
 * Este tipo se utiliza para transportar los datos del usuario entre el frontend y el backend.
 */
export interface Usuario {
	id: string;
	email: string;
	nombre: string;
}

/**
 * Define la estructura para los datos de geolocalización obtenidos del navegador.
 * Este modelo de datos es utilizado por el servicio del mapa para renderizar la ubicación.
 */
export interface DatosGeolocalizacion {
	latitud: number;
	longitud: number;
	precision: number;
}
