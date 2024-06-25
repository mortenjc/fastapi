from pydantic import BaseModel
from fastapi import FastAPI

import uvicorn

app = FastAPI()

class Item(BaseModel):
    id : int
    album : str
    artist: str

db = {
    0: Item(id = 0, album='Guardian of the light', artist='George Duke'),
    1: Item(id = 1, album='Headhunters', artist='Herbie Hancock'),
    2: Item(id = 2, album='The early tapes', artist='Level 42'),
}

@app.get('/get')
def index():
    return db


@app.post('/add')
def add_item(item: Item) -> dict[str, str]:
    if item.id in db:
        return {'error': f'id {item.id} already exist'}
    db[item.id] = item
    return {'status' : f'id {item.id} added to db'}


@app.delete('/delete')
def del_item(item: Item) -> dict[str, str]:
    if item.id not in db:
        return {'error': f'id {item.id} doesnt exist'}
    db.pop(item.id)
    return {'status' : f'id {item.id} removed from db'}


if __name__ == "__main__":
    uvicorn.run('fastapi3:app', reload=True)
