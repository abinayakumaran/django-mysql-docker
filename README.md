# django-mysql-docker


## Dependency Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## settings.py

```python
DB Connection

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_schema_name',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

##  Migrate
```bash
Migration

python manage.py migrate
```

## Create admin user
```bash
python manage.py createsuperuser
```
## Run server
```bash
python manage.py runserver
```