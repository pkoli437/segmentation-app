# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r req.txt

# Expose the port your Flask app will run on
EXPOSE 5001

# Run the Flask app
CMD ["python3", "app.py"]
