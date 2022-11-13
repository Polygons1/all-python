import requests
import json

rbxid = input("Enter you're roblox id: ")
api = requests.get(f"https://api.roblox.com/users/{rbxid}")

username = json.loads(api.text)['Username']

print(f"Hi @{username}!")