import requests

resp = requests.get(f"https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(2)

countries = resp.json()  # Convert Array of JSON objects to list of Dict
for c in sorted(countries, key=lambda c: c['population'], reverse=True)[:10]:
    print(f"{c['name'][:40]:40} {c['capital']:30} {c['population']:10}")
