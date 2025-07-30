# Frontend (SvelteKit)

Este directorio contiene la aplicación web del proyecto _**CaminaSeguro**_, construida con SvelteKit, TypeScript y Tailwind CSS.

## Requisitos Previos

- Node.js 20.x o superior
- `pnpm` (se puede instalar con `npm install -g pnpm`)

## Instalación y Configuración

1. **Instalar las dependencias:**

   ```bash
   pnpm install
   ```

2. **Configurar las variables de entorno:**
   - Crear una copia del archivo `.env.example` y renombrarlo a `.env`.
   - Asegurarse de que la variable `BACKEND_API_BASE_URL` apunte a la URL donde se está ejecutando el backend (por defecto, `http://127.0.0.1:8000`).

## Ejecución en Desarrollo

Para iniciar el servidor de desarrollo de SvelteKit, ejecutar:

```bash
pnpm dev
```

La aplicación estará disponible en `http://localhost:5173`.

## Construcción y Previsualización para Producción

1. **Construir la Aplicación (Build)**

   Este comando compila y optimiza todo el código (Svelte, TypeScript, CSS) en un conjunto de archivos eficientes y listos para producción.

   ```bash
   pnpm build
   ```

   El proceso generará una versión final de la aplicación dentro del directorio `.svelte-kit/output`.

2. **Previsualizar la Aplicación (Preview)**

   Una vez construida, se puede iniciar un servidor local que sirva los archivos de producción para verificar su comportamiento.

   ```bash
   pnpm preview
   ```

La aplicación estará disponible en la URL que indique la terminal (comúnmente `http://localhost:4173`).
