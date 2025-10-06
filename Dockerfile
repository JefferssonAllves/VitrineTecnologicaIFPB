FROM python:3.13-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências do sistema
RUN apt-get update && apt-get install -y \
  gcc \
  g++ \
  pkg-config \
  default-libmysqlclient-dev \
  netcat-traditional \
  && rm -rf /var/lib/apt/lists/*

# Dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt

# Aplicação
COPY . .

# 👈 PRIMEIRO copia o script e dá permissão
COPY scripts/entrypoint.sh .
RUN chmod +x entrypoint.sh  # 👈 Como root ainda

# 👈 DEPOIS cria usuário e muda
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
