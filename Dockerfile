FROM python:3

COPY bots/cfg.py /bots/
COPY bots/activius.py /bots/
COPY bots/dayandtime.py /bots/
COPY bots/followero.py /bots/
COPY bots/mentionaro.py /bots/
COPY bots/statusio.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "activius.py", "followero.py", "mentionaro.py", "statusio.py"]