# Debian Based Docker
FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt-get update \
    && apt-get install -y \
    ...
    wkhtmltopdf \
    ...
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
COPY start.sh /start.sh

# Running Radio Player Bot
CMD ["/bin/bash", "/start.sh"]
