```sh
docker inspect --format "{{json .State.Health }}" <container-name> | jq
docker rmi $(docker images -f "dangling=true" -q)
docker inspect <container-name> | jq .[].Mounts
docker volume ls
docker volume inspect <volume-name>
```