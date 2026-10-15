\# Containerized Flask App on AWS



A small Flask app packaged with Docker, stored in Amazon ECR, and deployed on

Amazon ECS Express Mode. A GitHub Actions pipeline builds and deploys it on every push to `main`.



\## Architecture



Push to GitHub -> GitHub Actions -> Docker build -> Amazon ECR -> ECS Express Mode -> HTTPS URL



\## Project files



| File | Purpose |

|---|---|

| app.py | Flask app (home page shows version and container hostname, /health for health checks) |

| requirements.txt | Python dependency (Flask) |

| Dockerfile | Instructions to build the image |

| .dockerignore | Files kept out of the image |

| .github/workflows/deploy.yml | CI/CD pipeline |



\## Run locally



&#x20;   docker build -t my-app:v1 .

&#x20;   docker run -d -p 5000:5000 --name my-app-test my-app:v1



Open http://localhost:5000



\## How the pipeline works



1\. A push to the `main` branch starts the workflow.

2\. The workflow logs in to AWS and Amazon ECR.

3\. It builds the image and pushes it to ECR, tagged with the commit ID.

4\. It updates the ECS Express Mode service to use the new image.

5\. ECS replaces the old task with the new one (rolling deployment).

6\. The live AWS environment was taken down after testing.



AWS credentials are stored as GitHub Secrets and are never committed to the repo.



\## What I learned



\- Images vs containers, and why a registry is needed

\- Why a containerized Flask app must listen on 0.0.0.0

\- Tagging images with version numbers or commit IDs

\- Rolling deployments and health checks

\- Keeping credentials out of source code with GitHub Secrets

