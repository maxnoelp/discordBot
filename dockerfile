FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bot-Code kopieren
COPY . .

# Startbefehl
CMD ["python", "bot.py"]
