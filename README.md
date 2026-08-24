# Felix Amoah — DevSecOps Engineer

![DevSecOps](https://img.shields.io/badge/DevSecOps-In%20Training-blue)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange)
![GitHub](https://img.shields.io/badge/GitHub-Source%20Control-black)
![AWS](https://img.shields.io/badge/AWS-Cloud%20Infrastructure-orange)
![Terraform](https://img.shields.io/badge/Terraform-Infrastructure%20as%20Code-purple)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Python](https://img.shields.io/badge/Python-Flask-yellow)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Automation-green)

## About

I am **Felix Amoah**, a DevSecOps Engineer in training focused on building practical skills in **cloud infrastructure, containerization, automation, security, and CI/CD**.

I am currently completing a six-month DevSecOps training program while working as an **Assistant Pipe Fitter Cum Rigger** with Emkan for Engineering and Contracting Services.

My transition into technology is driven by a strong interest in building secure, automated, and reliable infrastructure.

My current focus areas include:

* Cloud Engineering
* DevSecOps
* AWS Infrastructure
* Infrastructure as Code
* Containerization
* CI/CD Automation
* Cloud Security
* Cybersecurity
* Infrastructure Automation

---

## Featured DevSecOps Application

### Secure Containerized Flask Application

One of my current projects is a containerized Flask application designed to demonstrate a practical DevSecOps deployment workflow.

The application is packaged with Docker, stored in **Amazon ECR**, and deployed using **Amazon ECS/Fargate**.

### Deployment Flow

```text
                    Developer
                        |
                        | Git Push
                        v
                  GitHub Repository
                        |
                        v
                 CI/CD Pipeline
                        |
              +---------+---------+
              |                   |
              v                   v
        Code Validation      Security Scanning
              |                   |
              +---------+---------+
                        |
                        v
                  Docker Build
                        |
                        v
                  Amazon ECR
                        |
                        v
                 Amazon ECS
                    Fargate
                        |
                        v
                 AWS Networking
                        |
                        v
                  Public Web App
```

### Application

The application exposes a web interface and health-check endpoint:

```text
/
 /health
```

The containerized application runs on port:

```text
5000
```

The deployment demonstrates:

* Docker containerization
* Multi-stage Docker builds
* Python/Flask application deployment
* Non-root container execution
* Amazon ECR image management
* Amazon ECS/Fargate deployment
* AWS VPC networking
* Security group configuration
* Application health checks
* Container troubleshooting
* Cloud deployment troubleshooting

---

## DevSecOps Security Practices

Security is incorporated throughout the development and deployment lifecycle rather than treated as a final step.

Current practices include:

* Least-privilege principles
* Secret management
* `.gitignore` protection for sensitive files
* `.dockerignore` usage
* GPG-signed Git commits
* Container security practices
* Dependency scanning
* Secret scanning
* Container image scanning
* CI/CD security checks
* Non-root container execution
* Secure AWS IAM configuration

### Container Security

The production container uses an unprivileged application user rather than running the Flask application as root.

The application image also uses a **multi-stage build** to separate the build environment from the runtime environment and reduce the final image footprint.

---

## Technology Stack

| Category                | Technologies                                                  |
| ----------------------- | ------------------------------------------------------------- |
| Operating System        | Linux / Ubuntu                                                |
| Programming             | Python                                                        |
| Web Framework           | Flask                                                         |
| Version Control         | Git / GitHub                                                  |
| Cloud                   | Amazon Web Services                                           |
| Containers              | Docker                                                        |
| Container Registry      | Amazon ECR                                                    |
| Container Orchestration | Amazon ECS / Fargate                                          |
| Infrastructure as Code  | Terraform                                                     |
| CI/CD                   | GitHub Actions                                                |
| Web Technologies        | HTML / CSS / JavaScript                                       |
| Web Server              | Nginx                                                         |
| Security                | GPG, Secret Scanning, Dependency Scanning, Container Scanning |
| Networking              | VPC, Subnets, Security Groups                                 |

---

## AWS Deployment

The application has been deployed using AWS cloud infrastructure.

### AWS Components

```text
AWS
|
+-- VPC
|   |
|   +-- Subnet
|       |
|       +-- ECS/Fargate Task
|             |
|             +-- Flask Application
|
+-- Amazon ECR
|     |
|     +-- scriptsmith-app
|
+-- IAM
      |
      +-- ECS Task Execution Role
```

The deployment process includes:

1. Build the Docker image locally
2. Tag the image for Amazon ECR
3. Push the image to ECR
4. Create/configure an ECS cluster
5. Configure an ECS task definition
6. Configure networking and security groups
7. Launch the Fargate task
8. Verify the application remotely
9. Troubleshoot container and network connectivity

---

## Docker

The application is containerized using Docker.

Example image:

```text
scriptsmith-app:3.3
```

The application has also been optimized using a multi-stage Docker build.

This approach reduces the runtime image size by separating dependency installation from the final runtime environment.

Example workflow:

```bash
docker build -t scriptsmith-app:3.3 .

docker run -p 5000:5000 scriptsmith-app:3.3
```

The image can then be tagged and pushed to Amazon ECR for cloud deployment.

---

## CI/CD

The project is being developed toward an automated CI/CD workflow using GitHub Actions.

The intended pipeline includes:

```text
Git Push
   |
   v
Code Validation
   |
   v
Security Scanning
   |
   v
Docker Build
   |
   v
Container/Image Scanning
   |
   v
Amazon ECR
   |
   v
Amazon ECS
```

The objective is to automate the path from source-code changes to a validated and deployable container.

---

## Infrastructure as Code

I am developing infrastructure automation skills using **Terraform**.

Areas of focus include:

* AWS VPCs
* Subnets
* Route tables
* Internet gateways
* Security groups
* IAM
* EC2
* ECS
* ECR
* Cloud infrastructure automation

The goal is to make infrastructure **repeatable, version-controlled, and reproducible** rather than relying entirely on manual configuration.

---

## Git & Source Control

Git is used throughout the development lifecycle.

Practices include:

* Feature and development workflows
* Meaningful commit messages
* Remote GitHub repositories
* `.gitignore`
* GPG-signed commits
* Version control for infrastructure and application code

Sensitive information such as credentials, private keys, and environment files should never be committed to the repository.

---

## Professional Experience

### Emkan for Engineering and Contracting Services

**Assistant Pipe Fitter Cum Rigger**

Working in an engineering and construction environment supporting pipe fitting, rigging operations, material handling, and workplace safety.

This experience has strengthened my ability to work in safety-critical environments, follow procedures, troubleshoot problems, and work effectively as part of a team.

### City Nights Contracting LLC — Dubai, UAE

**Security Personnel**

Worked in security operations involving access control, monitoring, safety, and maintaining secure working environments.

### Oak Plaza Suites — Asokwa, Ghana

**Security Receptionist**

Worked in a hotel environment combining security responsibilities with reception, visitor management, and customer-facing duties.

### Guinness Ghana Limited — Ahinsan, Ghana

**Warehouse Man**

Worked in warehouse operations involving inventory handling, material movement, storage, and workplace safety.

---

## DevSecOps Learning Journey

### Completed / Practiced

* Linux
* Git
* GitHub
* AWS
* Terraform
* Docker
* Python
* Flask
* CI/CD fundamentals
* AWS networking fundamentals
* IAM
* Amazon ECR
* Amazon ECS
* Container deployment
* Security fundamentals

### Currently Developing

* Advanced CI/CD
* Kubernetes
* Ansible
* Container security
* Cloud security
* Infrastructure automation
* Automated deployment

---

## Portfolio

### Personal Portfolio

**Live Portfolio:**

https://scriptsmithdev.github.io/Felix-DevSecOps-Portfolio/

### GitHub

https://github.com/scriptsmithdev

### Featured Project

**Containerized DevSecOps Application**

https://github.com/scriptsmithdev/scriptsmith-app

---

## Career Objective

I am transitioning from an engineering and construction career into technology, with a specific focus on **DevSecOps and Cloud Engineering**.

My objective is to combine the discipline, safety awareness, problem-solving ability, and operational experience developed throughout my previous career with modern technology skills.

I am particularly interested in opportunities involving:

* DevSecOps
* Cloud Engineering
* AWS
* Cloud Security
* Infrastructure as Code
* CI/CD
* Docker
* Kubernetes
* Automation
* Cybersecurity

I am actively building hands-on projects to demonstrate my ability to learn, troubleshoot, automate, secure, and deploy real-world applications.

---

## Contact

**Felix Amoah**

DevSecOps Engineer in Training

**Email:** scriptsmith.dev@yahoo.com

**GitHub:**
https://github.com/scriptsmithdev

---

## License

This repository is maintained as a personal professional portfolio and learning project.
