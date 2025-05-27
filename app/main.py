from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/detect/")
@app.post("/detect/{label}")
async def detect_image(file: Annotated[UploadFile, File()],label: str | None = None):
  return {"message": "it works"}