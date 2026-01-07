# Use an official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy the current folder contents into the container
COPY . .

# Expose port if it's a web app
EXPOSE 80

# Run your Python script
ENTRYPOINT ["python", "app.py"]

