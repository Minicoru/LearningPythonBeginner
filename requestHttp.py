import requests

# URL de la API
url = "https://jsonplaceholder.typicode.com/todos"

# Haciendo una solicitud GET
response = requests.get(url)

# Verificando si la solicitud tuvo éxito
if response.status_code == 200:
    # Imprimiendo la respuesta en formato JSON
    data = response.json()
    print(data)
else:
    # Imprimiendo el código de estado de la respuesta
    print("Error con la solicitud, código de estado:", response.status_code)
