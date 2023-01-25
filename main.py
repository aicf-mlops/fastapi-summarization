# FastAPI main file with healtcheck function and main function
from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
    
