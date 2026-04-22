# QA Automation Pipeline (Selenium + Docker + Terraform + CI/CD)

## Project Overview

This project demonstrates an end-to-end **UI Automation Testing pipeline** designed using modern **QA + SRE practices**.

The framework automates UI tests using **Selenium + Pytest**, packages the tests into a **Docker container**, runs them through **GitHub Actions CI/CD**, and stores the generated **HTML test reports in a private AWS S3 bucket configured via Terraform**.

The architecture mimics a real-world automation environment used by QA and SRE teams where tests run automatically on every code change.

---

# Architecture
Developer Push -> GitHub Actions CI/CD -> Docker Build -> Pytest (Dynamic Data Discovery) -> Dual Reporting (S3 + GH Artifacts)

---

# Tech Stack

| Technology | Purpose |
|--------|--------|
| Python | Test framework |
| Selenium | UI automation |
| Pytest | Test runner |
| pytest-html | HTML reporting |
| Docker | Containerized test execution |
| GitHub Actions | CI/CD pipeline |
| Terraform | Infrastructure as Code |
| AWS S3 | Test report storage |

---

# Test Framework Design

The framework follows the **Page Object Model (POM)** design pattern.

### BasePage

Contains reusable Selenium methods:

- click
- type
- select
- wait_for_page
- get_text
- get_text_of_all_elements

This avoids duplication and improves maintainability.

---

### Page Classes

Each application page is modeled as a class:

| Page | Responsibility |
|-----|-----|
| LoginPage | Handles login functionality |
| AccountServices | Navigation between banking services |
| AccountsOverview | Retrieves account details |
| OpenNewAccount | Handles new account creation |

---

### Test Layer

Tests interact only with page objects.

Example test scenario:

Login to application
Open new bank account
Return to accounts overview
Validate account list and balances

### Self-Healing & Dynamic Data

To ensure test resilience against demo-environment resets (e.g., ParaBank database wipes), the framework implements Runtime Data Discovery. Instead of hardcoding Account IDs, the tests dynamically fetch active IDs from the UI during execution, significantly reducing flakiness and maintenance.

---

# Configuration

Configuration is stored in `config.json`.

Example:

{
"BROWSER": "chrome",
"BASE_URL": "https://parabank.parasoft.com/
",
"CREDENTIALS": {
"username": "john",
"password": "demo"
},
"ACCOUNT_TYPE": "CHECKING"
}


---

# Running Tests Locally

Install dependencies:
pip install -r requirements.txt

Run tests:
pytest --html=report.html --self-contained-html

---

# Running Tests Using Docker

Build Docker image:
docker build -f docker/Dockerfile -t ui-tests .


Run tests:
docker run --rm -v $(pwd)/reports:/app/reports ui-tests

The test report will be generated inside:
reports/report.html

---

# CI/CD Pipeline

The project includes a **GitHub Actions workflow** that automatically runs tests on every push.

**Pre-requisite:**
Provision the AWS S3 bucket using the provided **Terraform** configuration to enable automated report uploading. 

**Pipeline steps:**

1. Checkout repository
2. Build Docker image
3. Run UI tests inside container
4. Generate HTML test report
5. Upload report to AWS S3
6. Store report as GitHub artifact

Workflow file:
.github/workflows/automated-tests.yml

---

# Infrastructure as Code (Terraform)

Terraform provisions the AWS infrastructure required to store test reports.

Resources created:

- AWS S3 bucket
- Bucket versioning
- Server-side encryption
- Public access block
- Lifecycle rules for automatic cleanup

Example resource:
aws_s3_bucket


Bucket configuration includes:
- Versioning enabled
- AES256 encryption
- Public access disabled
- Lifecycle rule to delete old reports

---

# Test Report Storage

All reports are uploaded to a **private AWS S3 bucket**:
qa-automation-logs-afsah


The bucket is **not publicly accessible** for security reasons.
Reports are stored using the format:
report-<github-run-id>.html

Example:
report-24738275682.html

---

# Accessing Reports via Pre-Signed URL

Since the S3 bucket is private, reports can be accessed using AWS Console or a **pre-signed URL** for secure sharing.

Generate a temporary link using AWS CLI:
aws s3 presign s3://<bucket-name>/report-<github-run-id>.html --expires-in 604800 --region us-east-1

This generates a secure URL valid for **7 days**.

---

# Key Features

- Page Object Model architecture
- Headless browser execution
- Dockerized test execution
- GitHub Actions CI pipeline
- Terraform Infrastructure as Code
- Secure S3 report storage
- Pre-signed report access

---

# Why This Project Matters

This project demonstrates skills across **QA Automation and SRE practices**, including:

- Test framework design
- Containerized automation
- CI/CD pipeline development
- Infrastructure as Code
- Cloud artifact storage

These capabilities reflect real-world automation environments used in modern QA and DevOps teams.

**Observability & Error Handling:** 
Implemented if: always() logic in CI/CD to ensure test artifacts are captured even during execution failures, facilitating faster debugging and "Mean Time to Repair" (MTTR).

---