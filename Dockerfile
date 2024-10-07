# Base image
FROM python:alpine

# Copy alle filer i den mappe hvor min Dockerfile er til /app mappen i mit image
COPY . /app

# Skift til mappen /app (svarer til CD kommandoen)
WORKDIR /app

# Installer alle dependencies
RUN pip install -r requirements.txt

# Eksekver denne kommando når Containeren køres
CMD ["python", "app.py"]