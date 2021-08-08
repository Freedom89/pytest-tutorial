FROM continuumio/miniconda3:4.8.2
RUN apt-get update - && \
    apt-get install -y build-essential && apt-get install -y make curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $HOME/my_project

COPY requirements.txt $HOME/my_project/

RUN pip install -r requirements.txt

COPY pytest.ini Makefile $HOME/my_project/

COPY tests $HOME/my_project/tests

ENTRYPOINT ["make"]
CMD ["run"]