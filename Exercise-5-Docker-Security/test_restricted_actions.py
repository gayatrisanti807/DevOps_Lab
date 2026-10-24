import docker

client = docker.from_env()
container = None

try:
    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )
    print(f"Container started: {container.short_id}")

    for command, description in [
        ("cat /etc/passwd", "Attempt to read /etc/passwd"),
        ("/bin/bash", "Attempt to execute /bin/bash"),
    ]:
        result = container.exec_run(command)
        print(f"{description}: Exit Code {result.exit_code}, Output: {result.output.decode(errors='replace')}")

finally:
    if container is not None:
        container.remove(force=True)
        print("Container stopped and removed.")
