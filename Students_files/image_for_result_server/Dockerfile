# Use an official Python runtime as a parent image
FROM python:3.9-alpine
# Set a working directory for the app
WORKDIR /app
# Copy the current directory contents into the container
COPY . .
# Install dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt
# Expose port 80
EXPOSE 80
# Define the command to run your app
CMD ["python", "app.py"]
