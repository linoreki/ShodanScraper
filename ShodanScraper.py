import requests
from bs4 import BeautifulSoup
import argparse

# Configurar el analizador de argumentos
parser = argparse.ArgumentParser(description="Script para obtener IPs y puertos desde Shodan.")
parser.add_argument("--cookie", type=str, required=False, default="", help="Cookie de autenticación para Shodan.")
parser.add_argument("--query", type=str, required=True, help="Query de búsqueda en Shodan.")
args = parser.parse_args()

# Variables configuradas por argumentos
cookie = args.cookie
query = args.query

# URL base y parámetros
url = "https://www.shodan.io/search"
params = {"query": query}
headers = {
    "Host": "www.shodan.io",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.shodan.io/dashboard?language=en",
    "Connection": "close",
}

# Agregar cookie si se proporciona
if cookie:
    headers["Cookie"] = cookie

# Realizar la solicitud GET
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    # Analizar el HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraer resultados
    results = soup.find_all("div", class_="result")
    
    with open("ips_puertos.txt", "w") as file:
        for result in results:
            ip_element = result.find("li", class_="hostnames text-secondary")
            link_element = result.find("a", {"target": "_blank", "rel": "noopener noreferrer nofollow"})
            
            # Extraer la IP y el puerto
            ip = ip_element.text if ip_element else "No IP"
            port = link_element["href"].split(":")[-1] if link_element else "No Port"
            
            file.write(f"{ip} {port}\n")
            print(f"IP: {ip}, Puerto: {port}")
else:
    print(f"Error al acceder al sitio: {response.status_code}")
