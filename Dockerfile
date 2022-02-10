FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN git clone https://github.com/casperTeam/never1.git
WORKDIR /never1
RUN pip3 install -U -r requirements.txt
ENV DOWNLOAD_URL "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-3/wkhtmltox-0.12.6-3.archlinux-x86_64.pkg.tar.xz" -L -o "wkhtmltopdf.tar.xz"
RUN apt-get update && apt-get install -y \
    curl libxrender1 libfontconfig libxtst6 xz-utils
RUN curl $DOWNLOAD_URL
RUN tar Jxvf wkhtmltopdf.tar.xz
RUN cp usr/bin/wkhtmltopdf /never1
CMD python3 main.py
