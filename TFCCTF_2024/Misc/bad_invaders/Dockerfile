FROM golang:latest AS build

COPY chal /chal

WORKDIR /chal

RUN go build -o /chal/chal

FROM golang:latest

COPY ./bot.py /bot.py

COPY --from=build /chal/chal /game

CMD ["/game"]