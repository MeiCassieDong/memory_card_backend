This is a prototype backend project with python language.
Below are the commands for running the project and the relevant website.

//API website
https://fastapi.tiangolo.com/

//install component
pip install -r requirements.txt

//run and depoloy server
uvicorn main:app --reload
uvicorn main:app --host 0.0.0.0 // let the main:app listen to all the network interfaces

//set env before compile 
. _env/bin/activate
python db.py


# 5432/tcp
docker run --name postgres -e POSTGRES_PASSWORD=gtgt  -p 5432:5432  -d postgres:12 //use docker to start single image
docker ps //show running docker containers
docker exec -it DOCKER_ID bash //get into docker, DOCKER_ID is named postgres in first line.
psql -h localhost -p 5432 -U postgres //start to run psql command
create database db;

\c db //connect to db
\dt //show tables
create table games(content text);
insert into games values ('game1');
drop table games;

//EndPoint
fetch all cards:
get is to fetch
post is to upload
localhost:8080/user_id/cards
localhost:8080/user_id/card

for users
register one user:
localhost:8080/user_name
body has email and password, user id is returned.


eg. 
Apple & Apfel
Danke & Thank you

Table users
userId user_name email                        password
0       cassie    meicassiedong@gmail.com      12345

Table cards
UserId Cards
0       Apple & Apfel
0       Danke & Thank you

https://k3d.io/v5.4.4/


docker build -t memorycard_docker_image . // build project image in current folder which has Dockerfile 
docker build -t local/memorycard_docker_image:0.0.2 . //build a local docker image which can be pull with docker desktop 

docker run -it --rm  memorycard_docker_image // start a container with the project image
docker run -it --rm python:3.9-alpine3.15 // start a container with public python image
docker run --name postgres -e POSTGRES_PASSWORD=gtgt  -p 5432:5432  -d postgres:12 //start a container with postgress image 
docker ps //show running docker containers
docker exec -it DOCKER_ID bash //get into docker, DOCKER_ID is named postgres in first line.

docker images //show all the local images
docker tag memorycard_docker_image:latest k3d-registry.localhost:12345/memorycard_docker_image:0.0.1 //add the image another tag
docker tag postgres:12 local/postgres:12 // add the image another tag
docker push k3d-registry.localhost:12345/memorycard_docker_image:0.0.1 //push image to k3 registry

kubectl create -f deployment.yaml 
kubectl apply -f deployment_memorycard.yaml // apply only the changes, avoid delete old one. 
kubectl get pods 
kubectl get pods -o wide //show pods with more status
kubectl describe deployment memorycard-dev //see the error in memorycard
kubectl describe pod postgres-prd-56f94b4b7-8ckrw //see the log in pod
kubectl describe pods //see the error in pod
kubectl delete -f deployment.yaml 
kubectl cluster-info 

kubectl logsk pods //see log in pods
kubectl logs // see logs
kubectl logs memorycard-dev-574c9d6557-nml8q // see log in one pod
sudo vi /etc/hosts 

//create secret env for postgres
kubectl create secret generic postgres --from-literal=POSTGRES_PASSWORD=mypassword
kubectl get secret postgres -o yaml
kubectl delete secret

//forward localhost:8080 to kubenetes service 80, this needs to be set when test the service from outside to kubenetes
kubectl port-forward service/memorycard-dev 8080:80

// show all endpoints, each service has one endpoint
 kubectl get endpoints 

//show all service, service can be accessed from outside
kubectl get service 