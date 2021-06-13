import requests
from datetime import datetime
import time
import json
import os

os.environ["TZ"] = "Asia/Kolkata"
time.tzset()

district_id = 374  
telegram_key = "1753315617:AAEOTzux5XHZANJX7qIIDa7oKlFhSXo_oJs"
current_date = datetime.today().strftime('%d-%m-%Y')
current_time = datetime.now().strftime("%H:%M:%S")
end_log = "- at {} https://www.cowin.gov.in/home".format(current_time)

results = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(district_id, current_date))
results = results.json()

def telegram_bot(msg):
	requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id=1003584231&text={}".format(telegram_key, msg))

def check_slots():
	for result in results['sessions']:
		msg = {}
		if result["min_age_limit"] == 18 and result["fee_type"] == 'Free':
			if result["available_capacity"] != 0:
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

	telegram_bot(end_log)

while True:
	check_slots()
	time.sleep(15)