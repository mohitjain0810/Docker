# 🐳 Ultimate Docker Guide & Command Reference

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![CI/CD Ready](https://img.shields.io/badge/CI%2FCD-Ready-brightgreen?style=for-the-badge)

A complete Docker guide with **all essential commands**, from building images to managing containers and Docker Compose. Perfect for developers and teams to hit the ground running with containerization.

---

## 🚀 What is Docker?

Docker is an open-source platform that packages applications and their dependencies into lightweight containers. Containers ensure consistency across development, testing, and production.

---

## 🗂️ Table of Contents

1. [Verify Installation](#-verify-installation)
2. [Basic Docker Commands](#-basic-docker-commands)
3. [Image Management](#-image-management)
4. [Container Management](#-container-management)
5. [Docker Compose](#-docker-compose)
6. [Maintenance & Cleanup](#-maintenance--cleanup)
7. [Production Tips](#-production-tips)
8. [Troubleshooting & Debugging](#-troubleshooting--debugging)
9. [FAQ](#-faq)

---

## ✅ Verify Installation

```bash
docker --version
docker-compose --version  # For multi-container apps

```

---

## 🔧 Basic Docker Commands

```bash
# Pull an image from Docker Hub
docker pull <image_name>

# Build an image from Dockerfile
docker build -t <image_name>:<tag> .

# Run a container from an image
docker run -d -p <host_port>:<container_port> <image_name>:<tag>

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a running container
docker stop <container_id>

# Start a stopped container
docker start <container_id>

# Remove a stopped container
docker rm <container_id>

# Remove an image
docker rmi <image_name>:<tag>

# View container logs
docker logs <container_id>

# Exec into a running container
docker exec -it <container_id> sh

```

--- 


## 📦 Image Management
```bash
# List local images
docker images

# Tag an image
docker tag <image_name>:<tag> <username>/<repo>:<tag>

# Push an image to Docker Hub
docker login
docker push <username>/<repo>:<tag>

# Pull an image from Docker Hub
docker pull <username>/<repo>:<tag>

# Remove unused images
docker image prune

# Remove all dangling (untagged) images
docker image prune -a
```

--- 

## 🚀 Container Management

```bash
# Run a container with environment variables
docker run -d \
  --name <container_name> \
  -p <host_port>:<container_port> \
  -e "ENV_VAR=value" \
  -v <host_path>:<container_path> \
  <image_name>:<tag>

# List all containers
docker ps -a

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# Check container logs
docker logs <container_id>

# Check resource usage
docker stats

# Inspect container metadata
docker inspect <container_id>
```

---

## 🐙 Docker Compose 
Example docker-compose.yml:

```bash
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - ENV_VAR=value
    depends_on:
      - redis
  redis:
    image: redis:alpine
```

Common Docker Compose Commands
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs

# Rebuild services
docker-compose up --build

# List services
docker-compose ps
```

---

## 🧹 Maintenance & Cleanup
```bash
# Remove unused containers, networks, images, and caches
docker system prune

# Remove all stopped containers
docker container prune

# Remove dangling (untagged) images
docker image prune

# Remove unused volumes
docker volume prune

# Remove all unused resources
docker system prune -a
```

---
## 🐞 Troubleshooting & Debugging
```bash
# Port in use
lsof -i :<port> && kill $(lsof -ti :<port>)

# Permission issues
docker run --user $(id -u) ...

# Check logs
docker logs -f <container_id>

# View container details
docker inspect <container_id>

# Monitor container stats
docker stats
```
---

## ❓ FAQ
1. What is Docker?
- A platform to build, ship, and run applications in containers.

2. Why use Docker?
- Ensures consistency, portability, and scalability.

3. Where to use Docker?
- Development, testing, production, and CI/CD pipelines.
