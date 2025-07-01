# 1. Base image
FROM python:3.12-slim

# 2. Environment config
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV DJANGO_ALLOWED_HOSTS=uas-django-164037829861.asia-southeast2.run.app

# 3. Set working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN apt update && apt install -y default-libmysqlclient-dev build-essential pkg-config python3-dev
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy source code + database
COPY . .


# 7. Expose port (untuk Cloud Run)
EXPOSE 8080

# 8. Jalankan Django pakai development server
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:$PORT"]