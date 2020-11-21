FROM continuumio/miniconda3:4.8.2

RUN apt-get update -y && apt-get install -y build-essential && apt-get install -y make \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $HOME/tutorial

# This is due to docker steps, so i do not have to reinstall and only build once
COPY requirements.txt requirements-test.txt $HOME/tutorial/
RUN pip install -r requirements.txt -r requirements-test.txt

COPY . $HOME/tutorial
WORKDIR $HOME/tutorial/
