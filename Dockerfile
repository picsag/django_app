FROM postgres:15.1-alpine

LABEL author="Petru Radu"
LABEL description="Postgres Image for demo"
LABEL version="1.0"

COPY init.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_HOST_AUTH_METHOD trust

EXPOSE 5432

