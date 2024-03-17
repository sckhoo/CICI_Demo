from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to CM CI/CD Demo 17March 1035am"}