FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y socat

COPY ./main.py /main.py
COPY ./flag /flag
COPY ./readflag /readflag

RUN chown -R root:root /flag
RUN chmod 700 /flag
RUN chmod +x /readflag
RUN chmod u+s /readflag

RUN useradd -m ctf
USER ctf

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 /main.py"