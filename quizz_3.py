import requests
import json
import sqlite3
lat = 41.785978
long = 44.743510
key = "31fadeb23ac040c04223d384ba340cde"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={key}"
resp = requests.get(url + "&units=metric")
header = resp.headers
status_code = resp.status_code
post = requests.post(url + "&units=metric")
result = resp.json()


with open('dataa.json', 'w') as file:
    json.dump (result, file, indent=4)
feels_like = result["main"]["feels_like"]
country = result["sys"]["country"]
visibility = result["visibility"]
timezone = result["timezone"]
print(country), print(feels_like)

connect = sqlite3.connect('weather.sqlite')
conn = connect.cursor()

# vqmnit bazas sadac shegvyavs chvens mier json failidan wamogebuli 4ve monacemi
data = (country, timezone, feels_like, visibility) 
conn.execute('''CREATE TABLE IF NOT EXISTS weather
        (country VARCHAR(50),
        timezone FLOAT,
        feels_like FLOAT,
        visibility FLOAT)''')
#placeholderad viyenebt ?-ebs da mat gadavcemt winaswar tuple-shi tavmoyril informacias
conn.execute('INSERT INTO weather VALUES (?, ?, ?, ?)', (data))
connect.commit()
connect.close()
