# Use the official Python image from the Docker Hub
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Install dependencies
COPY . /code/
RUN pip install pipenv && pipenv install --system --deploy

# Install Django
RUN pip install django

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
