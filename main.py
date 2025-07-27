from fastapi import FastAPI
from mylib.logic import wiki as wikilogic
from mylib.logic import search_wiki
from mylib.logic import phrase as wikiphase

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in Wikipedia"""
    print(value)
    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve the Wikipedia page"""
    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Return phrases from Wikipedia"""
    result = wikiphase(name)
    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8080, host="0.0.0.0")
