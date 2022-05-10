import requests

def get_cotation():
    request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    request_dic = request.json()

    dolar_cotation =