# DevOps Capstone Project

[![CI Build](https://github.com/OWNER/REPOSITORY/actions/workflows/ci-build.yaml/badge.svg?branch=main)](https://github.com/OWNER/REPOSITORY/actions/workflows/ci-build.yaml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://www.python.org/)

**Project Name: DevOps Capstone**

This project implements the IBM DevOps Capstone Accounts REST API as part of the IBM DevOps and Software Engineering Professional Certificate.

Course: [IBM DevOps Capstone Project](https://www.coursera.org/learn/devops-capstone-project?specialization=devops-and-software-engineering)

Certificate: [IBM DevOps and Software Engineering Professional Certificate](https://www.coursera.org/professional-certificates/devops-and-software-engineering)

## Project Overview

The Accounts microservice provides REST API operations for managing account records. The project applies automated testing, continuous integration, containerization, security headers, and Kubernetes deployment practices.

## Features

- Create an account.
- List all accounts.
- Retrieve an account by ID.
- Update an account.
- Delete an account.
- Configure CORS policies and security headers.
- Run automated code linting and unit tests.
- Build a Docker image.
- Deploy the application to Kubernetes.
- Use GitHub Actions for continuous integration.

## Development Environment

The original labs are designed for the IBM Developer Skills Network Cloud IDE with OpenShift. Follow the setup instructions provided in the course environment.

Initialize the environment by sourcing the setup script:

```bash
source bin/setup.sh
```

This script configures the Python environment and activates the virtual environment.

## Useful Commands

Activate the Python virtual environment:

```bash
source ~/venv/bin/activate
```

Install project dependencies:

```bash
make install
```

Start the PostgreSQL container:

```bash
make db
```

Check running Docker containers:

```bash
docker ps
```

## Project Structure

```text
devops-capstone-project/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── user-story.md
│   └── workflows/
│       └── ci-build.yaml
├── service/
│   ├── common/
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── tests/
│   ├── factories.py
│   ├── test_cli_commands.py
│   ├── test_models.py
│   └── test_routes.py
├── Dockerfile
├── README.md
├── requirements.txt
└── setup.cfg
```

## Account Data Model

| Field | Type | Required |
|---|---|---|
| id | Integer | Yes |
| name | String(64) | Yes |
| email | String(64) | Yes |
| address | String(256) | Yes |
| phone_number | String(32) | No |
| date_joined | Date | Yes |

## Continuous Integration

The GitHub Actions workflow is stored in `.github/workflows/ci-build.yaml`.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Lints the source code using `flake8`.
5. Runs unit tests using `nosetests`.

The CI Build badge at the top of this README links to the workflow run history. It reflects the real GitHub Actions status when the workflow exists and has run.

## Testing and Code Coverage

Run the unit tests with:

```bash
nosetests
```

Run tests with coverage reporting:

```bash
nosetests --with-coverage --cover-package=service
```

The project objective is to maintain at least 95% code coverage while ensuring the tests pass.

## Docker

Build the application image:

```bash
docker build -t accounts:latest .
```

Run the container:

```bash
docker run --rm -p 8080:8080 accounts:latest
```

The application must be configured to listen on port 8080 inside the container for this command to work.

## Kubernetes and Tekton

The project can be extended to deploy the Accounts service to Kubernetes and automate build and deployment stages using Tekton.

Use the commands and manifests supplied by the course environment for cluster setup, pipeline execution, and deployment verification.

## License

Licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file.

---

© IBM Corporation 2022. All rights reserved.
