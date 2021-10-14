# djangotask

usage

```shell
# in the repository root directory
docker build -t djangotask:latest .
docker run -p 8000:8000 djangotask:latest
```

## My Notes

[Python — Virtualenv 虛擬環境安裝](https://medium.com/python4u/python-virtualenv%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83%E5%AE%89%E8%A3%9D-9d6be2d45db9)

['virtualenv' won't activate on Windows](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows)
`Set-ExecutionPolicy Unrestricted -Scope Process`

no such table:

```shell
python manage.py makemigrations
python manage.py migrate
```

[Django client.get response has no 'data' attribute](https://stackoverflow.com/questions/63060849/django-client-get-response-has-no-data-attribute)

[How to resolve AssertionError: .accepted_renderer not set on Response in django and ajax](https://stackoverflow.com/questions/55416471/how-to-resolve-assertionerror-accepted-renderer-not-set-on-response-in-django)

---

[Django model.BooleanField value as 0/1](https://stackoverflow.com/questions/33021461/django-model-booleanfield-value-as-0-1)

[DjangoCMS TypeError: from_db_value() missing 1 required positional argument: 'context' after upgrade to 3.7.2 w/ Django 3.0.1](https://stackoverflow.com/questions/61451710/djangocms-typeerror-from-db-value-missing-1-required-positional-argument-co)
