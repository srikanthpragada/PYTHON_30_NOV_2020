import requests

user = input("Enter git username :")
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code == 404:
    print("Sorry! User not found!")
    exit(1)
elif resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit(2)

details = resp.json()  # Convert JSON to Dict
for key, value in details.items():
    print(f"{key:20} {value}")
