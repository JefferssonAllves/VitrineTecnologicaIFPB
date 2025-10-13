#!/bin/sh
set -e  # Sai no primeiro erro

echo "🚀 Iniciando VitrineIFPB..."

# Aguarda o MySQL ficar pronto (se estiver usando)
echo "⏳ Aguardando banco de dados..."
while ! nc -z mysql 3306; do
  sleep 1
done
echo "✅ Banco de dados pronto!"

# Aplica migrações
echo "🔄 Aplicando migrações..."
python manage.py migrate --noinput

# Coleta arquivos estáticos
echo "📁 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "✅ Configuração concluída! Iniciando servidor..."

# Inicia o servidor8
exec python manage.py runserver 0.0.0.0:8000