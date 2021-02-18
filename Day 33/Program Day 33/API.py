import requests

# getting request from url
URL = "http://api.open-notify.org/iss-now.json"
response = requests.get(url=URL)
print(response)

# getting status of the the requested data
response.raise_for_status()

# accessing the requested json file from the data
data = response.json()
print(data)

# accessing the data inside json file
timestamp = data["timestamp"]
iss_position = data["iss_position"]
longitude = iss_position["longitude"]
latitude = iss_position["latitude"]
message = data["message"]
print(
    f"timestamp    = {timestamp}\niss position = {iss_position}\nlongitude    = {longitude}\nlatitude     = {latitude}\nmessage      = {message}")

response.close()
