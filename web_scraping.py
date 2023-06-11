import requests
from bs4 import BeautifulSoup

# Realizar una solicitud GET a la página web
url = "Escribe aquí la URL. Ejemplo: (https://www.ejemplo.com/)"
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener el contenido HTML de la página
    html_content = response.text

    # Crear un objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Extraer datos de la página
    # Aquí puedes utilizar los métodos y atributos de BeautifulSoup para buscar elementos específicos en el HTML y extraer la información que necesitas

    # Ejemplo: Obtener todos los enlaces de la página
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))

else:
    print("Error al realizar la solicitud:", response.status_code)
