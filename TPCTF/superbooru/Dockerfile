FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY static static
COPY superbooru superbooru
COPY templates templates
COPY booru.db implications.txt ./

EXPOSE 8000
CMD ["fastapi", "run", "superbooru", "--port", "8000"]
