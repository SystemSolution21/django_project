# 🐳 Docker & Docker Compose Commands Reference

Complete guide for managing this LangChain RAG React Agent application and general Docker operations.

## 📋 Table of Contents

- [Container Management](#container-management)
- [Image Management](#image-management)
- [Logs & Debugging](#logs--debugging)
- [Cleanup & Maintenance](#cleanup--maintenance)
- [Ollama Management](#ollama-management)
- [Resource Monitoring](#resource-monitoring)
- [Troubleshooting](#troubleshooting)

---

### Daily Usage (Manual Start - Saves Memory)

```bash
# Start containers
docker-compose start

# Stop containers (frees memory, keeps containers)
docker-compose stop

# Run the app
docker-compose exec app python -m <script_name>
```

---

## Container Management

### Starting Containers

```bash
# Start containers (if already created)
docker-compose start

# Create and start containers(docker-compose.yml changed)
docker-compose up -d

# Force recreate containers (apply docker-compose.yml changes)
docker-compose up -d --force-recreate

# Create and start with build(Dockerfile or dependencies changed)
docker-compose up -d --build

# Start with containerized Ollama
docker-compose --profile local up -d

# Start in foreground (see logs in terminal)
docker-compose up
```

### Stopping Containers

```bash
# Stop containers (keeps them for quick restart)
docker-compose stop

# Stop specific service
docker-compose stop app

# Stop and remove containers + networks
docker-compose down

# Stop and remove everything including volumes (⚠️ DELETES DATA)
docker-compose down --volumes
```

### Restarting Containers

```bash
# Restart all containers
docker-compose restart

# Restart specific service
docker-compose restart app

```

### Container Status

```bash
# List running containers (docker-compose)
docker-compose ps

# List all Docker containers
docker ps

# List all containers (including stopped)
docker ps -a

# Show container resource usage
docker stats

# Inspect container details
docker inspect <container_name>
```

---

## Image Management

### Building Images

```bash
# Build images (doesn't start containers)
docker-compose build

# Build with no cache (fresh build)
docker-compose build --no-cache

# Build specific service
docker-compose build app

# Build and start
docker-compose up -d --build
```

### Listing Images

```bash
# List all images
docker images

# List images with size
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# List dangling images (<none>)
docker images -f "dangling=true"

# Show disk usage
docker system df

# Check which containers use an image (including stopped)
docker ps -a --filter ancestor=<image_name>

# List all containers with their images and status
docker ps -a --format "table {{.Names}}\t{{.Image}}\t{{.Status}}"
```

### Removing Images

```bash
# Remove specific image
docker rmi <image_name>

# Remove dangling images (<none>)
docker image prune -f

# Remove all unused images
docker image prune -a -f

# Remove specific image by ID
docker rmi abc123def456

# Force remove image (even if containers exist)
docker rmi -f <image_name>
```

---

## Logs & Debugging

### Viewing Logs

```bash
# View logs from all services
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# Follow logs for specific service
docker-compose logs -f app

# View last 100 lines
docker-compose logs --tail=100 app

# View logs with timestamps
docker-compose logs -f -t app

# View logs from specific container
docker logs <container_name>

# Follow container logs
docker logs -f <container_name>
```

### Accessing Containers

```bash
# Execute command in running container
docker-compose exec app bash

# Run Python script
docker-compose exec app python -m langchain_rag_react_agent.agent

# View files in container
docker-compose exec app ls -la /app/logs

# View log file content
docker-compose exec app cat /app/logs/agent_tools.log

# Follow log file in real-time
docker-compose exec app tail -f /app/logs/agent_tools.log

# Execute as root user
docker-compose exec -u root app bash

# Run one-off command
docker-compose run --rm app python --version
```

### Debugging

```bash
# Check container health
docker inspect --format='{{.State.Health.Status}}' <container_name>

# View container processes
docker-compose top

# View container resource usage
docker stats <container_name>

# Inspect container configuration
docker inspect <container_name>

# Check restart policy
docker inspect <container_name> --format='{{.HostConfig.RestartPolicy.Name}}'

# View container environment variables
docker-compose exec app env
```

---

## Cleanup & Maintenance

### Remove Containers

```bash
# Remove stopped containers
docker container prune -f

# Remove specific container
docker rm <container_name>

# Force remove running container
docker rm -f <container_name>

# Remove all stopped containers
docker rm $(docker ps -a -q)
```

### Remove Images

```bash
# Remove specific image
docker rmi <image_name>

# Remove dangling images (<none>)
docker image prune -f

# Remove all unused images
docker image prune -a -f

# Remove specific image by ID
docker rmi abc123def456

# Force remove image (even if containers exist)
docker rmi -f <image_name>
```

### Remove Volumes

```bash
# Remove unused volumes (⚠️ DELETES DATA)
docker volume prune -f

# Remove specific volume
docker volume rm langchain_rag_react_agent_ollama_data

# List volumes
docker volume ls
```

### Remove Networks

```bash
# Remove unused networks
docker network prune -f

# Remove specific network
docker network rm langchain-network

# List networks
docker network ls
```

### Complete Cleanup

```bash
# Remove everything unused (containers, networks, images, cache)
docker system prune -f

# Remove everything including volumes (⚠️ DELETES ALL DATA)
docker system prune -a --volumes -f

# Remove build cache
docker builder prune -f

# Remove everything for this project
docker-compose down --volumes --rmi all
```

### Weekly Maintenance

```bash
# Recommended weekly cleanup routine
docker image prune -f          # Remove dangling images
docker container prune -f      # Remove stopped containers
docker network prune -f        # Remove unused networks
docker builder prune -f        # Remove build cache

# Or all at once
docker system prune -f
```

---

## Ollama Management

### Using Containerized Ollama

```bash
# Start with Ollama container
docker-compose --profile local up -d

# List available models
docker exec langchain-ollama ollama list

# Pull a model
docker exec langchain-ollama ollama pull llama3.2:3b

# Pull other models
docker exec langchain-ollama ollama pull llama3.2:1b
docker exec langchain-ollama ollama pull gemma2:2b
docker exec langchain-ollama ollama pull phi3:mini

# Remove a model
docker exec langchain-ollama ollama rm llama3.2:3b

# Test Ollama API
curl http://localhost:11434/api/tags

# View Ollama logs
docker logs -f langchain-ollama

# Access Ollama container
docker exec -it langchain-ollama bash
```

### Using Local Ollama

```bash
# Set in .env file
OLLAMA_BASE_URL=http://host.docker.internal:11434

# Start without Ollama container
docker-compose up -d

# Test connection from container
docker-compose exec app curl http://host.docker.internal:11434/api/tags
```

---

## Resource Monitoring

### Memory & CPU Usage

```bash
# Real-time resource usage
docker stats

# Resource usage for specific container
docker stats <container_name>

# One-time snapshot
docker stats --no-stream

# Format output
docker stats --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

### Disk Usage

```bash
# Overall disk usage
docker system df

# Detailed disk usage
docker system df -v

# Check specific image size
docker images <image_name>

# Check volume sizes
docker volume ls
docker system df -v | grep -A 10 "Local Volumes"
```

### Network Inspection

```bash
# List networks
docker network ls

# Inspect network
docker network inspect langchain-network

# See which containers are on a network
docker network inspect langchain-network --format='{{range .Containers}}{{.Name}} {{end}}'
```

---

## Troubleshooting

### Common Issues

#### Container Won't Start

```bash
# Check logs for errors
docker-compose logs app

# Check container status
docker-compose ps

# Inspect container
docker inspect <container_name>

# Try rebuilding
docker-compose down
docker-compose up -d --build
```

#### Ollama Connection Issues

```bash
# Check Ollama is running
docker ps | grep ollama

# Test Ollama API
curl http://localhost:11434/api/tags

# Check network connectivity
docker-compose exec app curl http://ollama:11434/api/tags

# View Ollama logs
docker logs langchain-ollama
```

#### Port Already in Use

```bash
# Find what's using port 11434
netstat -ano | findstr :11434  # Windows
lsof -i :11434                 # Linux/Mac

# Stop conflicting container
docker stop <container-name>

# Change port in docker-compose.yml
ports:
  - "11435:11434"  # Use different host port
```

#### Out of Memory

```bash
# Check memory usage
docker stats

# Stop containers to free memory
docker-compose stop

# Use smaller model in .env
OLLAMA_LLM=llama3.2:1b

# Increase Docker memory limit (Docker Desktop → Settings → Resources)
```

#### Permission Issues

```bash
# Run as root
docker-compose exec -u root app bash

# Fix permissions on host
sudo chown -R $USER:$USER ./logs ./db ./pdfs

# Windows: Run Docker Desktop as Administrator
```

### Reset Everything

```bash
# Complete reset (⚠️ DELETES ALL DATA)
docker-compose down --volumes --rmi all
docker system prune -a --volumes -f

# Start fresh
docker-compose up -d --build
```

---

## 📚 Quick Reference

### Container Lifecycle

```bash
# Create → Start → Stop → Remove
docker-compose up -d        # Create & Start
docker-compose stop         # Stop (keeps container)
docker-compose start        # Start existing container
docker-compose restart      # Restart
docker-compose down         # Stop & Remove
```

### Memory vs Disk

| Action | Frees Memory | Frees Disk |
|--------|--------------|------------|
| `docker-compose stop` | ✅ Yes | ❌ No |
| `docker-compose down` | ✅ Yes | ✅ Small |
| `docker image prune -a` | ❌ No | ✅ Yes |
| `docker system prune -a` | ❌ No | ✅ Yes |

### When to Use What

| Scenario | Command |
|----------|---------|
| Daily start/stop | `docker-compose start/stop` |
| Changed Python code | `docker-compose restart app` |
| Changed .env | `docker-compose restart app` |
| Changed docker-compose.yml | `docker-compose up -d --force-recreate` |
| Changed Dockerfile | `docker-compose up -d --build` |
| Changed dependencies | `docker-compose up -d --build` |
| Free memory | `docker-compose stop` |
| Free disk space | `docker image prune -a -f` |
| Complete cleanup | `docker-compose down` |

---

## 🎯 This App Specific Commands

### Development Workflow

```bash
# Start working
docker-compose start
docker-compose exec app python -m langchain_rag_react_agent.agent

# Stop working (saves memory)
docker-compose stop

# View logs
docker-compose logs -f app
docker-compose exec app tail -f /app/logs/agent_tools.log

# Add new PDFs
# 1. Copy PDFs to ./pdfs/ directory
# 2. Restart app to rebuild vector store
docker-compose restart app
```

### Updating Dependencies

```bash
# After modifying pyproject.toml
docker-compose down
docker-compose up -d --build
```

### Switching Ollama Setup

```bash
# Switch to containerized Ollama
# 1. Edit .env: OLLAMA_BASE_URL=http://ollama:11434
# 2. Restart with profile
docker-compose down
docker-compose --profile local up -d

# Switch to local Ollama
# 1. Edit .env: OLLAMA_BASE_URL=http://host.docker.internal:11434
# 2. Restart without profile
docker-compose down
docker-compose up -d
```

---

## 💡 Tips & Best Practices

1. **Save Memory**: Use `docker-compose stop` instead of `down` for daily use
2. **Weekly Cleanup**: Run `docker system prune -f` to free disk space
3. **Check Logs**: Always check logs when troubleshooting: `docker-compose logs -f app`
4. **Volume Mounts**: Code changes in `./src` are live - no rebuild needed!
5. **Restart Policy**: Set to `"no"` for development to save memory
6. **Local Ollama**: Use local Ollama instead of containerized to save ~2-4GB RAM
7. **Smaller Models**: Use `llama3.2:1b` instead of `llama3.2:3b` to save memory
8. **Docker Desktop**: Use the GUI for easy container/image management

---

## 📖 Additional Resources

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)
- [Ollama Documentation](https://github.com/ollama/ollama)
- [Project README](README.md)
- [Development Guide](DEVELOPMENT.md)

---

**Last Updated**: 2025-11-18
