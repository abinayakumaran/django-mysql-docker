FROM python:3.7
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR code
RUN cd /code && python manage.py 

EXPOSE 8000

# Migrates the database, uploads staticfiles, and runs the production server
CMD python /code/manage.py migrate;gunicorn --bind 0.0.0.0:8000 