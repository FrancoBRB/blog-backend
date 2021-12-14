from fastapi import APIRouter, Depends, status, HTTPException
from .. import models, schemas
from sqlalchemy.orm import Session
from ..hashing import Hash
from blog.database import get_db
from ..src import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

""" NUEVO USUARIO """


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.createUser(request, db)


""" VER USUARIO """


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.userProfile(db, id)
