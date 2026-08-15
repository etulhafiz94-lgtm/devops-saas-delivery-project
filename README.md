# DevOps SaaS Delivery Project

## Overview

This project demonstrates a modern DevOps delivery workflow for a small SaaS application. It is based on a growing SaaS organisation moving away from manual deployments, inconsistent environments and limited operational visibility.

The implementation demonstrates automated testing, continuous integration, containerisation, Infrastructure as Code, security scanning and basic application observability.

## Technology Stack

- Python 3.10
- Flask
- Pytest
- GitHub Actions
- Docker
- Terraform
- AWS Infrastructure as Code
- pip-audit

## Project Structure

```text
devops-saas-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── infrastructure/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── tests/
│   └── test_app.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md