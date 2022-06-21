# Part 2: Flask App runs on Kubernetes

In this part the Flask App runs on Kubernetes

## Installation

- You need to have Minikube installed on your local machone to run a Kubernetes cluster locally. Check this [blog post](https://medium.com/gitconnected/getting-started-with-minikube-as-your-local-kubernetes-cluster-cfebf87abc39) to install minikube on your local machine.

### 1. Apply the Kubernetes Deployment
```
kubectl apply -f flask-k8s-deployment.yml
```

### 2. Apply the Kubernetes Service
```
kubectl apply -f flask-k8s-service.yml
```

### 3. Check pod runs properly:
```
kubectl get pods
kubctl get all
kubectl describe pod <pod-name>
```

### 4. Get the IP via minikube
```
minikube service --all
```

### 5. Click the link with the `ip_address:port` in the browser to open the app.

### 6. Open minikube dashboard
```
minikube dashboard
```
![](https://github.com/randiltennakoon/flask_k8s/blob/run_on_kubernetes/kubernetes_dashboard.png?raw=true)








