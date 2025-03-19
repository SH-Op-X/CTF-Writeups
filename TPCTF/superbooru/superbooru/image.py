import json

from pydantic import BaseModel


class Image(BaseModel):
    id: int
    tags: set[str]
    url: str

    def from_row(row: dict) -> "Image":
        return Image(id=row["id"], tags=set(json.loads(row["tags"])), url=row["url"])
