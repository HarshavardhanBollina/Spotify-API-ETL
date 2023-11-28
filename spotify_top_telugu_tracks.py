import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

# api end point for telugu music - https://api.spotify.com/v1/browse/categories/0JQ5DAqbMKFIdOwkMWR5at
# category_id: 0JQ5DAqbMKFIdOwkMWR5at
# artist_id's
# 1-thaman - 2FgHPfRprDaylrSRVf1UlN?si=iKm5gyi4SM2BRrULYoE6Eg
# 2- dsp - 5sSzCxHtgL82pYDvx2QyEU?si=D46T52dOSHCBVtBS4ZLV9g
# 3- anirudh - 4zCH9qm4R2DADamUHMCa6O?si=bySYVkxwTs-vjQESOYKeow
# 4- Bheems Ceciroleo - 0L5f9aJIaxQXTipZ7uQYiC?si=JvmPkEd4Tpe8-PM1TvC9oA
# 5- keeravani - 12l1SqSNsg2mI2IcXpPWjR?si=U5t_NfhqR7eZFrcJHQMVWQ




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

headers = {'Authorization': f'Bearer {access_token}'}

artist_ids = '2FgHPfRprDaylrSRVf1UlN,5sSzCxHtgL82pYDvx2QyEU,4zCH9qm4R2DADamUHMCa6O,0L5f9aJIaxQXTipZ7uQYiC,12l1SqSNsg2mI2IcXpPWjR'


url = f'https://api.spotify.com/v1/artists?ids={artist_ids}'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # formatted_data = json.dumps(data, indent=4)
    for artist in data['artists']:
        name = artist['name']
        followers = artist['followers']['total']
        popularity = artist['popularity']
        print(f"Name: {name}, Followers: {followers}, Popularity: {popularity}")

    # print(formatted_data)
else:
    print("Failed to fetch data: Status code", response.status_code)

