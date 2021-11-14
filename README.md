# Safe-Talk
Security Engineering Final Project - A secure messaging service written in python

## Docker
This project is run with docker containers. You will need to have docker installed to the run code.

Open terminal/cmd and cd to main directory where the docker-compose.yml file is. 

To build/run containers:
* type `docker-compose up`

To take down containers:
* type `docker-compose down`

To see what containers are running:
* type `docker ps`

To stop a container:
* type `docker stop <container_id>`

To enter containers shell:
* type `docker exec -t -i <container_id> /bin/bash`

To view logs from containers:
* type `docker logs <container_id>` 

To remove all exited containers:
* type `docker container prune`

## MySQL
The apps database runs off MySQL which is hosted separately on a container.

Database credentials: 
* password - root
* username - root
* database name - 

To access MySQL commandline client enter mysql container shell then:
* type `mysql -u root -proot`
* then type `use <database name>;`
