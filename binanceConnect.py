import requests


def get_assets_list():
    url = 'https://api.binance.com/api/v1/exchangeInfo'
    assets_list = []

    try:
        response = requests.get(url)
        data = response.json()
        data = data["symbols"]

        for key in data:
            if not key["baseAsset"] in assets_list:
                assets_list.append(key["baseAsset"])
    except requests.exceptions.RequestException:
        exit("Не могу подключиться к {0}. Проверьте правильность ссылки или повторите позже".format(url))

    # if response.status_code == 404:
    #     assets_list.append("404")
    #     print("HELLO")
    # elif response.status_code == 200:


    return assets_list, url
