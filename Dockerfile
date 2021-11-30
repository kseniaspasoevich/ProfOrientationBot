FROM python:3.8
WORKDIR /app
RUN pip install -U pip aiogram

COPY src ./ 
ENTRYPOINT ["python","profbot.py"]
