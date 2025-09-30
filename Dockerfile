FROM python:3.13.7-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  gcc g++ \
  libjpeg-dev zlib1g-dev \
  netcat-traditional curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -r appuser && \
  useradd -r -g appuser appuser && \
  chown -R appuser:appuser /app \
  && mkdir -p /app/staticfiles /app/media /app/logs

USER appuser

COPY scripts/entrypoint.sh .
RUN chmod +x entrypoint.sh

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health/ || exit 1

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]