\# Exercise 4: Docker Networking with Multiple Containers



\## Objective

To understand Docker bridge networking and configure communication between a Flask REST API, MySQL database, and Redis cache using a custom Docker network.



\## Technologies Used

\- Docker

\- Python 3.9

\- Flask 2.0.1

\- Werkzeug 2.0.3

\- MySQL

\- Redis



\## Project Structure

```text

Exercise-4-Docker-Networking/

├── app.py

├── requirements.txt

├── Dockerfile

├── README.md

└── screenshots/

&#x20;   └── 04-network-connectivity.png

```



\## Implementation



\### 1. Create a Custom Bridge Network

```powershell

docker network create --driver bridge my-bridge-net

docker network ls

docker network inspect my-bridge-net

```



The custom bridge network enables isolated communication between connected containers.



\### 2. Create the Flask REST API

The Flask application exposes a GET endpoint at `/about`, returning the API name, version, and description in JSON format.



\### 3. Build the Docker Image

```powershell

docker build -t flask-api .

```



\### 4. Start the MySQL Container

```powershell

docker run -d --name mysql --network my-bridge-net -e MYSQL\_ROOT\_PASSWORD=<LAB\_PASSWORD> mysql:latest

```



\### 5. Start the Redis Container

```powershell

docker run -d --name redis --network my-bridge-net redis:latest

```



\### 6. Start the Flask Container

```powershell

docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api

```



\### 7. Test the Flask API

```powershell

curl.exe http://localhost:5001/about

```



Expected response:

```json

{

&#x20; "description": "This is a simple REST API built with Flask.",

&#x20; "name": "Simple REST API",

&#x20; "version": "1.0"

}

```



\### 8. Verify Container Connectivity

Resolve the MySQL container name:

```powershell

docker exec flask python -c "import socket; print('MySQL IP:', socket.gethostbyname('mysql'))"

```



Resolve the Redis container name:

```powershell

docker exec flask python -c "import socket; print('Redis IP:', socket.gethostbyname('redis'))"

```



Test both service ports:

```powershell

docker exec flask python -c "import socket; \[(lambda s: (print(f'{host}:{port}', 'OPEN' if s.connect\_ex((host,port))==0 else 'CLOSED'), s.close()))(socket.socket()) for host,port in \[('mysql',3306),('redis',6379)]]"

```



\## Results

\- Created a custom Docker bridge network named `my-bridge-net`.

\- Started Flask, MySQL, and Redis containers on the same network.

\- Successfully accessed the Flask `/about` endpoint on port 5001.

\- Confirmed that Flask resolves MySQL and Redis through Docker's internal DNS.

\- Confirmed successful TCP connectivity to MySQL port 3306 and Redis port 6379.



\## Viva Questions and Answers



\### 1. What is the purpose of `--network`?

It connects a container to a specified Docker network, allowing it to communicate with other containers attached to that network.



\### 2. How do containers communicate by name?

On a user-defined bridge network, Docker provides internal DNS resolution, allowing containers to locate one another using their container names.



\### 3. What is the difference between bridge and host networking?

\- \*\*Bridge:\*\* Containers use an isolated virtual network. Ports can be published to the host using `-p`.

\- \*\*Host:\*\* On supported platforms, the container shares the host's network namespace and does not use the same port-mapping model.



\### 4. What does `-p 5001:5001` mean?

It maps port 5001 on the host to port 5001 inside the Flask container, allowing the API to be accessed from the host.



\## Cleanup

After capturing all required evidence, stop and remove the lab containers and delete the custom network:



```powershell

docker stop flask redis mysql

docker rm flask redis mysql

docker network rm my-bridge-net

```



\## Evidence

See `screenshots/04-network-connectivity.png` for the successful container connectivity tests.



