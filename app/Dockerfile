FROM python:3.12-slim-bullseye

ENV TZ=Europe/Paris

LABEL AUTHOR=SylvainTouret 
LABEL MAIL=sylvain.touret@delia.tech

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV WATCHFILES_FORCE_POLLING=true

RUN mkdir -p /app

WORKDIR /app
RUN pip install poetry

# File imports : requirements
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

RUN poetry install --no-root

COPY ./src /app

CMD ["poetry","run", "uvicorn", "main:app", "--host", "0.0.0.0"]