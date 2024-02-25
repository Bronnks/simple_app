FROM python:3.11
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY poetry.lock pyproject.toml /app/


ENV PATH="${PATH}:/root/.local/bin" \
    POETRY_VIRTUALENVS_CREATE=False \
    PYTHONPATH="${PYTHONPATH}:/opt:/opt/src"
RUN poetry install
RUN apt-get update && apt-get install -y vim htop

COPY . .

CMD ["python", "simple_app/manage.py", "runserver", "0.0.0.0:8000"]