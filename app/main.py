from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/detect/{label}")
async def detect_image(label: str, file: Annotated[UploadFile, File()]):
  return {"message": "it works"}