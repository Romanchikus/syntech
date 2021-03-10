# Dockerfile
# Pull base image
FROM python:3.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*\
  && /usr/local/bin/python -m pip install --upgrade pip

# RUN pip install psycopg2
RUN pip install pipenv 
# Requirements are installed here to ensure they will be cached.
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

# Set work directory
WORKDIR /certificate
COPY . /certificate

RUN python manage.py collectstatic --noinput
# run gunicorn
CMD pipenv gunicorn certificate.wsgi:application --bind 0.0.0.0:$PORT
