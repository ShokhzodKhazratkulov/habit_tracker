import requests
from datetime import datetime
#_______________________________________CREATE_USER__________________________________________
USERNAME = "Your username"
TOKEN = "Your token"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
print(response.text)
#__________________________________________CREATE_GRAPH_______________________________________________
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Book Graph",
    "unit": "Pages",
    "type": "int",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN  #bazi websitelar header parametr qoshishni soraydi sekurity uchun
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.json())
#_________________________________________POST_RESULTS_______________________________________
today = datetime.now()

PIXELA_POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
POST_BODY = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Enter quantity of the pages. ")
}

response = requests.post(url=PIXELA_POST_ENDPOINT, json=POST_BODY, headers=headers)
print(response.text)

#__________________________________________HTTP_PUT___________________________________________
PIXELA_PUT_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}" #date is requared
PUT_BODY = {
    "quantity": "10",
}
response = requests.put(url=PIXELA_PUT_ENDPOINT, json=PUT_BODY, headers=headers)
print(response.text)

#_________________________________________HTTP_DELETE________________________________________
PIXELA_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
response = requests.delete(PIXELA_DELETE_ENDPOINT, headers=headers)
print(response.text)