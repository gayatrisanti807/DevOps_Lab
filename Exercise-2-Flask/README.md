# Exercise 2: Flask Application on Kubernetes



## Objective

Deploy a Python Flask web application on a local Kubernetes cluster using Docker and Minikube.



## Technologies Used

- Python

- Flask

- Docker

- Kubernetes

- Minikube

- kubectl

- YAML



## Project Structure

```text

Exercise-2-Flask/

|-- app.py

|-- Dockerfile

|-- deployment.yaml

|-- service.yaml

`-- README.md

```



## Application Details

The Flask application runs on port `15000` and displays:



```text

Hello from Flask on Kubernetes!

```



## Implementation Steps

1\. Created a Flask application using Python.

2\. Created a Dockerfile to package the application.

3\. Built the Docker image `flask-app:v1`.

4\. Loaded the Docker image into Minikube.

5\. Created a Kubernetes Deployment using `deployment.yaml`.

6\. Created a NodePort Service using `service.yaml`.

7\. Verified the Deployment, Pod, and Service using `kubectl`.

8\. Tested the application successfully in a web browser.



## Deployment Commands



Apply the Deployment:



```powershell

kubectl apply -f deployment.yaml

```



Apply the Service:



```powershell

kubectl apply -f service.yaml

```



Check Kubernetes resources:



```powershell

kubectl get deployments,pods,services

```



View application logs:



```powershell

kubectl logs deployment/flask-app

```



Inspect the Service:



```powershell

kubectl describe service flask-service

```



## Accessing the Application

The application is exposed through a Kubernetes NodePort Service.



- Application port: `15000`

- NodePort: `30000`

- Service type: `NodePort`



To access the application through Minikube:



```powershell

minikube service flask-service --url

```



Open the URL returned by the command in your browser. Keep the terminal running while using the URL.



## Verification

- Deployment available: `1/1`

- Flask Pod status: `Running`

- Pod restarts: `0`

- Service endpoint connected to the Flask Pod

- Browser displayed `Hello from Flask on Kubernetes!`



## Result

Successfully built and deployed a Flask web application on Kubernetes using Docker and Minikube. The application was exposed through a NodePort Service and verified in a web browser.



