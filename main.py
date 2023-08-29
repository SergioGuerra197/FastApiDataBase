import os
from fastapi import FastAPI, Body, Path, Query, Depends, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Optional, List
from starlette.requests import Request
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer
from config.database import Session, engine, Base
from models.movie import Movie

app = FastAPI()
app.title = 'Mi aplicacion con fastApi con bases de datos'
app.version = '0.0.1'

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    return FileResponse(html_file_path, media_type="text/html")