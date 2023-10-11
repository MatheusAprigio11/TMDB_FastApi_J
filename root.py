from fastapi import FastAPI, HTTPException, status, Response
from models import Serie
from acessar_dados import series
import requests


api_key = 'd307689e567699f40e67ca9ef1b011d3'

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMzA3Njg5ZTU2NzY5OWY0MGU2N2NhOWVmMWIwMTFkMyIsInN1YiI6IjY1MDA0OTU5NmEyMjI3MDExYTdhYTFiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NWGTRV5EV14BcNGIdVznEvLm-b-uIJ_cOHW9h__Fwjo"
}

app = FastAPI()


@app.get('/')
async def home():
    return {"msg": 'SeriesLib'}

@app.get("/series")
async def get_series():
    return series



#Nesse get, ele retorna qualquer serie desde que haja um id para ela e adiciona no dicionario, podendo acessa-la no get de todas as series.
@app.get("/series/{serie_id}")
async def get_serie(serie_id: int):
   if serie_id in series:
       return series[serie_id]
   
   elif serie_id not in series:
        url = f"https://api.themoviedb.org/3/tv/{serie_id}?language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()

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
   else: 
       return {"Essa série não foi encontrada"}


@app.put("/series/{serie_id}")
async def att_serie(serie_id: int, serie: Serie):
    try:

        if serie_id in series:
            series[serie_id] = serie
            return serie    
    except:
        return f"Essa série não existe"


@app.post("/series")
async def add_serie(serie: Serie):

    last_key = sorted(series.keys())[-1]
    next_key = last_key + 1
    serie.id = next_key
    series[next_key] = serie
    return serie


@app.delete("/series/{serie_id}")
async def del_serie(serie_id: int):
    if serie_id in series:
        del series[serie_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Essa série não existe.")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("root:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
