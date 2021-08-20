from fastapi import FastAPI
from starlette.responses import FileResponse
import os.path

app = FastAPI(title="Info.Bottley")

responseHeader = {"Accept-Encoding": "gzip", "Content-Encoding": "gzip"}

@app.get("/")
async def index():
    return FileResponse("./app/page/index.html.gz", media_type="text/html", headers=responseHeader)

@app.get("/{fileName}")
async def main(fileName):
    if not os.path.isfile("./app/page/"+fileName+".gz"):
        return FileResponse("./app/page/notFound.html.gz", media_type="text/html", headers=responseHeader)
    return FileResponse("./app/page/"+fileName+".gz", media_type="text/html", headers=responseHeader)