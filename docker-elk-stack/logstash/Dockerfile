FROM docker.elastic.co/logstash/logstash:8.5.1

RUN rm -f /usr/share/logstash/pipeline/logstash.conf

COPY pipeline/ /usr/share/logstash/pipeline/
COPY conf/ /usr/share/logstash/config/