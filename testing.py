from time import sleep
import requests
from datetime import datetime

current_date = datetime.today().strftime('%d-%m-%Y')

requests.get("https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/sendMessage?chat_id=1003584231&text=hello world")
time.sleep(5)
requests.get("https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/sendMessage?chat_id=1003584231&text={}".format(current_date))