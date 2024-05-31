from fastapi import FastAPI, Depends
from db.database import engine, session
from schemas import *
from db.models import *
from sqlalchemy.orm import Session
import uvicorn



Base.metadat.create_all(engine)


app = FastAPI()


def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()



@app.get('films/')
def get_films(db: Session = Depends(get_db)):
    return db.query(Film).all()


@app.post('create/')
def create_film(film: Films, db: Session = Depends(get_db)):
    pass


if __name__ == '__main__':
    uvicorn.run('main:app', port=5050, reload=True)