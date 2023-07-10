-- Create a PostgreSQL user
CREATE USER postgres1 WITH PASSWORD 'postgres';

-- Create a PostgreSQL database
CREATE DATABASE db;

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE db TO postgres;

-- Set default encoding and other configuration options (optional)
ALTER DATABASE db SET client_encoding TO 'utf8';
ALTER DATABASE db SET timezone TO 'UTC';
