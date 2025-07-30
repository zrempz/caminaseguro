import 'leaflet/dist/leaflet.css';
import type { Map, Marker } from 'leaflet';
import type { DatosGeolocalizacion } from '$lib/types';

/**
 * @file Módulo de servicio para encapsular la lógica de geolocalización.
 */
/**
 * Nivel de zoom inicial al centrar el mapa en la ubicación del usuario.
 * Un valor más alto significa más cerca del suelo.
 */
const ZOOM_INICIAL = 16;

/**
 * Nivel máximo de zoom permitido por la capa de teselas (tiles) de OpenStreetMap.
 */
const MAX_ZOOM_TILE_LAYER = 19;

/**
 * Almacena la instancia del módulo de Leaflet una vez que se ha cargado dinámicamente.
 * @private
 */
let L: typeof import('leaflet') | null = null;

/**
 * Inicializa una instancia de mapa de Leaflet en un elemento del DOM.
 * @async
 * @param {string} idElementoDOM - El 'id' del `<div>` donde se renderizará el mapa.
 * @param {DatosGeolocalizacion} ubicacionInicial - Objeto con la latitud y longitud para centrar el mapa.
 * @returns {Promise<{ mapa: Map; marcador: Marker }>} Una promesa que resuelve con la instancia del mapa y el marcador creados.
 * @description Realiza una importación dinámica de Leaflet para asegurar la compatibilidad con el Renderizado en Servidor (SSR).
 */
export async function inicializarMapa(
	idElementoDOM: string,
	ubicacionInicial: DatosGeolocalizacion
): Promise<{ mapa: Map; marcador: Marker }> {
	if (!L) {
		L = (await import('leaflet')).default;
	}

	const mapa = L.map(idElementoDOM).setView(
		[ubicacionInicial.latitud, ubicacionInicial.longitud],
		ZOOM_INICIAL
	);

	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: MAX_ZOOM_TILE_LAYER,
		attribution:
			'© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(mapa);

	const marcador = L.marker([ubicacionInicial.latitud, ubicacionInicial.longitud])
		.addTo(mapa)
		.bindPopup(`<b>¡Estás aquí!</b><br>Precisión: ${ubicacionInicial.precision.toFixed(2)} metros.`)
		.openPopup();

	return { mapa, marcador };
}

/**
 * Obtiene la ubicación geográfica actual del usuario a través de la API del navegador.
 * @async
 * @returns {Promise<DatosGeolocalizacion>} Una promesa que resuelve con los datos de la ubicación del usuario.
 * @throws {Error} Si el navegador no soporta la geolocalización.
 * @throws {GeolocationPositionError} Si el usuario deniega el permiso o si ocurre un error al obtener la posición.
 */
export function obtenerUbicacionActual(): Promise<DatosGeolocalizacion> {
	return new Promise((resolve, reject) => {
		if (!navigator.geolocation) {
			return reject(new Error('Tu navegador no soporta la geolocalización.'));
		}
		navigator.geolocation.getCurrentPosition(
			(posicion) => {
				resolve({
					latitud: posicion.coords.latitude,
					longitud: posicion.coords.longitude,
					precision: posicion.coords.accuracy
				});
			},
			(error: GeolocationPositionError) => {
				reject(error);
			}
		);
	});
}
