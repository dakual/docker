```sh
docker inspect --format "{{json .State.Health }}" <container-name> | jq
docker rmi $(docker images -f "dangling=true" -q)
docker inspect <container-name> | jq .[].Mounts
docker volume ls
docker volume inspect <volume-name>

# comtaier ips
docker inspect -f '{{.Name}} - {{.NetworkSettings.IPAddress }}' $(docker ps -aq)

# compose ips
docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)

```