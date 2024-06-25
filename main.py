from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sympy import isprime
import uvicorn
import random

app = FastAPI()

templates = Jinja2Templates(directory='templates')


def makeintlist(n : int) -> list:
    numbers = []
    for i in range(n):
        numbers.append({'index' : i, 'value' : random.randrange(1000)})
    return numbers


def makeprimelist(n : int) -> list:
    primes = []
    pcount = 0
    while pcount != n:
        number = random.randrange(1000)
        if isprime(number):
            pcount += 1
            primes.append({'index' : len(primes), 'value' : number})
    return primes


@app.get('/', response_class=HTMLResponse)
def index(request : Request):
    context = {'request' : request}
    return templates.TemplateResponse('index.html', context)


@app.get('/ints', response_class=HTMLResponse)
def index(request : Request, n: int = 10, hx_request: Optional[str] = Header(None)):
    numbers = makeintlist(n)
    context = {'request' : request, 'numbers' : numbers, 'type' : 'Random integers'}
    if hx_request:
        return templates.TemplateResponse('table.html', context)
    return templates.TemplateResponse('ints.html', context)


@app.get('/primes', response_class=HTMLResponse)
def getprimes(request : Request, n : int = 10, hx_request: Optional[str] = Header(None)):
    numbers = makeprimelist(n)
    context = {'request' : request, 'numbers' : numbers, 'type' : 'Random primes'}
    if hx_request:
        return templates.TemplateResponse('table.html', context)
    return templates.TemplateResponse('primes.html', context)


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
