# Auther: Ecohnoch

# 构建一个本地镜像
docker build -t test-k8s:latest ./

kubectl get pods
kubectl delete deployment test-k8s
kubectl delete service test-k8s
kubectl create -f test_k8s_service.yaml


