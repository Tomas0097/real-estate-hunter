FROM mariadb:10.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && apt-get clean

COPY real-estate-hunter-dev/db.img/*.sh real-estate-hunter-dev/db.img/*.sql /
