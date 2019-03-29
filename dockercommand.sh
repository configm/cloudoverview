#!/bin/bash

echo 'docker build -t "cloudoverview" .'
docker build -t "cloudoverview" .


docker ps 

sudo docker kill $(sudo docker ps |grep 1984 |awk '{print $1;}')
docker ps -a
env


sleep 3

docker ps -a

echo 'docker run -d -p 1984:1984 cloudoverview &'
docker run -d -p 1984:1984 cloudoverview 

$(aws ecr get-login --no-include-email --region us-east-1)

 docker tag cloudoverview:latest 172660532281.dkr.ecr.us-east-1.amazonaws.com/cloudoverview:latest

docker push 172660532281.dkr.ecr.us-east-1.amazonaws.com/cloudoverview:latest


kubectl delete pods -all