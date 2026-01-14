from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "New build is live ✅"}
