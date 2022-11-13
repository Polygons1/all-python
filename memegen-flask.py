import requests
import json
import flask

api = requests.get('https://api.imgflip.com/get_memes')

memes = json.loads(api.text)

open('memes.json', 'w').write(str(memes['data']))

meme = json.loads(open('memes.json', 'r').read())