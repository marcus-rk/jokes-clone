# Use a specific platform to ensure compatibility with Azure
FROM --platform=linux/amd64 python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY *.py .

# Expose port 80 to ensure it's accessible externally
EXPOSE 80

# Command to run the app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]

#FROM python:3.9-slim
#
#WORKDIR /app
#
#COPY requirements.txt .
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY *.py .
#
# command to run on container start. gunicorn is a WSGI HTTP server
#CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]