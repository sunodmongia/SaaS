# Set the Python version as a build-time argument
# Default is Python 3.13 for Windows
ARG PYTHON_VERSION=3.13-windowsservercore-ltsc2022
FROM python:${PYTHON_VERSION}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip and create a virtual environment
RUN python -m ensurepip --upgrade && \
    python -m venv env && \
    env\Scripts\python -m pip install --upgrade pip

# Set the virtual environment in PATH
ENV PATH="env\Scripts;${PATH}"

# Install dependencies required by Python packages
SHELL ["powershell", "-Command"]
RUN Set-ExecutionPolicy Bypass -Scope Process -Force; \
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; \
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')); \
    choco install -y postgresql; \
    choco install -y libjpeg-turbo; \
    choco install -y cairo; \
    choco install -y mingw;

# Create the code directory
RUN mkdir src

# Set the working directory to that same code directory
WORKDIR src

# Copy the requirements file into the container
COPY requirements.txt .

# Copy the project code into the container's working directory
COPY . .

# Install the Python project requirements
RUN env\Scripts\python -m pip install -r requirements.txt

# Set the Django default project name
ARG PROJ_NAME="Saas"

# Create a batch script to run the Django project
RUN echo @echo off > paracord_runner.bat && \
    echo set RUN_PORT=%%PORT%% ^|^| set RUN_PORT=8000 >> paracord_runner.bat && \
    echo env\Scripts\python manage.py migrate --no-input >> paracord_runner.bat && \
    echo env\Scripts\gunicorn %%PROJ_NAME%%.wsgi:application --bind 0.0.0.0:%%RUN_PORT%% >> paracord_runner.bat

# Set the entrypoint command
ENTRYPOINT ["cmd", "/c", "paracord_runner.bat"]