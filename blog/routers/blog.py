from fastapi import APIRouter, Depends, status
from blog.oauth2 import get_current_user
from .. import schemas
from sqlalchemy.orm import Session
from typing import List
from blog.database import get_db
from ..src import blog


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

""" CREAR NUEVO BLOG """


@router.post('/', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.createBlog(request, db)


""" OBTENER BLOG TODOS O INDIVIDUAL RESPECTIVAMENTE """


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.getAllBlogs(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.getIndividualBlog(db, id)


""" ELIMINAR BLOG """


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.deleteBlog(db, id)


""" ACTUALIZAR BLOG """


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.BlogBase, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.updateBlog(id, request, db)
