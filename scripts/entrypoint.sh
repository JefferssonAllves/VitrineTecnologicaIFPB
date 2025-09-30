#!/bin/bash
set -e

echo "Iniciando o servidor..."

#VERIFICA SE O ARQUIVO DE BANCO DE DADOS EXISTE, SE NÃO, CRIA
if [ ! -f "/app/db.sqlite3" ]; then
  echo "Criando banco de dados SQLite..."
  touch /app/db.sqlite3
fi

echo "Aplicando migrações..."
python manage.py migrate --noinput

echo "Verificando configuração..."
python manage.py check --deploy

echo "✅ Configuração concluída! Iniciando servidor..."
exec "$@"