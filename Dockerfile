FROM python:3.10

ENV HOME /app
WORKDIR $HOME
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . .

CMD ["sh", "entrypoint.sh"]
#COPY migrations migrations
#
#COPY docker_config.py default_config.py
#
#CMD flask run -h 0.0.0.0 -p 80