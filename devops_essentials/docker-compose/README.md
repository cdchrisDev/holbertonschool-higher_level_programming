# Docker compose
## Objectives
Define two services in a Docker Compose YAML file:
1. **PostgreSQL**: A relational database management system
2. **pgAdming**: A web-based administration tool for PostgreSQL
The main goals are:<br />
* Set up a private network that both containers will use.
* Allow public access only from the pgAdmin container
* Ensure pgAdmin can connect and manage the PostgreSQL database
* Explicitle configure the dependecy between services, so the PostgreSQL container always starts before pgAdmin.
### Resources
* [Docker Compose documentation](https://docs.docker.com/compose/)
* [PostgreSQL docker image documentation](https://hub.docker.com/_/postgres)
* [pgAdmin Docker image documentation](https://hub.docker.com/r/dpage/pgadmin4/)