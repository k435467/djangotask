FROM python:3.8.3-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
