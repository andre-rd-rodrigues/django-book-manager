# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /myproject

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /myproject/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files
COPY . /myproject/

# Ensure the entrypoint script is executable
RUN chmod +x ./entrypoint.sh

# Expose the port Django runs on
EXPOSE 8000

# Entry point for the container
ENTRYPOINT ["./entrypoint.sh"]
