# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FS script into the container
COPY fs.py .

# Expose the port the app runs on
EXPOSE 9090

# Run the FS script when the container launches
CMD ["python", "fs.py"]