FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser -D appuser
USER appuser

#CMD ["python", "app.py"]
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]

