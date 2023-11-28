from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import os

load_dotenv()  # This loads the .env file variables into the environment

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


auth_response = requests.post(
    'https://accounts.spotify.com/api/token',
    auth = HTTPBasicAuth(client_id, client_secret),
    data={'grant_type': 'client_credentials'}
)
auth_response_data = auth_response.json()
access_token = auth_response_data.get('access_token')
artist_id = '2FgHPfRprDaylrSRVf1UlN?si=iKm5gyi4SM2BRrULYoE6Eg'

headers = {
    'Authorization' : f'Bearer {access_token}'
}


def artist_data(artist_id):
    artist_response = requests.get(
        f'https://api.spotify.com/v1/artists/{artist_id}',
        headers = headers
    )
    return artist_response



print(artist_data(artist_id).json())

