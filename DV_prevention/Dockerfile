FROM python:3.9.0

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN python -m pip install python-dev-tools --user --upgrade
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .