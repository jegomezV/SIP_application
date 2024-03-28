# Etapa de construcción del front-end
FROM node:14 as build

WORKDIR /app/client

COPY applications/sip_application/src/package*.json ./

RUN npm install

COPY applications/sip_application/client/ ./

# Etapa de construcción del backend
FROM python:3.8

# Instalar dependencias para psycopg2, PyGObject, pycairo y cairo
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    python3-apt \
    python3-gi \
    python3-gi-cairo \
    libcairo2-dev \
    libsystemd-dev \
    gir1.2-gtk-3.0 \
    libgirepository1.0-dev \
    libdbus-1-dev  \
    postgresql-client

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY . /app

# Install pip
RUN apt-get install -y python3-pip

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Copy entrypoint script into the image
COPY ./entrypoint.sh /app/entrypoint.sh


RUN chmod +x entrypoint.sh

# Run entrypoint.sh when the container launches
ENTRYPOINT ["/app/entrypoint.sh"]
