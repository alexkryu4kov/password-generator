FROM python:3.10.13-bookworm

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN flask db migrate
RUN flask db upgrade

CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5000", "run:app"]
