# Use a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY AWSPythonDash/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY AWSPythonDash/ .

# Command to run the application
CMD ["python", "awss3bucket_improved_dash.py"]
