FROM python:3.12

#Set enviroment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#Pipenv configs
# Tell pipenv to create virtualenv in the project directory
ENV PIPENV_VENV_IN_PROJECT=1
# # Prevent pipenv from trying to create a virtual environment in the user's home
# ENV PIPENV_IGNORE_VIRTUALENVS=1


# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install dependecies
RUN pipenv install --system --deploy

# Copy the rest of the app
COPY . .

# Create and switch to non-root user for security
RUN adduser --disabled-password --gecos '' myuser
USER myuser
