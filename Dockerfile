# Use a locally available Python 3.9 image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Flask application
CMD ["flask", "run"]
