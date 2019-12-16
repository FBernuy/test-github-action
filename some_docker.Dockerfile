FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install --no-install-recommends --yes python3 python3-pip

RUN mkdir /code
COPY . /code/

RUN pip3 install --upgrade pip
RUN pip3 install -r /code/requirements.txt

WORKDIR /code
CMD PYTHONPATH=$PWD python3 -m some_code.some_script