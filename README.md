# demo api
flask CRUD app with
- docker
- redis
- celery
- postgres

# getting started

## install prerequisites
This app requires [docker &
docker-compose](https://docs.docker.com/compose/install/)

```bash
$ docker-compose version
docker-compose version 1.25.0, build 0a186604
docker-py version: 4.1.0
CPython version: 3.7.4
OpenSSL version: OpenSSL 1.1.0l  10 Sep 2019
```

## run
```bash
docker-compose up --build
```

# Testing
Exec `pytest` unit tests in the running api container

```bash
$ docker-compose exec api python -m pytest tests
```

## create
Create a new member with `curl`:

```bash
$ curl -H 'Content-Type: application/json' \
>   -d '{"members": [{"mem_id": 5556, "fname": "Hello", "lname": "World", "phone": "8185552211"}]}' \
>   127.0.0.1:8080/member
{
  "members": [
    {
      "acct_id": 4199,
      "fname": "Hello",
      "id": 1002,
      "lname": "World",
      "mem_id": 5556
    }
  ]
}
```

## get
Get that member (or other members) data by setting one or more of `id`,
`mem_id`, or `phone` as query parameters

```bash
$ curl 127.0.0.1:8080/member?id=9,10
{
  "members": [
    {
      "acct_id": 18,
      "fname": "Ody",
      "id": 9,
      "lname": "Hartnell",
      "mem_id": 2882815
    },
    {
      "acct_id": 14,
      "fname": "Ody",
      "id": 10,
      "lname": "Brimilcombe",
      "mem_id": 5306299
    }
  ]
}
```

# LICENSE
MIT
 
 
 
 
 
 
 
