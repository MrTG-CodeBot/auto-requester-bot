FROM python:3.10
RUN apt update && apt upgrade -y
RUN apt install git -y
RUN  pip install --upgrade pip
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip install -U pip && pip install -U -r requirements.txt
WORKDIR /app

COPY . .
CMD ["python3", "main.py"]
