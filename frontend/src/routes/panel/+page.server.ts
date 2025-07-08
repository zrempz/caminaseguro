import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const usuario = {
		nombre: 'John Doe',
		correo: 'johndoe@example.com',
		urlAvatar: ''
	};

	return {
		usuario: usuario
	};
};
