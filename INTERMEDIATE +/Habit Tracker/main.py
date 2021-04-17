import requests
from datetime import datetime

#--------------------LINK TO SITE----------------------
# https://pixe.la/v1/users/jaygaur99/graphs/graph1.html
#----------------------------------------------------

today = datetime.now()
# today = datetime(2021, 4, 16)
DATE = today.strftime("%Y%m%d")
USERNAME = "jaygaur99"
TOKEN = ""# ENTER YOUR TOKEN HERE
GRAPHID = 'graph1'
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPHID,
    'name': 'Study Minutes',
    "unit": 'Minutes',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post To Graph1
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_data = {
    'date': DATE,
    'quantity': "220",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Update pixel in Graph
update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}'

new_pixel_data = {
    'quantity': "160"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete pixel from Graph
delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}'

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)