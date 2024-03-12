import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://brockhoferart.com/meta-pcs-case"

# Obtener el contenido HTML de la página
response = requests.get(url)
html = response.content

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todas las etiquetas de imagen (img) con una clase específica
img_tags = soup.find_all('img', class_='cover__img js-lazy')  # Reemplaza 'tu_clase_especifica' con la clase real

# Crear una lista para almacenar las URL de las imágenes
image_urls = []

# Obtener las URL de las imágenes y añadirlas a la lista
for i in img_tags:
    src = i.get('src')
    image_url = urljoin(url, src)
    image_urls.append(image_url)

# Descargar y guardar cada imagen con su ID
for i, image_url in enumerate(image_urls):
    image_data = requests.get(image_url).content
    img_file = open(f'imagen_{i + 1}.jpg', 'wb')
    img_file.write(image_data)
    img_file.close()

print("Imágenes descargadas exitosamente.")
