# Essential Linux Commands for Debugging Django Containers

Here are the most essential Linux commands need for debugging Django container.

## 1. Getting Inside the Container

Before running any Linux commands inside the container, Need to enter it.

- **docker ps**
  - **What it does:** Lists all running containers.
  - **Why use it:** To find the **Container ID** or **Name** of the running Django app (e.g., django_project-web-1).
- **docker exec -it <container_name> /bin/bash**
  - **What it does:** Opens an interactive shell (terminal) inside the container.
  - **Why use it:** This is the "remote desktop" into the container. If /bin/bash doesn't work (some minimal images don't have it), try /bin/sh.

## 2. Permissions & User (Crucial for the app user setup)

Since configuring a non-root user (app), permission errors are the #1 issue will be face.

- **whoami**
  - **What it does:** Prints the username currently logged in as.
  - **Why use it:** Verify user is actually running as app and not root.
- **ls -la**
  - **What it does:** Lists all files (-a) in the current directory with detailed permissions (-l).
  - **Why use it:** Check if the app user owns the folders it needs to write to.
  - *Example Output:* drwxr-xr-x 2 app app 4096 ... media (This shows app owns the folder).
- **pwd**
  - **What it does:** Prints Working Directory.
  - **Why use it:** To confirm current user in /app (where the Dockerfile put the code).

## 3. Debugging Configuration

- **env** (or printenv)
  - **What it does:** Prints all environment variables.
  - **Why use it:** To verify that the .env file values (like POSTGRES_PASSWORD or SECRET_KEY) were actually passed into the container correctly.
- **cat `<filename>`**
  - **What it does:** Reads and outputs the content of a file.
  - **Why use it:** To inspect files. For example, cat /etc/os-release tells which Linux version the container is using.

## 4. Django-Specific Debugging

Once inside the container, user can run Django management commands just like do locally.

- **python manage.py shell**
  - **Why use it:** Opens a Python shell with Django loaded. Can import the models and query the database directly to see if data exists or if the DB connection is working.
- **python manage.py showmigrations**
  - **Why use it:** To see if the database migrations have actually applied.
- **python manage.py collectstatic --dry-run**
  - **Why use it:** To see where Django would put static files without actually moving them.

## 5. Processes & Networking

- **top**
  - **What it does:** Shows real-time view of running processes (like Task Manager).
  - **Why use it:** To see if gunicorn is running and how much memory/CPU it is using. (Note: ps is often missing in "slim" images, so top is a good alternative).

## Summary Workflow

If site crashes, here is a typical debugging sequence:

1. `docker logs <container_name>` (Read the error trace from outside).
2. `docker exec -it <container_name>` /bin/bash (Go inside).
3. `ls -la media/` (Check if permissions are blocking uploads).
4. `env` (Check if the database password is correct).
5. `python manage.py shell` (Try to fetch a user from the DB manually).
