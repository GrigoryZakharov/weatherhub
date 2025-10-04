from fastapi import FastAPI

app = FastAPI(title="WeatherHub API")

@app.get("/")
def root():
    return {"status": "ok", "message": "WeatherHub API running"}
