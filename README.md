# sebas_blog

blog backend api

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Local setup with docker

- To startup the dev applcication, use this command:

```bash
docker compose -f local.yml up
```
### Setting Up Your Users

-   To create a **superuser account**, use this command:

```bash
docker compose -f local.yml run --rm django python manage.py createsuperuser
```

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

``` bash
docker compose -f local.yml run --rm django coverage run -m pytest
docker compose -f local.yml run --rm django coverage html
open htmlcov/index.html
```


#### Running tests with pytest

```bash
docker compose -f local.yml run --rm django pytest
```

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).


### How it works

- Create a django superuser.
- Authenticate your requests:

```bash
curl -X POST http://localhost:8000/auth-token/ -H 'Content-Type: application/json' -d '{"username": <your-username>, "password": <your-password>}'

{"token": <your-token>}
```
- List blogs

```bash
curl -X GET http://localhost:8000/blogs/list/ -H 'Authorization: Token <your-token>'

[
    {
        "id": "1",
        "blog_content": "content1",
        "blog_title": "title1",
        "blog_author": <your-username>
        "created_at": "2023-02-16T17:09:10.690256Z",
    },
]
```

- Create a blog
```bash
curl -X POST http://localhost:8000/blogs/list/ -H 'Authorization: Token <your-token>' -d '{"blog_title": "blog1", "blog_content": "content1"}'

{
    "id": "1",
    "blog_content": "content1",
    "blog_title": "title1",
    "blog_author": <your-username>
    "created_at": "2023-02-16T17:09:10.690256Z",
}
```

- Retrieve a blog
```bash
curl -X GET http://localhost:8000/blogs/retrieve/1 -H 'Authorization: Token <your-token>'

{
    "id": "1",
    "blog_content": "content1",
    "blog_title": "title1",
    "blog_author": <your-username>
    "created_at": "2023-02-16T17:09:10.690256Z",
}
```

- Update a blog
```bash
curl -X PUT http://localhost:8000/blogs/update/1 -H 'Authorization: Token <your-token>' -d '{"blog_title": "blog1", "blog_content": "content1"}'

```

- Delete a blog
```bash
curl -X DELETE http://localhost:8000/blogs/update/1 -H 'Authorization: Token <your-token>'

```
