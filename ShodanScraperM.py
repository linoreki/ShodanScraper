import requests
from bs4 import BeautifulSoup

# Configuración de la URL y los encabezados
base_url = "https://www.shodan.io/search"
query = ''  # Cambia esto según tu consulta
headers = {
    "Host": "www.shodan.io",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.shodan.io/dashboard?language=en",
    "Connection": "close",
    "Cookie": 'polito=""' #set this parameter
}

# Configuración de paginación
max_pages = 5  # Define el número máximo de páginas a iterar

with open("ips_puertos.txt", "w") as file:
    for page in range(1, max_pages + 1):
        print(f"Scraping página {page}...")
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
            print(f"No hay más resultados en la página {page}. Finalizando.")
            break
        
        for result in results:
            ip_element = result.find("li", class_="hostnames text-secondary")
            link_element = result.find("a", {"target": "_blank", "rel": "noopener noreferrer nofollow"})
            
            # Extrae la IP y el puerto
            ip = ip_element.text if ip_element else "No IP"
            port = link_element["href"].split(":")[-1] if link_element else "No Port"
            
            file.write(f"{ip} {port}\n")
            print(f"IP: {ip}, Puerto: {port}")

print("Scraping completado. Resultados guardados en ips_puertos.txt.")
