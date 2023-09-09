# Dockerized Python Application

This is a Python application template that demonstrates how to containerize a Python application using Docker. The project structure includes Dockerfiles, Docker Compose configuration, and source code files.

## Project structure

```zsh
.
├── README.md
├── docker
│   └── Dockerfile
├── docker-compose.yml
├── envs
│   ├── dev.env
│   └── prd.env
└── src
    ├── __pycache__
    ├── app.py
    ├── requirements.txt
    └── utils.py
```

- docker: Directory containing Docker-related files.
  - Dockerfile: Defines how the Docker image for the application should be built.
- docker-compose.yml: Configuration file for Docker Compose, which defines how to run the application's containers.
- envs: Contains environment variable files for different environments.
  - dev.env: Environment variables for the development environment.
  - prd.env: Environment variables for the production environment.
- src: Contains the application source code.
  - app.py: The main Python application script.
  - requirements.txt: Lists the Python dependencies required by the application.
  - utils.py: A utility module with functions for loading environment variables and working with MySQL.

## Docker Setup

This project uses Docker to containerize the Python application. Here's how it works:

### Dockerfile

The docker/Dockerfile contains the instructions for building the Docker image in two stages. It first installs the Python dependencies defined in requirements.txt and then sets up the final image to run the application.

### Docker Compose

The docker-compose.yml file defines two services, docker-demo-dev and docker-demo-prd, which use the same Docker image but have different environment configurations. Docker Compose allows running multiple containers with shared configurations.

### Environment Variables

Environment variables are stored in separate .env files (envs/dev.env and envs/prd.env) for each environment. These environment files are not included in the repository for security reasons. You should create these files locally based on the provided examples and adjust the values as needed.

## How to Use

Follow these steps to set up and run the Dockerized Python application:

- Clone this repository to your local machine.
- Create environment variable files for both development and production environments. You can use the provided examples (envs/dev.env and envs/prd.env) as templates.
- Build the Docker image:

```docker
docker-compose build
```

- Start the development environment:

```docker
docker-compose up -d docker-demo-dev
```

The -d flag runs the container in detached mode.

- Start the production environment (optional):

```docker
docker-compose up -d docker-demo-prd
``````

- You can access the development environment by running:

```docker
docker-compose exec docker-demo-dev bash
```

- This opens a shell inside the container, allowing you to interact with the application.
- To access the production environment, replace docker-demo-dev with docker-demo-prd in the above command.
- Make changes to the Python code in the src directory. You can save changes, and they will be reflected immediately inside the container without the need for container recreation.
- Stop and remove the containers when you're done:

```docker
docker-compose down
```

## Conclusion

This Dockerized Python application template simplifies the development and deployment process. It allows you to run the application in different environments with minimal configuration changes. Enjoy developing your Python applications with Docker!
