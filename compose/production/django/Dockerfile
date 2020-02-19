FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update \
    # Pillow dependencies
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN apk add autoconf automake make g++ gcc libxslt-dev libffi-dev build-base musl-dev --no-cache

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN  pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

COPY ./compose/production/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

