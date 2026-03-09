import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request
        }
    )


@app.post('/roll', response_class=HTMLResponse)
async def roll(request: Request):
    dice = random.randint(1, 6)
    result_dice = ('⚀', '⚁', '⚂', '⚃', '⚄', '⚅')
    print(dice * 2500)
    return templates.TemplateResponse(
        'dice_result.html',
        {
            'request': request,
            'result_dice': result_dice[dice - 1]
        }
    )
