# pg1-lib-solution

This repository is a back-end service built on Flask, PostgreSQL, Docker (w/ Docker-compose).

Technologies:
- Python (3.10.12) w/ Flask,
- SQL with PostgreSQL, Marshmallow, SQLAlchemy
- Docker & Docker-compose

Security & auth:
- Flask-JWT-Extended

## Starting the project

### Build
```bash
cd envs/dev
docker compose build
```

## Launching
Dev:
```bash
docker-compose -f envs/dev/docker-compose.yml up 
```

Prod:
```bash
docker-compose up --build
```