# Counter Service

Flask web app that tracks GET/POST request counts.

## Features

- GET `/` - Shows request dashboard, increments GET counter
- POST `/` - Increments POST counter

## Run

```bash
# Local
python counter-service.py

# Docker
docker build . && docker run -p 8080:80

# Kubernetes
make deploy
```

## CI/CD

- Auto-build on PR
- Deploy on merge to main
- Semantic versioning via VERSION file
