# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY app /app

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
