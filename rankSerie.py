import json

import requests

lista_queries = ["The Mentalist", "Druck", "House", "How i met your mother", "Modern family", "It's okay to be not okay"]
vote_list = []

api_key = 'd307689e567699f40e67ca9ef1b011d3'
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMzA3Njg5ZTU2NzY5OWY0MGU2N2NhOWVmMWIwMTFkMyIsInN1YiI6IjY1MDA0OTU5NmEyMjI3MDExYTdhYTFiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NWGTRV5EV14BcNGIdVznEvLm-b-uIJ_cOHW9h__Fwjo"
}

for query in lista_queries:
    url = f"https://api.themoviedb.org/3//search/multi?api_key={api_key}&query={query}"
    response = requests.get(url, headers=headers)

    dados = response.json()
    j = json.dumps(dados, indent=4)
    d = dados["results"][0]["vote_average"]
    # print(j)
    
    vote_list.append(d)
    print(d)
