//API website
https://fastapi.tiangolo.com/

//install component
pip install -r requirements.txt

//run and depoloy server
uvicorn server:app --reload

//set env before compile 
. _env/bin/activate
python db.py


# 5432/tcp
docker run --name postgres -e POSTGRES_PASSWORD=gtgt  -p 5432:5432  -d postgres:12 //run docker
docker ps //check docker process
docker exec -it DOCKER_ID bash //get into docker, DOCKER_ID is named postgres in first line.
psql -h localhost -p 5432 -U postgres //connect psql database
create database db;

\c db //connect to db
\dt //show tables
create table games(content text);
insert into games values ('game1');

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