import requests
from datetime import datetime
from playsound import playsound
from time import sleep

current_date = datetime.today().strftime('%d-%m-%Y')
district_id = 374  #363 pune, state_id = 21
notification = "gamey_notification.wav"

results = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(district_id, current_date))
results = results.json()

def check_slots():
	noti_flag = 0
	for result in results['sessions']:
		if result["min_age_limit"] == 18 and result["fee_type"] == 'Free':
			if result["available_capacity"] != 0:
				print('Name: ', result['name'])
				print('Address: ', result['address'])
				print('Pincode: ', result['pincode'])
				print('Total_dose: ', result['available_capacity'])
				print('Dose_1: ', result['available_capacity_dose1'])
				print('Vaccine: ', result['vaccine'])
				print('----------------------------------')
				noti_flag = 1
	return noti_flag


while True:
	if check_slots():
		playsound(notification)
	sleep(12)