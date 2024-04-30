# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements.txt file from the host to the container
COPY ./requirements.txt /code/requirements.txt

# Install the Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the entire app directory from the host to the container
COPY ./app /code/app

# Command to run when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
