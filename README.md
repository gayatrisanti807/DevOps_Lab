# Kubernetes Hands-On Exercise 1: Deploy Nginx on Minikube

## Aim
To deploy an Nginx Pod on a local Kubernetes cluster using Minikube, expose it through a NodePort Service, and verify that the application is accessible.

## Tools Used
- Docker Desktop
- Minikube
- Kubernetes
- kubectl
- Nginx

## Procedure
1. Start the Kubernetes cluster using `minikube start --driver=docker`.
2. Verify the Kubernetes node using `kubectl get nodes`.
3. Create the Nginx Pod using `kubectl run hello-k8s --image=nginx`.
4. Verify that the Pod is running using `kubectl get pods`.
5. Expose the Pod using a NodePort Service with `kubectl expose pod hello-k8s --type=NodePort --port=80`.
6. Verify the Service using `kubectl get services`.
7. Access the Nginx website using `minikube service hello-k8s` and verify that the Welcome to nginx page appears.

## Result
The Nginx Pod was successfully deployed on Minikube, exposed through a NodePort Service, and accessed through a web browser. The Welcome to nginx page was displayed successfully.

## Key Learnings
- A Pod is the smallest deployable unit in Kubernetes.
- Minikube runs a local Kubernetes cluster.
- kubectl is used to manage Kubernetes resources.
- A NodePort Service exposes an application through a port on the cluster node.
