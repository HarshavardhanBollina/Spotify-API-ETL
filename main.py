import os
import requests
from requests import post,get
from dotenv import load_dotenv
from base64 import b64encode
import json

# Load the .env file before accessing environment variables
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = b64encode(credentials.encode()).decode()

    auth_url = "https://accounts.spotify.com/api/token"
    headers = {"Authorization": f"Basic {encoded_credentials}", "Content-Type": "application/x-www-form-urlencoded"}
    body = {"grant_type": "client_credentials"}

    response = requests.post(auth_url, headers=headers, data=body)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print("Failed to retrieve access token")
        print(response.json())
        return None
    
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_artist(artist_name, token):
    search_url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = search_url + query

    response = get(query_url, headers=headers)
    if response.status_code == 200:
        json_result = json.loads(response.content)
        # formatted_json_result = json.dumps(json_result, indent=4)
        # return formatted_json_result
        return json_result['artists']['items']
        
    else:
        print(f"Failed to search artist: {response.status_code}")
        print(response.json())
        return None



token = get_token()
result = search_artist("Thaman", token)
# for artist in result:
#     print(artist['name'])

# Assuming 'result' is your JSON object
artist_id = result['artists']['items'][0]['id']
print(artist_id)

