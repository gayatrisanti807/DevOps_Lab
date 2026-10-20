\# Exercise 3: Scaling Flask App on a Single Node Using ReplicaSets



\## 1. Objective



To deploy a Flask web application on Kubernetes using a ReplicaSet, scale the application to five replicas, expose it through a Kubernetes Service, and verify automatic Pod replacement when a Pod is deleted.



\## 2. Real-Life Use Case



During an e-commerce flash sale, the number of customer requests can increase suddenly. Running an application in a single Pod may not be sufficient. Kubernetes ReplicaSets maintain the desired number of application Pods, helping the application remain available when a Pod fails or is deleted.



\## 3. Technologies Used



\- Docker

\- Kubernetes

\- Minikube

\- kubectl

\- Python

\- Flask

\- Gunicorn

\- PowerShell



\## 4. Application Features



The Flask application provides three endpoints:



\- `/` — Displays a welcome message and the name of the Pod handling the request.

\- `/buy` — Simulates a purchase and returns the selected item, user ID, status, time, and serving Pod.

\- `/health` — Returns the application's health status and Pod name.



\## 5. Implementation Steps



\### Step 1: Build the Docker Image



The application image was built inside Minikube:



```powershell

minikube image build -t flashsale:1.0 .

```



\### Step 2: Deploy the ReplicaSet and Service



```powershell

kubectl apply -f flashsale-replicaset.yaml

```



The ReplicaSet initially created three application Pods. The Kubernetes Service exposed the application internally on port 80 and forwarded requests to container port 5000.



\### Step 3: Scale the Application



```powershell

kubectl scale rs flashsale-rs --replicas=5

```



The ReplicaSet scaled the application from three to five Pods.



\### Step 4: Verify the ReplicaSet



```powershell

kubectl get rs flashsale-rs

```



Observed result:



| NAME | DESIRED | CURRENT | READY |

|---|---:|---:|---:|

| flashsale-rs | 5 | 5 | 5 |



\### Step 5: Verify the Pods



```powershell

kubectl get pods -l app=flashsale -o wide

```



Five Pods were in the `Running` state and assigned to the single Minikube node.



\### Step 6: Access the Application



```powershell

kubectl port-forward service/flashsale-svc 8080:80

```



The application was accessed locally at `http://localhost:8080`.



Test the endpoints:



```powershell

curl.exe http://localhost:8080/

curl.exe "http://localhost:8080/buy?user=123"

curl.exe http://localhost:8080/health

```



The homepage and purchase endpoints returned successful JSON responses. The health endpoint returned:



```json

{

&#x20; "pod": "flashsale-rs-vhhmt",

&#x20; "status": "healthy"

}

```



\### Step 7: Test Self-Healing



A running application Pod was deleted:



```powershell

kubectl delete pod flashsale-rs-5jwq9

```



The ReplicaSet automatically created a replacement Pod named `flashsale-rs-x7kmm`.



Verification command:



```powershell

kubectl get pods -l app=flashsale

```



Five Pods were running again, confirming the self-healing behavior of the ReplicaSet.



\## 6. Final Results



\- Successfully built the Flask application image.

\- Deployed the application using a Kubernetes ReplicaSet.

\- Scaled the application to five replicas.

\- Exposed the application using a Kubernetes Service.

\- Tested the homepage, purchase, and health endpoints.

\- Verified that all five Pods ran on a single Minikube node.

\- Confirmed automatic Pod replacement after deleting a Pod.



\## 7. Assignment Questions and Answers



\*\*Q1. How many replicas were initially created?\*\*



Three replicas were initially created.



\*\*Q2. What happened when the replicas were scaled to five?\*\*



Kubernetes created two additional Pods to reach the desired count of five.



\*\*Q3. What happened when one Pod was deleted?\*\*



The ReplicaSet detected that the actual number of Pods was below the desired count and automatically created a replacement Pod.



\*\*Q4. How does a ReplicaSet maintain the desired number of Pods?\*\*



It continuously compares the actual number of matching Pods with the desired replica count and creates or removes Pods as necessary.



\*\*Q5. Where did the application Pods run?\*\*



All five application Pods ran on the single Minikube node.



\*\*Q6. What is the purpose of the Kubernetes Service?\*\*



The Service provides a stable network endpoint for accessing the application and routes requests to eligible application Pods.



\## 8. Conclusion



The exercise demonstrated Kubernetes ReplicaSet scaling and self-healing using a Flask application that simulates an e-commerce flash sale. The application successfully ran with five replicas on a single Minikube node, and Kubernetes automatically replaced a deleted Pod to maintain the desired replica count.

