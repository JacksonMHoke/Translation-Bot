FROM python:3.8-slim

COPY translator.py ./
COPY tweet.py ./
COPY requirements.txt ./
COPY keys.json ./
COPY tweet.txt ./
RUN pip install -r ./requirements.txt

CMD ["python3", "tweet.py"]