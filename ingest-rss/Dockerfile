FROM python:3.9-slim-buster

# Add your additional Dockerfile instructions here
COPY app /app
WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt
CMD ["/bin/bash", "-c", "python /app/ingest-rss.py" ]