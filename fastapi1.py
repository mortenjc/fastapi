from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {'item' : 'hammer', 'count': 700}


if __name__ == "__main__":
    uvicorn.run('fastapi1:app', reload=True)
