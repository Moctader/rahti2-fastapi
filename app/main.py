from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "Hello": "Rahti2", "v": "0.900" }


@app.get("/items/{id}")
def read_item(id: int, q: str = None):
    return {"id": id, "q": q}
