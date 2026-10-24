# Exercise 5: Docker Security with AppArmor

## Objective
Build a Flask application in Docker and explore container security using an AppArmor profile.

## Files
- `app.py` - Flask web application on port 5000.
- `Dockerfile` - Builds the application image.
- `requirements.txt` - Python dependencies.
- `my-apparmor-profile` - AppArmor profile example.
- `apply_apparmor.py` - Builds the image and starts a container with the profile option.
- `test_restricted_actions.py` - Tests selected commands inside the container.

## Requirements
- Docker Engine on a compatible Linux host.
- AppArmor enabled and supported by the host.
- Python and the Docker SDK (`pip install docker`) to run the helper scripts.

## Build and run
```bash
docker build -t flask-apparmor .
docker run --rm -p 5000:5000 flask-apparmor
```
Open `http://localhost:5000` in your browser.

## Load the AppArmor profile on Linux
Review and validate the profile for your Linux distribution and image paths first. Then install it in the host AppArmor profile directory and load it:
```bash
sudo cp my-apparmor-profile /etc/apparmor.d/my-apparmor-profile
sudo apparmor_parser -r /etc/apparmor.d/my-apparmor-profile
docker run --rm --security-opt="apparmor=my-apparmor-profile" -p 5000:5000 flask-apparmor
```

## Run the Python helper scripts
```bash
pip install docker
python apply_apparmor.py
python test_restricted_actions.py
```

## Assignment questions

### 1. What is AppArmor?
AppArmor is a Linux security module that applies per-program access-control policies to restrict what processes can access or do.

### 2. How does AppArmor improve Docker security?
It can restrict a container process access to files, capabilities, and other resources, reducing the impact of a compromised application.

### 3. What happens when a process attempts a restricted action?
The kernel can deny the operation and record an AppArmor denial in system logs, depending on the active profile and enforcement mode.

### 4. Can AppArmor completely prevent all container security risks?
No. It is one layer of defense and should be combined with least privilege, patched images, restricted capabilities, and other security controls.

### 5. What are the benefits of using AppArmor with Docker?
It provides an additional layer of mandatory access control, limits process permissions, and can reduce the potential damage caused by a compromised container.

## Platform and testing notes
AppArmor enforcement requires a compatible Linux host with AppArmor enabled and the profile loaded. Docker Desktop on Windows may not support loading a custom profile in the same way as native Linux. The profile paths and permissions must match the image, and the profile should be validated before enforcement. The Python scripts have not been verified on every platform; actual results depend on host configuration and image contents.
