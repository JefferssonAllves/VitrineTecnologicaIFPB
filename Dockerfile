FROM python:3.13-slim-bullseye

ENV PYTHONUNBUFFERED=1

# Definir WORKDIR primeiro
WORKDIR /app

# Copiar arquivos para o WORKDIR
COPY VitrineIFPB /app/VitrineIFPB
COPY scripts/entrypoint.sh /app/scripts/entrypoint.sh
COPY requirements.txt /app/requirements.txt

# Dependências do sistema
RUN apt-get update && apt-get install -y \
  gcc \
  g++ \
  pkg-config \
  default-libmysqlclient-dev \
  netcat-traditional \
  && rm -rf /var/lib/apt/lists/*

# Dependências Python
RUN pip install --upgrade pip && \
  pip install --no-cache-dir -r /app/requirements.txt

# Dar permissão ao entrypoint (AGORA no caminho correto)
RUN chmod +x /app/scripts/entrypoint.sh

# Mudar para o diretório da aplicação
WORKDIR /app/VitrineIFPB

# Entrypoint com caminho absoluto
ENTRYPOINT ["/app/scripts/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000