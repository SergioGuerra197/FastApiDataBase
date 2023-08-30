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
from models.movie import Movie as MovieModel

app = FastAPI()
app.title = 'Mi aplicacion con fastApi con bases de datos'
app.version = '0.0.1'

Base.metadata.create_all(bind=engine)


class Movie(BaseModel):
    id: Optional[int] | None = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(default=2022,le=2022)
    rating: float = Field(ge=1,le=10)
    category: str = Field(min_length=5, max_length=15)




@app.get('/', tags=['home'])
def message():
    html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    return FileResponse(html_file_path, media_type="text/html")


@app.post('/movies', tags = ['movies'], response_model=dict, status_code= 201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())#Con los asteriscos extrae los atributos y los pasa como parametros 
    db.add(new_movie)
    db.commit()
    return JSONResponse(status_code=201, content={'message': 'Se ha registrado la pelicula'})