FROM python:3.9-slim as builder

WORKDIR /install

RUN python -m pip install --upgrade pip pipenv

COPY ./Pipfile* ./

RUN python -m pipenv requirements > requirements.txt

FROM python:3.9-slim

ARG workdir
ARG port

ENV PYTHONUNBUFFERED=1 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=${port}

# set work directory
WORKDIR ${workdir}

# python wand dependency 
# https://stackoverflow.com/a/59193253
RUN apt-get update && apt-get install -y -qq libmagickwand-dev ffmpeg
COPY ./compose/server/etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy.xml


COPY --from=builder /install/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./compose/server/start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

COPY ./src .

EXPOSE 8000

