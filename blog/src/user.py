from sqlalchemy.orm.session import Session
from .. import models, schemas
from ..hashing import Hash
from fastapi import HTTPException, status


def createUser(request: schemas.User, db: Session):
    new_user = models.User(username=request.username,
                           email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def userProfile(db: Session, id):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with ID {id} is not founded.")
    return user
