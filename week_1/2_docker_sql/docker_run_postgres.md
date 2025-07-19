## Running Postgres container with Docker
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v C:/Users/mathe/OneDrive/Área\ de\ Trabalho/Projetos/de-zoomcamp-lessons/week_1/2_docker_sql/postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13

To access this db by terminal:
pgcli -h localhost -p 5432 -u root -d ny_taxi

## Docker Network (Postgres db + pgadmin)
Connection between containers.

### Terminal
docker newtwork create pg-network

### Postgres container with network
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v C:/Users/mathe/OneDrive/Área\ de\ Trabalho/Projetos/de-zoomcamp-lessons/week_1/2_docker_sql/postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name=pg-database \
  postgres:13

### Pgadmin container with network
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4

### Connect to a postgres db on pgadmin ui
Right click Servers in the left sidebar -> Register -> Server
Genneral -> Name:Docker localhost
Connection -> Host:pg-database; Port:5432; Maintanance db:postgres; User:root; Pass:root