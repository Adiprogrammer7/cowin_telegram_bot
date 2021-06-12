# 1003584231 chat id
# https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/getUpdates
# https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/sendMessage?chat_id=1003584231&text=hello
# https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/sendMessage?chat_id=1003584231&text=```trying\n%20to%20make%20\n%20newline```&parse_mode=MarkdownV2

import requests
# d = 'hey \n my name is!'
# requests.get("https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/sendMessage?chat_id=1003584231&text={}".format(d))

import json
test1 = {}
test1['old'] = 'hello'
test1['new'] = 'heyyy'
print(test1)
msg = json.dumps(test1)
print(msg)
msg = msg.replace("{", "")
msg = msg.replace("}", "")
msg = msg.replace('"', "")
msg = msg.replace(",", "\n")
msg = msg.replace(" ", "")
msg = msg.replace(":", " = ")
print(msg)
