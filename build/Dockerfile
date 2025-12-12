FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libgl1 \
        libglib2.0-0 \
        libxcb-xinerama0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install "poetry==${POETRY_VERSION}"

WORKDIR /app

COPY build/pyproject.toml pyproject.toml
COPY build/poetry.lock poetry.lock

RUN poetry install --no-interaction --no-ansi --with dev --no-root

COPY . /app

ENTRYPOINT ["poetry", "run", "python"]
CMD ["python -m chatmate_src.chatmate_details.main.davinchik.daivinchik_auto_like_main"]
