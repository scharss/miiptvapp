# Reproductor IPTV Legal con Flask

Esta es una sencilla aplicación web desarrollada con Python y Flask que permite reproducir canales de televisión IPTV desde un archivo M3U local. Está diseñada para visualizar canales de televisión abiertos (Free-to-Air, FTA) que sean legales y de libre transmisión en tu región.

**¡IMPORTANTE! La legalidad del uso de esta aplicación depende enteramente del contenido del archivo `lista.m3u`. El usuario es el único responsable de asegurarse que los canales en la lista M3U son legales y que tiene derecho a visualizarlos en su ubicación geográfica.** Este software es solo una herramienta y no incluye ningún contenido ni lista de canales por defecto (aparte de un ejemplo básico en las instrucciones).

## Características

*   Carga canales desde un archivo `lista.m3u` local. Por ejemplo [https://iptv-org.github.io/iptv/index.m3u](https://iptv-org.github.io/iptv/index.m3u)
*   Interfaz simple con una lista de canales y un reproductor de video.
*   Utiliza HTML5 Video y `hls.js` para reproducir streams HLS (.m3u8).
*   Fácil de configurar y ejecutar.

## Requisitos Previos

*   Python 3.7 o superior
*   pip (gestor de paquetes de Python)
*   Un navegador web moderno

## Instalación y Configuración

1.  **Clonar el repositorio (o descargar los archivos):**
    ```bash
    git clone https://tu_repositorio_git.com/tu_usuario/mi_iptv_app.git
    cd mi_iptv_app
    ```
    Si no usas Git, simplemente descarga los archivos (`app.py`, `requirements.txt`, el directorio `templates/` con `index.html` y crea un `lista.m3u`).

2.  **Crear y activar un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    ```
    *   En Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Crear/Obtener tu archivo `lista.m3u`:**
    *   Crea un archivo llamado `lista.m3u` en el directorio raíz del proyecto (junto a `app.py`).
    *   Puebla este archivo con los enlaces a los streams de canales FTA legales. Puedes buscar listas como las del proyecto `iptv-org/iptv` en GitHub, pero **verifica siempre la legalidad de cada canal**.
    *   **Ejemplo de formato para `lista.m3u`:**
        ```m3u
        #EXTM3U

        #EXTINF:-1 tvg-name="Nombre del Canal 1" group-title="Grupo",Nombre del Canal 1 a Mostrar
        https://servidor.com/stream1.m3u8

        #EXTINF:-1 tvg-name="Nombre del Canal 2",Nombre del Canal 2 a Mostrar
        http://otroservidor.net/canal.ts
        ```
    *   **Recuerda:** La responsabilidad sobre el contenido de `lista.m3u` es tuya.

## Uso

1.  **Ejecutar la aplicación Flask:**
    Desde el directorio raíz del proyecto (donde está `app.py` y con el entorno virtual activado):
    ```bash
    python app.py
    ```
    La aplicación se ejecutará por defecto en `http://127.0.0.1:5000/` (o `http://localhost:5000/`).

2.  **Abrir en el navegador:**
    Abre tu navegador web y navega a `http://127.0.0.1:5000/`.

3.  **Seleccionar un canal:**
    Haz clic en un canal de la lista de la izquierda para empezar a reproducirlo en el reproductor de la derecha.

## Despliegue (Opcional - Producción)

Para un entorno de producción, no se recomienda usar el servidor de desarrollo de Flask (`app.run()`). En su lugar, utiliza un servidor WSGI como Gunicorn o Waitress.

**Ejemplo con Gunicorn (Linux/macOS):**
```bash
pip install gunicorn
gunicorn --workers 4 --bind 0.0.0.0:8000 app:app
