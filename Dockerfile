
FROM python:3.7

WORKDIR /app

RUN echo 'deb http://deb.debian.org/debian stretch main' >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get autoremove -y && \
    apt-get install -y libssl1.0-dev curl git nano wget && \
    rm -rf /var/lib/apt/lists/* && rm -rf /var/lib/apt/lists/partial/*
    
ADD https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz /
RUN set -ex; wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz

COPY wkhtmltox-0.12.4_linux-generic-amd64.tar.xz /app
RUN set -ex; tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN set -ex; mv wkhtmltox/bin/wkhtmlto* /usr/bin/
RUN set -ex; ln -nfs /usr/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf

RUN set ex; ./wkhtmltopdf.sh
RUN pip install -r requirements.txt
RUN pip install flask python-dotenv pdfkit qrcode code128 pytesseract requests wget  --upgrade certifi
COPY . /app
EXPOSE 5000

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN git clone https://github.com/casperTeam/never1.git
WORKDIR /never1
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
