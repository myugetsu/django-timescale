# Raspberry Pi Temperature Sensor Simulation with Django and TimescaleDB

## Table of Contents
- [Raspberry Pi Temperature Sensor Simulation with Django and TimescaleDB](#raspberry-pi-temperature-sensor-simulation-with-django-and-timescaledb)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)

## Introduction
This project simulates a Raspberry Pi temperature sensor using Django for the backend and TimescaleDB for time-series data storage. The project is containerized using Docker Compose for easy setup and deployment.

## Features
- **Django**: Backend framework for the web application.
- **Django Ninja**: Fast and modern web framework for building APIs with Django.
- **TimescaleDB**: Time-series database built on PostgreSQL for storing temperature data.
- **Celery**: Distributed task queue for handling periodic sensor data generation.
- **Docker Compose**: Container orchestration for managing the application's services.


## Technologies Used
- Django
- TimescaleDB
- Docker
- Docker Compose

## Prerequisites
Ensure you have the following installed on your system:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/raspberry-pi-temp-sensor-simulation.git
    cd raspberry-pi-temp-sensor-simulation
    ```

2. **Create Environment Variables File**
    Create a `.env` file in the project root and add the following environment variables:
    ```dotenv
    DJANGO_SECRET_KEY=your_secret_key
    POSTGRES_DB=your_db_name
    POSTGRES_USER=your_db_user
    POSTGRES_PASSWORD=your_db_password
    ```

3. **Build and Run Docker Containers**
    ```bash
    docker-compose up --build
    ```

4. **Apply Migrations and Create Superuser**
    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```

## Usage
- Access the Django admin at `http://localhost:8000/admin` and log in with the superuser credentials.
- The REST API is accessible at `http://localhost:8000/api/`.

