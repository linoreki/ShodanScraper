import requests
from bs4 import BeautifulSoup
import argparse

# Configuración de la URL y los encabezados
base_url = "https://www.shodan.io/search"
query = '"'  # Cambia esto según tu consulta
headers = {
    "Host": "www.shodan.io",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.shodan.io/dashboard?language=en",
    "Connection": "close",
    "Cookie": 'polito=""' # Cambia esto 
}

# Configuración de ArgumentParser para obtener el parámetro -t
def parse_args():
    parser = argparse.ArgumentParser(description="Scraping de Shodan para obtener IPs y puertos.")
    parser.add_argument("-t", "--times", type=int, required=True, help="Número de veces que se debe hacer la búsqueda.")
    return parser.parse_args()

# Función principal de scraping
def scrape_shodan(times):
    with open("ips_puertos.txt", "a") as file:  # Usamos "a" para agregar al archivo
        for i in range(times):  # Repetir la consulta 'times' veces
            print(f"Ejecutando búsqueda número {i + 1}...")
            page = 1  # Comenzamos en la primera página para cada nueva ejecución
            while True:  # Haremos el scraping mientras haya páginas
                params = {"query": query, "page": page}

                # Realiza la solicitud GET
                response = requests.get(base_url, headers=headers, params=params)

                if response.status_code != 200:
                    print(f"Error en la página {page}: {response.status_code}")
                    break

                # Analiza el HTML
                soup = BeautifulSoup(response.text, "html.parser")

                # Busca las direcciones IP y puertos
                results = soup.find_all("div", class_="result")

                if not results:
                    print(f"No hay más resultados en la página {page}. Finalizando búsqueda {i + 1}.")
                    break  # Salir del bucle si no hay más resultados en esta página

                for result in results:
                    ip_element = result.find("li", class_="hostnames text-secondary")
                    link_element = result.find("a", {"target": "_blank", "rel": "noopener noreferrer nofollow"})

                    # Extrae la IP y el puerto
                    ip = ip_element.text if ip_element else "No IP"
                    port = link_element["href"].split(":")[-1] if link_element else "No Port"

                    # Escribe los resultados en el archivo
                    file.write(f"{ip} {port}\n")
                    print(f"IP: {ip}, Puerto: {port}")

                page += 1  # Avanzamos a la siguiente página

    print("Scraping completado. Resultados guardados en ips_puertos.txt.")

# Ejecutar el script
if __name__ == "__main__":
    args = parse_args()  # Obtener los argumentos
    scrape_shodan(args.times)  # Ejecutar el scraping
