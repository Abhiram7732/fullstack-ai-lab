# Fullstack AI Lab

*A hands-on exploration of full-stack AI application development.*

An experimental project exploring how modern web technologies, AI services, authentication, subscription billing, and cloud deployment work together to build a full-stack application.

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-Pages%20Router-black?logo=next.js" alt="Next.js" />
  <img src="https://img.shields.io/badge/React-UI-61DAFB?logo=react&logoColor=black" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-Development-3178C6?logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Python-Backend-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Clerk-Authentication-6C47FF?logo=clerk&logoColor=white" alt="Clerk" />
  <img src="https://img.shields.io/badge/Vercel-Deployment-black?logo=vercel" alt="Vercel" />
</p>

---

## Overview

The goal of this project is to explore how individual technologies connect to form a working application, from frontend development and backend APIs to authentication, AI integration, and deployment.

Rather than being a finished commercial product, this repository documents a hands-on learning process involving implementation, customization, debugging, and experimentation.

## Application Preview

<!-- Add your actual application screenshot at docs/images/homepage.png -->
<img width="1772" height="852" alt="image" src="https://github.com/user-attachments/assets/57658288-ce8c-43e0-ba8b-39681aa7661f" />

<img width="1652" height="853" alt="image" src="https://github.com/user-attachments/assets/32fe05f4-ffb8-463d-8a1e-80b7bf57da28" />
<img width="882" height="813" alt="Screenshot 2026-11-02 122643" src="https://github.com/user-attachments/assets/fd5e04e8-626d-4324-be73-567c17e58dbe" />
<img width="1607" height="828" alt="Untitled Design" src="https://github.com/user-attachments/assets/706c8421-3dc7-463a-80b5-a8215aa5dcae" />


<p align="center">
Manage Profiles , Billing , Subscriptions, Access Features
</p>


---

## Architecture Overview

The application explores communication between a web frontend, a Python backend, hosted AI services, and authentication infrastructure.

```mermaid
flowchart TD
    U([User]) --> FE["Next.js Frontend"]
    FE --> AUTH["Clerk Authentication"]
    FE --> API["FastAPI Backend"]
    API --> JWT["JWT Verification"]
    JWT --> AI["Hosted AI API"]
    AI --> STREAM["Streaming Response"]
    STREAM --> FE
    AUTH --> BILL["Subscription Billing"]
    FE --> V["Vercel Deployment"]

    style FE fill:#2563eb,color:#ffffff,stroke:#1d4ed8
    style API fill:#009688,color:#ffffff,stroke:#00796b
    style AUTH fill:#6d28d9,color:#ffffff,stroke:#5b21b6
    style AI fill:#475569,color:#ffffff,stroke:#334155
    style V fill:#111827,color:#ffffff,stroke:#374151
```

*Conceptual architecture illustrating the integrations being explored. The actual request and authorization flow depends on the implementation.*

## Technology Stack

| Area | Technologies |
|---|---|
| Frontend | Next.js, React, TypeScript |
| Styling | Tailwind CSS |
| Backend | Python, FastAPI |
| AI Integration | Hosted AI APIs |
| Authentication | Clerk |
| Subscription Billing | Clerk Billing |
| Streaming | Server-Sent Events (SSE) |
| Deployment | Vercel |
| Version Control | Git, GitHub |

---

## API Integration & Streaming

Exploring how the frontend communicates with a backend API, how requests reach an external AI service, and how generated content can be delivered progressively.

```mermaid
sequenceDiagram
    actor User
    participant UI as Next.js Frontend
    participant API as FastAPI Backend
    participant AI as Hosted AI API

    User->>UI: Submit input
    UI->>API: HTTP request
    API->>AI: Forward request
    AI-->>API: Generated content
    API-->>UI: Stream response using SSE
    UI-->>User: Display content progressively
```

**Concepts explored**
- HTTP requests and responses
- Frontend-to-backend communication
- External API integration
- Environment variables and API credentials
- Server-Sent Events (SSE)
- Streaming and error handling

<!-- Optional: add an actual screenshot of the AI interface below -->

<!--
<p align="center">
  <img src="docs/images/ai-interface.png" alt="AI interface" width="85%" />
</p>
-->

---

## Authentication & Authorization

Exploring how authentication providers manage user sessions and how protected backend endpoints can verify a user's identity.

```mermaid
flowchart TD
    A["User opens application"] --> B["Sign in through Clerk"]
    B --> C["Authenticated session"]
    C --> D["Frontend sends protected request"]
    D --> E["Backend validates token"]
    E --> F{"Token valid?"}
    F -->|Yes| G["Continue authorized operation"]
    F -->|No| H["Reject request"]

    style B fill:#6d28d9,color:#ffffff
    style G fill:#15803d,color:#ffffff
    style H fill:#b91c1c,color:#ffffff
```

**Concepts explored**
- User authentication and sessions
- JSON Web Tokens (JWTs)
- Backend token verification
- Protected routes and access control

Reference: [Clerk Documentation](https://clerk.com/docs)

<!-- Optional: add your actual sign-in or account screenshot -->

<!--
<p align="center">
  <img src="docs/images/authentication.png" alt="Authentication interface" width="85%" />
</p>
-->

---

## Subscription Billing

Exploring subscription-based application features and how billing can relate to user access.

Areas of interest include:
- Subscription plans
- Billing integration
- Access control for different plans
- Connecting authenticated users with subscription-related features

Reference: [Clerk Billing Documentation](https://clerk.com/docs)

*The billing section describes the concepts being explored; individual features may still be in progress.*

---

## Deployment & Development Workflow

Exploring the journey from local development to a hosted application using Git, GitHub, and Vercel.

```mermaid
flowchart LR
    A["Local Development"] --> B["Git Commit"]
    B --> C["GitHub Repository"]
    C --> D["Vercel Deployment"]
    D --> E["Preview & Testing"]
    E --> F["Production Deployment"]

    style A fill:#475569,color:#ffffff
    style C fill:#24292f,color:#ffffff
    style D fill:#2563eb,color:#ffffff
    style F fill:#15803d,color:#ffffff
```

**Concepts explored**
- Git and GitHub workflows
- Deployment configuration
- Environment variable management
- Build errors and debugging
- Deployment logs
- Preview and production environments

Reference: [Vercel Deployment Documentation](https://vercel.com/docs/deployments)

---


<!-- Optional: replace with an actual screenshot of your customized UI -->

<!--
<p align="center">
  <img src="docs/images/custom-ui.png" alt="Customized application UI" width="85%" />
</p>
-->


## What I'm Learning

- Building interfaces with Next.js, React, and TypeScript.
- Developing backend endpoints using Python and FastAPI.
- Integrating external APIs into web applications.
- Understanding HTTP communication and streaming responses.
- Exploring authentication and JWT verification.
- Learning about subscription billing and access control.
- Deploying applications and troubleshooting deployment issues.
- Managing environment variables and source control.

## Project Status

**In progress — experimental learning project.**

This repository documents ongoing exploration and implementation. Some features or integrations may be incomplete, and the application is not presented as a production-ready SaaS product.


## Learning Goal

To develop practical experience connecting frontend and backend technologies, integrating AI services, exploring authentication and billing, and deploying a full-stack application.

---

<p align="center">
  <em>Learn by building. Experiment, debug, and improve.</em>
</p>
