FROM python:3.10-slim

WORKDIR /app

COPY .env ./
COPY pyproject.toml poetry.lock ./
COPY src/ ./src/

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root


EXPOSE 8008

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8008"]
