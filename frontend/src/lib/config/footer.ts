/**
 * @file Archivo de configuración para todo el contenido del pie de página.
 * @description Centraliza los datos para facilitar el mantenimiento y la coherencia,
 * separando la data de la capa de presentación.
 */

/**
 * Define la estructura de un enlace del pie de página.
 */
interface FooterLink {
	href: string;
	text: string;
}

/**
 * Enlaces para la columna "Explorar".
 * @type {FooterLink[]}
 */
export const exploreLinks: FooterLink[] = [
	{ href: '/features', text: 'Características' },
	{ href: '/about', text: 'Sobre Nosotros' },
	{ href: '/contact', text: 'Contacto' }
];

/**
 * Enlaces para la columna "Legal".
 * @type {FooterLink[]}
 */
export const legalLinks: FooterLink[] = [
	{ href: '/terms', text: 'Términos de Servicio' },
	{ href: '/privacy', text: 'Política de Privacidad' }
];

/**
 * Contenido del aviso de copyright.
 */
export const copyright = {
	brandName: 'CaminaSeguro',
	message: 'Todos los derechos reservados.'
};
