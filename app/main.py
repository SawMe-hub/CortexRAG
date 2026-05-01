from fastapi import FastAPI

app = FastAPI(title="CortexRAG")

@app.get("/")
def root():
    return {"message": "CortexRAG is running"}