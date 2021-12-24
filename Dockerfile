FROM python:3.8
WORKDIR /app
RUN pip install -U pip aiogram
RUN pip install dp
RUN pip install telebot
RUN mkdir -p /app/fixture
COPY src ./ 
COPY fixture ./fixture
ENTRYPOINT ["python","profbot.py"]
