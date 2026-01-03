# создается контекст приложения, укажем где будет находиться статика, шаблоны
# будет создан сам объект приложения
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='todo/static'),'static')
templates = Jinja2Templates(directory='todo/templates')

# почему возникает проблема, если переместисть эту строку перед app или написать без todo, хотя они на одном уровне
from todo.routes import home
