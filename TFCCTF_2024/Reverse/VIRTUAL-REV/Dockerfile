FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    socat \
    libstdc++6 \
    libgcc-s1 \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/ctf

COPY virtual-rev /home/ctf/virtual-rev
COPY flag.txt /home/ctf/flag.txt

RUN chmod +x /home/ctf/virtual-rev

WORKDIR /home/ctf

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:/home/ctf/virtual-rev
