FROM postgres:15.1-alpine

LABEL author="Petru Radu"
LABEL description="Postgres Image for demo"
LABEL version="1.0"

COPY *.sql /docker-entrypoint-initdb.d/

# Expose the default PostgreSQL port (optional)
EXPOSE 5432
