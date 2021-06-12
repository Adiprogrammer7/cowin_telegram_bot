import requests
from datetime import datetime
from playsound import playsound
from time import sleep
import json
import os

current_date = datetime.today().strftime('%d-%m-%Y')
district_id = 363  #374, state_id = 21
notification = "gamey_notification.wav"
telegram_key = os.environ['cowin_telegram_bot']

results = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(district_id, current_date))
results = results.json()

def check_slots():
	noti_flag = 0
	for result in results['sessions']:
		msg = {}
		if result["min_age_limit"] == 18 and result["fee_type"] == 'Free':
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
				print(msg) #msg will be a formatted string now
				print('-'*20)
				telegram_bot(msg)
				noti_flag = 1
	return noti_flag

def telegram_bot(msg):
	requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id=1003584231&text={}".format(telegram_key, msg))


while True:
	if check_slots():
		playsound(notification)
	sleep(15)