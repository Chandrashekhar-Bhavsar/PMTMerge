# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy the application code to the container
COPY . .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set ownership and switch to a non-root user
RUN chown -R 1001:0 /app
USER 1001

# Expose the port on which the application will run (optional)
EXPOSE 8080

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Flask application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app", "--log-level", "debug"]
