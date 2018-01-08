import requests


def get_assets_list():
    url = 'https://www.binance.com/exchange/public/product'
    assets_list = []

    try:
        response = requests.get(url)
        data = response.json()
        data = data["data"]

        for key in data:
            if not key["baseAsset"] in assets_list:
                assets_list.append(key["baseAsset"])
    except requests.exceptions.RequestException:
        exit("Не могу подключиться к {0}. Проверьте правильность ссылки или повторите позже".format(url))

    return assets_list
