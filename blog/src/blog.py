from sqlalchemy.orm.session import Session
from .. import models, schemas
from fastapi import HTTPException, status


def getAllBlogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def getIndividualBlog(db: Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID {id} is not founded.")
    return blog


def createBlog(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def deleteBlog(db: Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID {id} is not founded.")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Blog has been deleted."}


def updateBlog(id, request: schemas.BlogBase, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID {id} is not founded.")
    blog.update({'title': request.title, 'body': request.body},
                synchronize_session=False)
    db.commit()
    return {"detail": "Blog has been updated."}
