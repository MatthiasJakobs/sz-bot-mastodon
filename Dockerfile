FROM python:3.10-alpine
WORKDIR szbot

COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]
