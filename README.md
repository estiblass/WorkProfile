WorkProfile – CI/CD Level 2

WorkProfile is an advanced project demonstrating a CI/CD pipeline for a professional profile management application with MySQL integration. It uses Docker Compose for local testing and Kubernetes with StatefulSets for production deployment.

🎯 Project Goals

Multi-tier architecture: frontend → backend → database

MySQL integration with data persistence

Docker Compose for local development and E2E testing

Kubernetes deployment with StatefulSets for database reliability

CI/CD pipeline with GitHub Actions using simplified curl-based tests

Secure management of Secrets, ConfigMaps, and environment variables

🛠️ Technologies

Python 3.8+ – application development

Flask – backend framework

MySQL 8 – database

Docker & Docker Compose – local 3-tier environment

Kubernetes & StatefulSets – production-ready deployment

GitHub Actions – CI/CD automation

Nginx – reverse proxy and load balancer (local port 8080)

📁 Repository Structure
workprofile-advanced/
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml
├── k8s/
│   ├── mysql-secret.yaml
│   ├── mysql-statefulset.yaml
│   ├── mysql-service.yaml
│   ├── workprofile-configmap.yaml
│   ├── workprofile-deployment.yaml
│   └── workprofile-service.yaml
├── docker-compose/
│   ├── docker-compose.yml
│   └── nginx.conf
├── src/
│   └── [application code]
├── Dockerfile
├── requirements.txt
└── README.md

🚀 Installation & Running Locally
Requirements

Python 3.8+

Docker + Docker Compose

Kubernetes (Killercoda or kind)

GitHub repository with full application code

Docker Hub or GHCR account

Run Locally

Clone the repository:

git clone https://github.com/estiblass/WorkProfile.git
cd WorkProfile


Start the 3-tier stack:

cd docker-compose
docker-compose up -d


Access the app:

http://localhost:8080


Health check:

curl http://localhost:8080/health
# Expected: "Database: Healthy"


Stop and clean up:

docker-compose down -v

☑️ CI/CD Pipeline (GitHub Actions)

The pipeline includes 6 stages:

Basic Validation – Check required files and Python imports (Flask, MySQL connector).

Build & Test Application – Build Docker image and run single-container curl tests.

3-Tier Stack Testing – Docker Compose stack testing, Nginx reverse proxy, database connectivity.

Publish – Push Docker image to registry with semantic versioning.

Kubernetes Deployment Testing – Deploy MySQL StatefulSet and WorkProfile Deployment; test health, persistence, and CRUD.

Manual Deployment – Detailed instructions for Killercoda deployment and verification.

🔧 Kubernetes Manifests

MySQL Secret – Database credentials

MySQL StatefulSet – Persistent storage, health checks, resource limits

MySQL Services – Headless + ClusterIP

WorkProfile ConfigMap – Non-sensitive config

WorkProfile Deployment – InitContainers wait for DB readiness

WorkProfile Service – NodePort for external access

✅ Testing

Endpoint tests: / and /health

Database connectivity and CRUD

Data persistence after pod restarts

StatefulSet, PVCs, and resource limits verification

Simplified curl-based tests for all pipeline stages

📊 CI/CD Workflow Diagram
[Basic Validation] → [Build & Test Container] → [3-Tier Docker Compose] 
→ [Publish Image] → [Kubernetes Deployment] → [Manual Killercoda Deployment]
