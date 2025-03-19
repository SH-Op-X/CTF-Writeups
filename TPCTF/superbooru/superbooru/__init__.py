import json

from contextlib import asynccontextmanager
from databases import Database

from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .engine import Engine
from .image import Image
from .parser import parse_implication

from typing import Annotated

print("Loading implications... (this may take a while)")

with open("implications.txt") as f:
    imps = []
    for line in f:
        line = line.strip()
        if not line:
            continue

        imps.append(parse_implication(line))

    engine = Engine(imps)

db = Database("sqlite+aiosqlite:///booru.db")

templates = Jinja2Templates(directory="templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    await db.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tags TEXT NOT NULL,
        url TEXT NOT NULL
    )
    """)
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root(request: Request):
    rows = await db.fetch_all("SELECT * FROM images")
    images = [Image.from_row(row) for row in rows]
    return templates.TemplateResponse(request, "index.html", {"images": images})


@app.get("/image/new")
async def new_image(request: Request):
    return templates.TemplateResponse(request, "new_image.html")


async def get_image(id: int):
    row = await db.fetch_one("SELECT * FROM images WHERE id = :id", {"id": id})
    if row is None:
        raise HTTPException(status_code=404, detail="Image not found")

    return Image.from_row(row)


def render_image(request: Request, image: Image):
    return templates.TemplateResponse(request, "image.html", {"image": image})


@app.get("/image/{id}")
async def image(request: Request, id: int):
    return render_image(request, await get_image(id))


def parse_tags(tags: str):
    if not tags.strip():
        return set()
    return set(tag.strip() for tag in tags.split(","))


@app.post("/image/{id}")
async def set_image_tags(request: Request, id: int, tags: Annotated[str, Form()]):
    image = await get_image(id)
    image.tags = parse_tags(tags)
    engine.apply(image)

    await db.execute(
        "UPDATE images SET tags = :tags WHERE id = :id",
        {
            "tags": json.dumps(list(image.tags)),
            "id": image.id,
        },
    )

    return render_image(request, image)


@app.post("/image")
async def create_image(
    request: Request, tags: Annotated[str, Form(...)], url: Annotated[str, Form(...)]
):
    image = Image(id=0, tags=parse_tags(tags), url=url)
    engine.apply(image)

    image.id = await db.fetch_val(
        "INSERT INTO images (tags, url) VALUES (:tags, :url) RETURNING id",
        {
            "tags": json.dumps(list(image.tags)),
            "url": image.url,
        },
    )

    return render_image(request, image)
