from .engine import Implication
from .query import Query, TagQuery, NegQuery, GroupQuery


SPECIAL_CHARS = "(),/-"


class Token:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Token) and self.value == other.value

    def __repr__(self):
        return f"Token({self.value!r})"


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def __iter__(self):
        return self

    def char(self):
        if self.pos >= len(self.text):
            raise StopIteration
        return self.text[self.pos]

    def __next__(self):
        while self.char().isspace():
            self.pos += 1

        ch = self.char()
        if ch in SPECIAL_CHARS:
            self.pos += 1
            return Token(ch)

        start = self.pos
        while not (ch.isspace() or ch in SPECIAL_CHARS):
            self.pos += 1
            ch = self.char()

        return self.text[start : self.pos]


def take_atom(lexer):
    token = next(lexer)
    if token == Token("("):
        return take_expr(lexer)
    elif token == Token("-"):
        return NegQuery(take_atom(lexer))
    elif isinstance(token, str):
        return TagQuery(token)
    else:
        raise ValueError(f"Unexpected {token}")


def take_expr(lexer):
    stack = [take_atom(lexer)]
    while True:
        try:
            token = next(lexer)
        except StopIteration:
            break

        if token == Token("/"):
            value = take_atom(lexer)
            last = stack[-1]
            if isinstance(last, GroupQuery) and last.type == "or":
                last.queries.append(value)
            else:
                stack[-1] = GroupQuery("or", [last, value])
        elif token == Token(","):
            stack.append(take_atom(lexer))
        elif token == Token(")"):
            break
        else:
            raise ValueError(f"Unexpected {token}")

    if len(stack) == 1:
        return stack[0]

    return GroupQuery("and", stack)


def parse_query(query: str) -> Query:
    lexer = Lexer(query)
    return take_expr(lexer)


def parse_implication(implication: str) -> Implication:
    lhs, rhs = implication.split("->")
    add_tags = []
    remove_tags = []
    for tag in rhs.split(","):
        tag = tag.strip()
        if tag.startswith("-"):
            remove_tags.append(tag[1:])
        else:
            add_tags.append(tag)

    return Implication(parse_query(lhs), add_tags, remove_tags)
