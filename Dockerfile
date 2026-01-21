# Usamos Python ligero
FROM python:3.9-slim

# Evita que Python genere archivos .pyc y buffer de salida
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Comando para mantener el contenedor encendido (modo espera)
# Esto nos permite entrar y ejecutar tests manualmente
CMD ["tail", "-f", "/dev/null"]