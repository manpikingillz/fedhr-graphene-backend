# base/parent image to use
FROM python:3.10.8-buster

# set environment variables
# prevents Python from copying pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1

# ensures that Python output is logged to the terminal,
# making it possible to monitor Django logs in realtime.
ENV PYTHONUNBUFFERED 1

# set work director
WORKDIR /fedhr

# copy requirements.txt
COPY ./requirements.txt /fedhr/

# install dependancies
RUN pip install -r requirements.txt

# copy project
COPY . /fedhr/

# port that the container will litsen on, at runtime
# EXPOSE 9000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:9000" ]