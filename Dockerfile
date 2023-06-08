FROM python:3.11.3-alpine
COPY . .
CMD python datascraping.py
