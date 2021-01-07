import requests

resp = requests.get(
    f"https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&offset=0&limit=100")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(2)

response = resp.json()
for entry in response['records']:
    print(f"{entry['city']:20} - {entry['pollutant_id']} -  {entry['pollutant_avg']}")
