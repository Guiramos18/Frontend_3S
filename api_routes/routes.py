import requests
from flask import request

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f"{base_url}/breeds"

    headers = {
        "x-api-key": "live_UDzRW87EazvQeWs6mi61B9bpmXTdesQZPT6UtnD55SqVjUhhOnycHfYyE1o6PteH"
    }

    resposta = requests.get(url, headers=headers)

    return resposta.json()

def get_image():
    url = "https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)
    return resposta.json()[0]