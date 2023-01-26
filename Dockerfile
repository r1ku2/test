# For more information, please refer to https://aka.ms/vscode-docker-python
# you can reduce the docker image size by using python:3.x-slim-buster
#FROM python:3.8
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# for python:fullpackage
RUN apt-get update && apt-get upgrade -y

WORKDIR /app

# Exposing default port for streamlit
EXPOSE 8501

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN python -m pip install -r requirements.txt

# Copy necessary files
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Launch app when container is run
CMD python seleni_test.py
