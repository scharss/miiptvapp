from flask import Flask, render_template
import re # Para un parsing un poco más robusto del M3U

app = Flask(__name__)

def parse_m3u(filepath="lista.m3u"):
    """
    Parsea un archivo M3U y devuelve una lista de diccionarios de canales.
    Cada diccionario contiene 'name' y 'url'.
    """
    channels = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        channel_name = None
        channel_url = None
        # Patrón para extraer atributos comunes de #EXTINF
        # ej: #EXTINF:-1 tvg-id="id" tvg-name="nombre" tvg-logo="logo.png" group-title="Grupo",Nombre visible del canal
        extinf_pattern = re.compile(r'#EXTINF:-1(?:.*tvg-name="([^"]+)")?.*,(.*)')
        extinf_simple_pattern = re.compile(r'#EXTINF:-1,(.*)') # Para #EXTINF más simples

        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith("#EXTINF:"):
                match = extinf_pattern.match(line)
                if match:
                    # Si tvg-name está presente y no vacío, usarlo, sino usar el nombre visible
                    name_from_tvg = match.group(1)
                    name_visible = match.group(2)
                    channel_name = name_from_tvg if name_from_tvg and name_from_tvg.strip() else name_visible
                else:
                    simple_match = extinf_simple_pattern.match(line)
                    if simple_match:
                        channel_name = simple_match.group(1)
                    else:
                        channel_name = "Canal Desconocido" # Fallback

            elif channel_name and (line.startswith("http://") or line.startswith("https://")):
                channel_url = line
                channels.append({"name": channel_name.strip(), "url": channel_url})
                channel_name = None # Reset para el próximo canal
                channel_url = None

    except FileNotFoundError:
        print(f"Error: El archivo M3U '{filepath}' no fue encontrado.")
        return [] # Devuelve lista vacía si no se encuentra el archivo
    except Exception as e:
        print(f"Error al parsear el archivo M3U: {e}")
        return [] # Devuelve lista vacía en caso de otro error
    return channels

@app.route('/')
def index():
    # MUY IMPORTANTE: Asegúrate de que 'lista.m3u' solo contenga streams legales y FTA.
    # La responsabilidad del contenido de 'lista.m3u' es tuya.
    channel_data = parse_m3u("lista.m3u")
    if not channel_data:
        print("No se cargaron canales. Verifica 'lista.m3u' o los mensajes de error.")
    return render_template('index.html', channels=channel_data)

if __name__ == '__main__':
    # Para desarrollo: app.run(debug=True)
    # Para producción, usa un servidor WSGI como Gunicorn o Waitress.
    app.run(host='0.0.0.0', port=5000, debug=True)