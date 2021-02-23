import requests
import datetime
import os

# Getting today's date in YYYYMMDD format
today = datetime.date.today().strftime("%Y%m%d")

USER_NAME = "gokuldev"
PIXEL_TOKEN = os.environ.get("PIXEL_TOKEN")

# ENDPOINTS used
PIXEL_ENDPOINT = "https://pixe.la/v1/users"
PIXEL_GRAPH_CREATION_ENDPOINT = f"{PIXEL_ENDPOINT}/{USER_NAME}/graphs"
PIXEL_GRAPH_ADD_VALUE_ENDPOINT = f"{PIXEL_GRAPH_CREATION_ENDPOINT}/g1"
PIXEL_GRAPH_UPDATE_VALUE_ENDPOINT = f"{PIXEL_GRAPH_ADD_VALUE_ENDPOINT}/{today}"

# PARAMETERS used
USER_PARAMETERS = {
    "token": PIXEL_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

GRAPH_PARAMETERS = {
    "id": "g2",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

GRAPH_HEADER = {
    "X-USER-TOKEN": PIXEL_TOKEN
}

GRAPH_ADD_VALUE_PARAMETERS = {
    "date": today,
    "quantity": "10"
}

GRAPH_UPDATE_VALUE_PARAMETERS = {
    "quantity": "15"
}

"""Creating a user account in pixela """
# user_creation = requests.post(url=PIXEL_ENDPOINT, json=USER_PARAMETERS)
# print(user_creation.text)

"""Creating a graph"""
# graph_creation = requests.post(url=PIXEL_GRAPH_CREATION_ENDPOINT, json=GRAPH_PARAMETERS, headers=GRAPH_HEADER)
# print(graph_creation.text)

"""Posting Value to Graph Pixel"""
graph_add_value = requests.post(url=PIXEL_GRAPH_ADD_VALUE_ENDPOINT, json=GRAPH_ADD_VALUE_PARAMETERS, headers=GRAPH_HEADER)
print(graph_add_value.text)

"""Updating a pixel"""
graph_update_value = requests.put(url=PIXEL_GRAPH_UPDATE_VALUE_ENDPOINT, json=GRAPH_UPDATE_VALUE_PARAMETERS, headers=GRAPH_HEADER)
print(graph_update_value.text)

"""Deleting a Graph"""
delete_graph = requests.delete(url=f"{PIXEL_GRAPH_CREATION_ENDPOINT}/g2", headers=GRAPH_HEADER)
print(delete_graph.text)

