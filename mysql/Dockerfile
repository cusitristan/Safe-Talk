FROM mysql:8.0.22

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_PASSWORD=root

COPY mysql_schema.sql /docker-entrypoint-initdb.d

RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/