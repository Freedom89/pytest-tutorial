FROM continuumio/miniconda3:4.8.2

RUN apt-get update -y && apt-get install -y build-essential && apt-get install -y make \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $HOME/introduction
COPY . $HOME/introduction/

# This is due to docker steps, so i do not have to reinstall and only build once
RUN pip install -r requirements.txt -r requirements-test.txt

