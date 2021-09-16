FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY main.py /usr/src/app/
COPY requirements.txt /usr/src/app/
COPY test.py /usr/src/app/
RUN pip install -r requirements.txt
CMD  python3 ./main.py
EXPOSE 8081
