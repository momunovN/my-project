import requests
async def get_sovet(message_text):
    prompt = {
  "modelUri": "gpt://b1grci7geomp81nlt838/yandexgpt-lite",
  "completionOptions": {
    "stream": False,
    "temperature": 0.9,
    "maxTokens": "2000"
  },
  "messages": [
    {
      "role": "system",
      "text": "Ты - можешь дать совет в любой ситуации"
    },
    {
      "role": "user",
      "text": message_text
    }
  ]
}

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNzV7AGIF_Y3wPKz6WEndHBebpDW42Ti-90lNF"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    return result['result']['alternatives'][0]['message']['text']