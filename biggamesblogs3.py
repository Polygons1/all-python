import xmltodict
import requests
import json

xmldict = dict(xmltodict.parse(requests.get("https://bigblog-storage.s3.amazonaws.com/").text))

xmldictv = xmldict.values()

print(xmldictv)