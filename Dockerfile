# Use the official Python base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 8080

# Create a non-root user
RUN adduser -D myuser

# Set ownership to the non-root user
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PATH="/home/myuser/.local/bin:${PATH}"

# Start the Flask application
CMD ["flask", "run", "--port", "8080", "--host", "0.0.0.0"]
