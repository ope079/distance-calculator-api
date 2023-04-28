from fastapi import FastAPI, Body, Request
from pydantic import BaseModel
import googlemaps as gm
import uvicorn
from datetime import datetime

# Input API key (Please be aware that API keys are private so cant post on Github)
gmaps = gm.Client(key="")

# Initialise fast API
app = FastAPI()

# A welcome home page message endpoint. Simple one.
@app.get("/")
async def welcome() -> dict:
    return {"message" : "Welcome to google map api service."
                        "Find distance locations using city names and mode of transport"} 


# The main endpoint. Takes a JSON body in the form 
"""
{
origin: origin,
destination: destination,
transit_mode: transit_mode,
unit: unit
}
"""
# transit_mode can be string of bicycle, car, or mass transit like bus, tram or train
# unit is the unit of measurement of distance, and can be metric for kilometers and meters, or imperial for miles etc.
# Incorrect entry for any field will return an error
# And returns JSON containing the origin location, destination distance and duration of travel
@app.post("/distance/")
async def distance(request: Request, origin: str = Body("Leeds") , destination: str = Body("London"), transit_mode: str = Body("Bicycle"), unit: str = Body("metric")):
    
    now = datetime.now()

    distance_result = gmaps.distance_matrix(origins=origin, destinations=destination, transit_mode=transit_mode, units=unit, departure_time= now)

    return {"distance" : distance_result}
