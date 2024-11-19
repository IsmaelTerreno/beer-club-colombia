# Use the official Python image from the Docker Hub.
FROM python:3.12.6-slim

# Set the working directory in the container.
WORKDIR /usr/src/app

# Copy the requirements file into the container.
COPY ./requirements.txt ./

# Install the required dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container.
COPY ./controller ./controller
COPY ./model ./model
COPY ./repository ./repository
COPY ./service ./service
COPY ./test ./test
COPY ./main.py ./

# Expose the port uvicorn will run on.
EXPOSE 8000

# Set the entry point for the application.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]