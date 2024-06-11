# Use the official Python image from the Docker Hub
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy only the necessary files and folders
COPY manage.py /code/
COPY pc_inventory /code/pc_inventory
COPY pc_inventoryDRF /code/pc_inventoryDRF

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
