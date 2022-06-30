FROM python:3.10-alpine
ENV PYTHONNUNBUFFERED 1
WORKDIR / starline
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt