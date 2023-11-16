FROM python:3.9
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
RUN pip install --upgrade pip -r requirements.txt
EXPOSE 5000
