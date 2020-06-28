FROM python:3

COPY bots/cfg.py /bots/
COPY bots/followero.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "followero.py"]