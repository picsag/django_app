# Django App
Steps to set up the Django project and REST framework:

1. Install Django and Django REST framework in your development environment.<br>
2. Create a new Django project using the command django-admin startproject table_builder.<br>
3. Change into the project directory using cd table_builder.<br>
4. Create a new Django app using python manage.py startapp api.<br>

## Steps for Creating PostgreSQL Docker Container

1. Clone or download the repository containing the Django app.

2. Ensure Docker is installed on your system. If not, follow the Docker installation instructions for your operating system.

3. Navigate to the directory containing the `Dockerfile` and `init.sql` file.

4. Open the `init.sql` file and modify it according to your desired PostgreSQL database setup. For example, you can create a database, grant privileges, and set configuration options.

5. Open the terminal or command prompt and build the Docker image by running the following command:

docker build -t database .

6. Once the image is built, create and run the Docker container by executing the following command:

docker run -p 5432:5432 --name your_container_name -d database

7. Wait for the PostgreSQL container to initialize. You can monitor the container logs by running the command:

docker logs your_container_name

8. Once the container is initialized and the PostgreSQL database is ready to accept connections, you can connect to the database using the default credentials (`postgres` user with no password) and the specified database name.

9. Update the Django app's database configuration (`settings.py`) with the appropriate PostgreSQL host, port, database name, username, and password.

10. Start your Django app and test the database connection to ensure it is working properly.


