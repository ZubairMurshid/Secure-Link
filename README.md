# Secure-Link — Self-Governing GenAI Document Auditor

**Apr 2026 – Present**  
**Status:** In Progress

Secure-Link is a self-governing GenAI document auditing platform designed to enforce **data privacy** and **compliance** before leveraging large language models (LLMs). The system analyzes uploaded documents (e.g., resumes, contracts), detects and redacts sensitive information, and then generates summaries in a **controlled, observable pipeline**.

Built with an **MLOps-first** mindset, Secure-Link integrates governance, monitoring, and automated deployment practices to enable secure, scalable, and production-ready AI usage.

---

## What Problem This Solves

Organizations often want to use LLMs for summarization and extraction, but must first ensure:
- Sensitive data (PII/PHI/secrets) is **not exposed** to downstream systems or third-party LLM providers
- Processing is **traceable**, **auditable**, and **policy-driven**
- Deployments are consistent, automated, and secure

Secure-Link addresses this by placing a governance and redaction layer *before* any GenAI processing, with observability throughout the pipeline.

---

## Key Features

- **Automated PII detection & redaction**
  - Enforces data governance policies before any LLM processing
  - Detects and redacts sensitive content (e.g., names, emails, phone numbers, IDs)

- **GenAI document summarization pipeline**
  - Summarization occurs only after validation/redaction checks
  - Designed for controlled access and policy-driven execution

- **Containerized microservice architecture**
  - Consistent local + production deployments
  - Scalable service composition using Docker

- **Integrated observability**
  - Tracks model latency, token usage, and governance violations
  - Enables monitoring and accountability for AI usage

- **CI/CD with security and build validation**
  - Automated security scanning
  - Safe releases via build checks and workflow enforcement

- **Optional cloud deployment**
  - Supports real-time access, audit logging, and scalability
  - Target: Azure Container hosting (optional)

---

## Tech Stack

- **Backend:** Python, FastAPI  
- **GenAI / NLP:** Hugging Face Transformers  
- **PII Detection:** Microsoft Presidio  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  
- **Observability:** Prometheus  
- **Optional Cloud Runtime:** Azure Container (optional)

---

## High-Level Workflow

1. **Upload Document**
2. **PII Detection**
3. **Policy Enforcement + Redaction**
4. **Validation Check (only proceed if compliant)**
5. **LLM Summarization**
6. **Observability & Audit Events**
   - latency, token usage, redaction actions, violations, pipeline status

---

## Repository Structure (Suggested / WIP)

> This project is in progress; structure may evolve.

Example structure you may see (or plan to add):

- `app/` — FastAPI application and API routes  
- `services/` — PII detection, redaction, summarization services  
- `models/` — model loading/inference utilities (Transformers)  
- `observability/` — metrics, logging, tracing, dashboards  
- `docker/` — Dockerfiles and container configs  
- `.github/workflows/` — CI/CD pipelines (GitHub Actions)

---

## Getting Started (Local / Docker/ Hugging Face)

Easiest: Navigate to https://zubairmurshid-secure-link-governance-gateway.hf.space/docs#/ to run the hosted Model

> Setup instructions may change as the project evolves.

---

### Prerequisites

* Python 3.10+ (recommended)
* Docker

### Clone the Repository

First, clone the repository from GitHub:

```bash
git clone https://github.com/ZubairMurshid/Secure-Link_Self-Governing_GenAI_Document_Auditor.git
cd presidio-env
```

### Run with Docker (recommended)

1. Build the Docker image:

   ```bash
   docker build -t secure-link .
   ```
2. Run the container:

   ```bash
   docker run -p 8000:8000 secure-link
   ```

### Run Locally (example)

1. Set up a virtual environment:

   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:

   * On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```
   * On Windows:

     ```bash
     .venv\Scripts\activate
     ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Start the application with `uvicorn`:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

---

## Observability (Planned / In Progress)

Secure-Link is designed to expose and track:
- Request latency (per endpoint / pipeline stage)
- Token usage (when applicable)
- Governance violations (policy and redaction events)
- Pipeline pass/fail metrics

Prometheus integration is included in the platform design and may be implemented incrementally.

---

## Security & Governance Notes

Secure-Link is built around the principle:  
**No document should reach the LLM layer until it passes governance checks.**

Planned/typical controls include:
- Redaction rules and allow/deny policies
- Audit logs for sensitive findings and actions
- Optional deployment configurations for stricter environments

---

## Roadmap (High-Level)

- [ ] Finalize end-to-end API workflow (upload → redact → summarize)
- [ ] Add policy configuration and rule management
- [ ] Expand observability coverage (metrics + dashboards)
- [ ] Add audit logging and governance reporting
- [ ] Harden CI/CD with SAST/dependency scanning gates
- [ ] Optional Azure container deployment templates

---

## Contact / Maintainer

**Maintainer:** Zubair Murshid  (https://www.linkedin.com/in/itszubairmurshid/)
