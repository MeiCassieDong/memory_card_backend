FROM python:3.9-alpine3.15 as py39
#run apk add gcc musl-dev libffi-dev g++
add requirements.txt /tmp/requirements.txt
RUN apk add musl-dev gcc postgresql-dev g++
run pip3 install --upgrade pip && pip3 install -r /tmp/requirements.txt
#ADD gitlab_workflow_webhook /usr/local/lib/python3.9/site-packages/gitlab_workflow_webhook


FROM python:3.9-alpine3.15
RUN apk add postgresql-libs
COPY --from=py39 /usr/local/bin /usr/local/bin
COPY --from=py39 /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
ADD memorycard_backend/ /src
WORKDIR /src
EXPOSE 8000
ENV DB_HOST=127.0.0.1:5432
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
