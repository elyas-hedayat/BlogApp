# BlogApp Project Setup

## Prerequisites

Before proceeding with the project setup, ensure that you have the following prerequisites installed:

- Git
- Docker (for running the required services)

## Step 1: Clone the Repository

Open your terminal or command prompt and navigate to the directory where you want to clone the project. Run the
following command to clone the repository:

```
git clone https://github.com/elyas-hedayat/BlogApp
```


## Step 2: Set Up Environment Variables

Create a `.env` file in the project root directory by copying the example file:

```
cp .env.example .env
```

Open the `.env` file and configure the required environment variables according to your project setup.

## Step 3: Start Docker Services

The project requires some additional services to be running, such as a database or a message broker. Start these
services using Docker Compose:

```
docker-compose -f docker-compose.yml up -d
```

The server should be running, and you can access the application in your web browser at `http://127.0.0.1:8000`.

### default admin user data

```
DJANGO_SUPERUSER_EMAIL=admin@gmail.com
DJANGO_SUPERUSER_PASSWORD=12345678
```