import requests

api_key = 'd307689e567699f40e67ca9ef1b011d3'
url = "https://api.themoviedb.org/3/tv/2?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMzA3Njg5ZTU2NzY5OWY0MGU2N2NhOWVmMWIwMTFkMyIsInN1YiI6IjY1MDA0OTU5NmEyMjI3MDExYTdhYTFiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NWGTRV5EV14BcNGIdVznEvLm-b-uIJ_cOHW9h__Fwjo"
}

response = requests.get(url, headers=headers)

data = response.json()

print(data['name'],data['number_of_episodes'])