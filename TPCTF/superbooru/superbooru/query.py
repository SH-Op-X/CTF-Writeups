from .image import Image

from typing import Literal

from collections.abc import Iterator


class Query:
    def matches(self, image: Image) -> bool:
        pass

    def tags(self) -> Iterator[str]:
        pass


class TagQuery(Query):
    def __init__(self, tag: str):
        self.tag = tag

    def matches(self, image: Image) -> bool:
        return self.tag in image.tags

    def tags(self) -> Iterator[str]:
        yield self.tag


class NegQuery(Query):
    def __init__(self, inner: str):
        self.inner = inner

    def matches(self, image: Image) -> bool:
        return not self.inner.matches(image)

    def tags(self) -> Iterator[str]:
        return self.inner.tags()


GroupType = Literal["and", "or"]


class GroupQuery(Query):
    def __init__(self, type: GroupType, queries: list[Query]):
        self.type = type
        self.queries = queries

    def matches(self, image: Image) -> bool:
        it = (q.matches(image) for q in self.queries)
        return all(it) if self.type == "and" else any(it)

    def tags(self) -> Iterator[str]:
        for q in self.queries:
            yield from q.tags()
