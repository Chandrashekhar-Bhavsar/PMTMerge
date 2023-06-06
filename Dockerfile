# Use the official Python base image
FROM python:3.9

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



# # Use the official Python base image
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /app

# # Upgrade pip
# RUN python -m pip install --no-cache-dir --upgrade pip

# # Install virtualenv
# RUN python -m pip install --no-cache-dir virtualenv

# # Create and activate a virtual environment
# RUN python -m venv venv
# RUN /bin/bash -c "source venv/bin/activate"

# # Copy the application code to the container
# COPY . .

# # Install the project dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Set ownership and switch to a non-root user
# RUN chown -R 1001:0 /app
# USER 1001

# # Expose the port on which the application will run (optional)
# EXPOSE 5000

# # Set environment variables
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# # Start the Flask application using Gunicorn
# ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--log-level", "debug"]
