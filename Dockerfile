FROM python:3.14-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_PROJECT_ENVIRONMENT=/usr/local

RUN groupadd -g 1001 aqm && \
    useradd -u 1001 -g 1001 aqm && \
    chown -R 1001:1001 /app

RUN pip install --no-cache-dir uv

RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-dev --no-cache-dir

USER 1001

COPY ./devops/init.sh ./devops/init.sh
COPY main.py ./
COPY src src

CMD ["sh", "./devops/init.sh"]
