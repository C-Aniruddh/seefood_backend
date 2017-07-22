import requests
from pprint import pprint

USER_KEY = 'd2106ca14444ca76c6e8b5d51ebe430a'

locationUrlFromLatLong = "https://developers.zomato.com/api/v2.1/search?city_id=3&cuisine_id=304"
header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key" : USER_KEY}

response = requests.get(locationUrlFromLatLong, headers=header)

pprint(response.json())
