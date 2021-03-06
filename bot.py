import requests
from datetime import datetime, timedelta
from playsound import playsound
from time import sleep
import json
import os
 
telegram_key = os.environ['COWIN_TELEGRAM_BOT']  #your telegram bot token goes here
telegram_chat_id = os.environ['COWIN_TELEGRAM_CHAT_ID']  #chat id for telegram bot goes here
notification = "gamey_notification.wav"

headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

# reading district_id
with open("location.txt", "r") as file:
	district_id = file.read()

# list of dates of n days from current date
def days_to_fetch(days):
	days_li = []
	for i in range(days):
		day = (datetime.today() + timedelta(days=i)).strftime('%d-%m-%Y')
		days_li.append(day)
	return days_li

# msg to telegram
def telegram_bot(msg):
	requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(telegram_key, telegram_chat_id, msg))

def check_slots(results):
	cnt = 0
	for result in results["sessions"]:
		msg = {}
		if result["min_age_limit"] == 18 and result["fee_type"] == 'Free':
			if result["available_capacity_dose1"] != 0:
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
				print('-'*25)
				cnt += 1
	return cnt

if __name__ == '__main__':
	while True:
		days_li = days_to_fetch(3) #will check for these many days
		for day in days_li:
			results = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(district_id, day), headers=headers)
			results = results.json()
			cnt = check_slots(results)
			if cnt:
				playsound(notification)
				end_log = "- {} results at {} https://www.cowin.gov.in/home".format(cnt, day)
				print(end_log)
				telegram_bot(end_log)
		sleep(12)