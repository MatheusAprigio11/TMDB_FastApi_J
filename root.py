from fastapi import FastAPI, HTTPException, status, Response
from models import Serie
from rankSerie import vote_list

app = FastAPI()


@app.get('/')
async def home():
    return {"msg": 'SeriesLib'}


series = {
    1: {
        "title": "The Mentalist",
        "seasons": 7,
        "year_start": 2008,
        "num_episodes": 151,
        "status": "finish",
        "description": "A famous psychic outs himself as a fake, and starts working as a consultant for the "
                       "California Bureau of Investigation so he can find Red John, the madman who killed his wife and daughter.",
        "vote_average": vote_list[0]

    },
    2: {
        "title": "Druck",
        "seasons": 5,
        "year_start": 2018,
        "number_episodes": 80,
        "status": "finish",
        "description": "Druck follows a group of friends in their teen life in Berlin and deals with daily and"
                       " current events, like friendship, love and the search for their own identity. Every season centers on a new character.",
        "vote_average": vote_list[1]
    },
    3: {
        "title": "House",
        "seasons": 7,
        "year_start": 2004,
        "number_episodes": 176,
        "status": "finish",
        "description": "An antisocial maverick doctor who specializes in diagnostic medicine does whatever it "
                       "takes to solve puzzling cases that come his way using his crack team of doctors and his wits.",
        "vote_average": vote_list[2]
    },
    4: {
        "title": "How i met your mother",
        "seasons": 9,
        "year_start": 205,
        "number_episodes": 208,
        "status": "finish",
        "description": "A father recounts to his children - through a series of flashbacks - the journey he and his "
                       "four best friends took leading up to him meeting their mother.",
        "vote_average": vote_list[3]
    },
    5: {
        "title": "Modern family",
        "seasons": 11,
        "year_start": 2009,
        "number_episodes": 250,
        "status": "finish",
        "description": "Three different but related families face trials and tribulations in their own uniquely comedic ways.",
        "vote_average": vote_list[4]
    },
    6: {
        "title": "It's okay to be not okay",
        "seasons": 1,
        "year_start": 2020,
        "number_episodes": 16,
        "status": 'Finish',
        "description": "An extraordinary road to emotional healing opens up for an selfish antisocial children's"
                       " book writer and a selfless psych ward caretaker when they cross paths.",
        "vote_average": vote_list[5]
    },
}


@app.get("/series")
async def get_series():
    return series


@app.get("/series/{serie_id}")
async def get_serie(serie_id: int):
   if serie_id in series:
       return series[serie_id]
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


# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run("root:app", host='127.0.0.1', port=8000, log_level="info", reload=True)
