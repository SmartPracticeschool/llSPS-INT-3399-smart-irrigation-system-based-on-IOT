
import requests

api_address='http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=403dec552ad1128a08f340f6d83f93d3'
city=input("city name :")

url = api_address + city

json_data = requests.get(url).json()

print(json_data)













