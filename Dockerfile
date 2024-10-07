# Usa la imagen base de Python 3.12
FROM python:3.12

# Añade el script de instalación de uv
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Establece el directorio de trabajo
WORKDIR /app

# Copia solo los archivos de dependencias para aprovechar la cache de Docker
COPY requirements.txt .

# Instala las dependencias utilizando uv
RUN /root/.cargo/bin/uv pip install --system --no-cache -r requirements.txt

RUN /root/.cargo/bin/uv pip show pydantic

# Copia el resto de la aplicación
COPY . .

# Establece las variables de entorno (opcional, pero útil para configurar tu aplicación)
ENV PYTHONUNBUFFERED=1

# Especifica el puerto de la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
