FROM python:3.10-alpine

COPY bot.py ./
COPY rss.py ./
COPY last_post.pickle ./
COPY token.secret ./
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

CMD ['python3', 'bot.py']
