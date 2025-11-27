import requests
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

API_KEY = "2def09815ee898a41baf7fe4a7450054"  # 👉 Put your OpenWeather API key here


# ---------- Function that calls weather API ----------
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


# ---------- Request model ----------
class WeatherRequest(BaseModel):
    city: str


# ---------- API endpoint (function calling) ----------
@app.post("/weather")
def weather(req: WeatherRequest):
    result = get_weather(req.city)
    return result


# ---------- Serve frontend (static files) ----------
# /frontend will show index.html from 'static' folder
app.mount("/frontend", StaticFiles(directory="static", html=True), name="frontend")
