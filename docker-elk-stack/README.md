## ELK Stack with RabbitMQ

```sh
docker compose up -d
```
> http://localhost:5601/


Test
```sh
cat /var/log/syslog | nc -q0 localhost 5000

curl -u logger:logger -X POST \
  -H "Content-Type:application/json" \
  -d '{"properties":{"content-type": "application/json"},"routing_key":"test","payload":"{\"Message\":\"hello world\"}","payload_encoding":"string"}' \
  http://localhost:15672/api/exchanges/%2F/logstash.topic/publish
```