# Used at least the minimum version defined in .python-version file, allowing patch updates
FROM python:3.13 AS poetry

ENV PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=120 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local'

RUN curl -sSL https://install.python-poetry.org | python3

# Catch the dependency layer to speedup the build
FROM poetry AS env_ready

WORKDIR /opt

COPY poetry.toml poetry.lock pyproject.toml /opt/

RUN poetry install --only main --no-interaction --no-ansi --no-root

FROM env_ready AS final

COPY . /opt/
EXPOSE 8000

# Delegated to the script the shell election
ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["api", "--host=0.0.0.0", "--port=8000"]
