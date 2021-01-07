import requests


def get_density(c):
    try:
        return c['population'] // c['area']
    except:
        return 0


resp = requests.get(f"https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(2)

f = open("countries_density.txt", "wt")
countries = resp.json()  # Convert Array of JSON objects to list of Dict
for c in sorted(countries, key=lambda c: get_density(c), reverse=True):
    f.write(f"{c['name']},{c['population']}, {c['area']}, {get_density(c)}\n")

f.close()
