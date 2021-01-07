import requests

user = 'srikanthpragada'
resp = requests.get(f"https://api.github.com/users/{user}/repos")

if resp.status_code == 404:
    print("No repos or user found!")
    exit(1)

repos = resp.json()  # Convert JSON to Dict
for repo in repos:
    print(repo['name'])
