FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

CMD ["sh", "entrypoint.sh"]