# TODO: make it more dynamic and versatile for other users like chatid, ability to select their location.
# 1003584231 chat id
# https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/getUpdates
# https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/sendMessage?chat_id=1003584231&text=hello
# https://api.telegram.org/bot1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs/sendMessage?chat_id=1003584231&text=```trying\n%20to%20make%20\n%20newline```&parse_mode=MarkdownV2

import requests
from datetime import datetime
from playsound import playsound
from time import sleep
import json
import os

current_date = datetime.today().strftime('%d-%m-%Y')
current_time = datetime.now().strftime("%H:%M:%S")
district_id = 363  #374, state_id = 21
notification = "gamey_notification.wav"
telegram_key = os.environ['cowin_telegram_bot']
end_log = "- at {} https://www.cowin.gov.in/home".format(current_time)

results = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(district_id, current_date))
results = results.json()

def telegram_bot(msg):
	requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id=1003584231&text={}".format(telegram_key, msg))

def check_slots():
	for result in results['sessions']:
		msg = {}
		if result["min_age_limit"] == 45 and result["fee_type"] == 'Free':
			if result["available_capacity"] == 0:
				msg['Name'] = result['name']
				msg['Address'] = result['address']
				msg['Pincode'] = result['pincode']
				msg['Total_doses'] = result['available_capacity']
				msg['Dose_1'] = result['available_capacity_dose1']
				msg['Dose_2'] = result['available_capacity_dose2']
				msg['Vaccine'] = result['vaccine']
				msg = json.dumps(msg)
				msg = msg.replace("{", "")
				msg = msg.replace("}", "")
				msg = msg.replace('"', "")
				msg = msg.replace(", ", "\n")
				telegram_bot(msg) #msg will be a formatted string now
				print(msg) 
				print('-'*20)
	playsound(notification)
	telegram_bot(end_log)

while True:
	check_slots()
	sleep(15)