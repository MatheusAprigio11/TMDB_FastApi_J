import requests

api_key = 'd307689e567699f40e67ca9ef1b011d3'

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMzA3Njg5ZTU2NzY5OWY0MGU2N2NhOWVmMWIwMTFkMyIsInN1YiI6IjY1MDA0OTU5NmEyMjI3MDExYTdhYTFiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NWGTRV5EV14BcNGIdVznEvLm-b-uIJ_cOHW9h__Fwjo"
}

series = {}

#função que busca dado por dado de cada serie e a adiciona no dicionario de acordo com o models

def buscar_dados():
    posicao = 1
    for posicao in range(20):
        posicao += 1
        url = f"https://api.themoviedb.org/3/tv/{posicao}?language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()

        serie_id = data["id"]
        serie = {
            'name': data["name"],
            'seasons' : data["number_of_seasons"],
            'year_start' : data["first_air_date"],
            'num_episodes' : data["number_of_episodes"],
            'status': data["status"],
            'description': data["overview"],
            'vote_average': data["vote_average"]           
        }
        series[serie_id] = serie
    
    return series

series = buscar_dados()
