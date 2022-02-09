# Debian Based Docker
FROM debian:latest

RUN apt update && apt upgrade -y

# Installing Packages
RUN apt install git curl python3-pip ffmpeg -y

# Installing Pip Packages
RUN pip3 install -U pip

# Copying Requirements
COPY requirements.txt /requirements.txt

# Installing Requirements
RUN cd /
RUN pip3 install -U -r requirements.txt

RUN mkdir /never
WORKDIR /never
ENV DOWNLOAD_URL "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-3/wkhtmltox-0.12.6-3.archlinux-x86_64.pkg.tar.xz" -L -o "wkhtmltopdf.tar.xz"

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl libxrender1 libfontconfig libxtst6 xz-utils

# Download and extract wkhtmltopdf
RUN curl $DOWNLOAD_URL
RUN tar Jxvf wkhtmltopdf.tar.xz
RUN cp usr/bin/wkhtmltopdf /never
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
