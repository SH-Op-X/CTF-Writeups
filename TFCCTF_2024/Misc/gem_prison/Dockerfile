FROM ruby:3.3-alpine

ENV TMP_ENABLED=1

COPY ./flag.txt /flag
COPY ./main.rb /chal.rb

RUN chmod +x /chal.rb

RUN apk update
RUN apk add socat

RUN chown -R root:root /flag /chal.rb

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"/chal.rb"