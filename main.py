from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from auth import create_token, verify_token
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_root():
    return {"message": "Blog API Working"}


# Login API
@app.post("/login")
def login():
    return {"access_token": create_token({"user": "admin"}), "token_type": "bearer"}


# Create Blog(Protected)
@app.post("/blogs", response_model=schemas.BlogResponse)
def create_blog(
    blog: schemas.BlogCreate, db: Session = Depends(get_db), user=Depends(verify_token)
):
    new_blog = models.Blog(title=blog.title, content=blog.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Read All Blog
@app.get("/blogs")
def get_blogs(
    page: int = 1,
    limit: int = 5,
    search: str = Query(default=""),
    db: Session = Depends(get_db),
    user=Depends(verify_token),
):
    query = db.query(models.Blog)
    if search:
        query = query.filter(models.Blog.title.ilike(f"%{search}"))

    total = query.count()
    start = (page - 1) * limit
    blog = query.offset(start).limit(limit).all()

    return {"page": page, "limit": limit, "total": total, "data": blog}


# Get By Id
@app.get("/blogs/{id}", response_model=schemas.BlogResponse)
def get_blog_by_id(id: int, db: Session = Depends(get_db), user=Depends(verify_token)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")
    return blog


@app.delete("/blog/{id}")
def delete_blog(id: int, db: Session = Depends(get_db), user=Depends(verify_token)):
    blog = blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")

    db.delete(blog)
    db.commit()

    return {"message": "Blog Deleted Successfully"}


@app.put("/blog/{id}", response_model=schemas.BlogResponse)
def update_blog(
    id: int,
    blog: schemas.BlogCreate,
    db: Session = Depends(get_db),
    user=Depends(verify_token),
):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not existing_blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")

    existing_blog.title = blog.title
    existing_blog.content = blog.content

    db.commit()
    db.refresh(existing_blog)

    return existing_blog
