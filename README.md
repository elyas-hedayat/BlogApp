# BlogApp Project Setup

## Prerequisites

Before proceeding with the project setup, ensure that you have the following prerequisites installed:

- Python (version 3.10 or higher)
- Git
- Docker (for running the required services)

## Step 1: Clone the Repository

Open your terminal or command prompt and navigate to the directory where you want to clone the project. Run the
following command to clone the repository:

```
git clone https://github.com/elyas-hedayat/BlogApp
```

## Step 2: Set Up Virtual Environment

It's recommended to create and activate a virtual environment to isolate the project dependencies. Navigate to the
project directory and follow these steps:

1. Create a new virtual environment:

```
python -m venv env
```

2. Activate the virtual environment:

- On Windows:

```
env\Scripts\activate
```

- On Linux/macOS:

```
source env/bin/activate
```

## Step 3: Install Dependencies

With the virtual environment activated, install the project dependencies by running:

```
pip install -r requirements.txt
```

## Step 4: Set Up Environment Variables

Create a `.env` file in the project root directory by copying the example file:

```
cp .env.example .env
```

Open the `.env` file and configure the required environment variables according to your project setup.

## Step 5: Create Database Tables

Apply the initial database migrations to create the necessary tables:

```
python manage.py migrate
```

## Step 6: Start Docker Services

The project requires some additional services to be running, such as a database or a message broker. Start these
services using Docker Compose:

```
docker-compose -f docker-compose.yml up -d
```

## Step 7: Run the Development Server

With all the prerequisites set up, you can now start the development server:

```
python manage.py runserver
```

The server should be running, and you can access the application in your web browser at `http://localhost:8000`.