# import requests
#
#
# class BotApi:
#     def send_message(self, token, chat_id, asset, debug):
#         if debug:
#             print('https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text="Новая валюта - {2}'.format(
#                 token, chat_id,
#                 asset))
#         requests.get(
#             'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text="Новая валюта - {2}'.format(
#                 token, chat_id,
#                 asset))
