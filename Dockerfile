# For more information, please refer to https://aka.ms/vscode-docker-python
# you can reduce the docker image size by using python:3.x-slim-buster
FROM python:3.8

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN python -m pip install -r requirements.txt

# Copy necessary files
COPY . /app

# Launch app when container is run
CMD ["python", "seleni_test.py"]
