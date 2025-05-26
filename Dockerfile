# Gunakan image Python
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Salin file ke dalam image
COPY ./app /app
COPY ./requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port FastAPI
EXPOSE 8000

# Jalankan aplikasi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
