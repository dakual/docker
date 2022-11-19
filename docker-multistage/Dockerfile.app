FROM python:3.8-alpine AS build

RUN apk add --no-cache build-base linux-headers

RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

WORKDIR /app
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8-alpine

COPY --from=build /venv /venv

ENV APP_HOME=/app
ENV PATH=/venv/bin:$PATH

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY app $APP_HOME
COPY ./entrypoint.prod.sh $APP_HOME

HEALTHCHECK --interval=60s --timeout=12s CMD python -c "import requests; requests.get('http://localhost:5000', timeout=2)"

# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
ENTRYPOINT [ "/bin/sh", "-c", "sh ${APP_HOME}/entrypoint.prod.sh" ]
