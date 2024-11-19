# Use the official Python image from the Docker Hub.
FROM python:3.12.6-slim

# Set the working directory in the container.
WORKDIR /usr/src/app

# Copy the requirements file into the container.
COPY ../requirements.txt ./

# Install the required dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container.
COPY ../controller ./app/controller
COPY ../model ./app/model
COPY ../repository ./app/repository
COPY ../service ./app/service
COPY ../test ./app/test
COPY ../main.py ./app

# Set the entry point for the application.
CMD ["python", "app/main.py"]