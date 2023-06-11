# Web Scraping utilizando Python

Este es un ejemplo básico de cómo utilizar Python para realizar web scraping, extraer datos de una página web y analizarlos utilizando las bibliotecas `requests` y `BeautifulSoup`.

## Requisitos previos
Asegúrate de tener las siguientes bibliotecas instaladas antes de ejecutar el código:
- requests
- beautifulsoup4

Puedes instalar estas bibliotecas utilizando `pip` con el siguiente comando:
```
pip install requests beautifulsoup4
```

## Descripción del código
El código muestra cómo realizar una solicitud GET a una página web específica y extraer datos del contenido HTML utilizando BeautifulSoup.

1. Importamos las bibliotecas necesarias:
   ```python
   import requests
   from bs4 import BeautifulSoup
   ```

2. Especificamos la URL de la página web a la que queremos hacer la solicitud GET:
   ```python
   url = "Escribe aquí la URL. Ejemplo: (https://www.ejemplo.com/)"
   ```

3. Hacemos la solicitud GET a la página web utilizando la biblioteca `requests`:
   ```python
   response = requests.get(url)
   ```

4. Verificamos si la solicitud fue exitosa (código de respuesta 200):
   ```python
   if response.status_code == 200:
   ```

5. Si la solicitud fue exitosa, obtenemos el contenido HTML de la página:
   ```python
   html_content = response.text
   ```

6. Creamos un objeto `BeautifulSoup` para analizar el contenido HTML:
   ```python
   soup = BeautifulSoup(html_content, "html.parser")
   ```

7. A partir de aquí, puedes utilizar los métodos y atributos de `soup` para buscar elementos específicos en el HTML y extraer la información que necesitas. En el ejemplo, mostramos cómo obtener todos los enlaces de la página:
   ```python
   links = soup.find_all("a")
   for link in links:
       print(link.get("href"))
   ```

8. Si la solicitud no fue exitosa, mostramos un mensaje de error junto con el código de respuesta:
   ```python
   else:
       print("Error al realizar la solicitud:", response.status_code)
   ```

Recuerda que al realizar web scraping, debes asegurarte de cumplir con los términos de servicio del sitio web y respetar las políticas de uso aceptable. Además, ten en cuenta que la estructura del HTML de una página puede variar, por lo que es posible que necesites ajustar tu código según la página que estés analizando.
