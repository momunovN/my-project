import time
import requests
import base64
from random import randint


message = input('Введите запрос:')
prompt = {
"modelUri": "art://b1gqmokukb7siapvkn2u/yandex-art/latest",
"generationOptions": {
  "seed": randint(10000, 2000000)
},
"messages": [
  {
    "weight": 1,
    "text": message
  }
]
}

url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVN3eD_D4rsCnw6hsHAv9HGCPW0hJDkYT5V3w6U"
}
response = requests.post(url=url, headers=headers, json=prompt)

result = response.json()
print(result)

operation_id = result['id']

operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"

while True:
    operation_response = requests.get(url=operation_url, headers=headers)
    operation_result = operation_response.json()
    if 'response' in operation_result:
        image_base64 =  operation_result['response']['image']
        break
    else:
        print('Ожидайте, изображение не готово')
        time.sleep(5)


image_data = base64.b64decode(image_base64)
with open('image.jpeg', 'wb') as image_file:
    image_file.write(image_data)

print('Изображение готово')