FROM python:3.10.5-buster
RUN mkdir -p /opt/real-estate-hunter
WORKDIR /opt/real-estate-hunter

# install requirements.txt
COPY requirements.txt .
RUN pip3 install -U pip
RUN pip3 install --no-cache-dir --force-reinstall -r requirements.txt

COPY real-estate-hunter-dev/app.img/*.sh /

CMD /docker-start.sh


