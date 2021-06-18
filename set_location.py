import requests

headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

def get_state_id(state):
	results = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states", headers=headers)
	results = results.json()
	results = results["states"]
	for each_result in results:
		if each_result["state_name"].lower() == state.lower():
			return each_result["state_id"]

def get_district_id(state_id, district):
	results = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_id), headers=headers)
	results = results.json()
	results = results["districts"]
	for each_result in results:
		if each_result["district_name"].lower() == district.lower():
			return each_result["district_id"]

if __name__ == '__main__':
	state = input("Enter state name: ")
	district = input("Enter district name: ")
	state_id = get_state_id(state)
	district_id = get_district_id(state_id, district)
	if district_id:
		with open("location.txt", "w") as file:
			file.write(str(district_id))  
	else:
		print("Invalid input!")