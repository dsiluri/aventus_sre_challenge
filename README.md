# aventus_sre_challenge

# FastAPI backend
Clone this Github repo and execute docker-compose up to spin up the two containers, one is the Python FastAPI backend and the other is the Postgres db:

To test the endpoiints use the following curl calls:

```
curl http://localhost:8080/populate
curl http://localhost:8080/delete
```

# Helm chart
Helm chart was tested locally on Minikube, here below the steps necessary to get it working locally:

```
minikube start --driver=docker --container-runtime=containerd
minikube addons enable ingress
```
on the values.yaml replace ingressHost value with a local dns name (must be present on your /etc/hosts file)

Deploy the Helm chart:
```
helm install backendchart backendChart
```

Test the endpoints by replacing the host value with the one you used on the ingress deployment, in my case:
```
curl http://minikube.localhost:8080/populate
curl http://minikube.localhost:8080/delete
```
