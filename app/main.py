from app.exceptions import Unauthorized
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from typing import List, Optional
from . import routes, models, database

app = FastAPI()

app.include_router(routes.router)
app.include_router(routes.users.router)

@app.on_event('startup')
async def create_db_tables():
    models.Base.metadata.create_all(bind=database.engine)

@app.exception_handler(Unauthorized)
async def unauthorized(request: Request, exc: Unauthorized):
    return JSONResponse(
        status_code=401,
        content={'code': exc.code},
    )
