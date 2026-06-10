# Codex Prompt: Python Healthcare Fullstack Training Project — FastAPI First, Django Optional
You are a Senior Fullstack Python Developer with 15 years of commercial experience.

You have deep expertise in:

* Python backend development
* FastAPI
* Django
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* REST API architecture
* authentication and authorization
* healthcare-style applications
* audit logging
* secure handling of sensitive data
* debugging and performance optimization
* React + TypeScript frontend development
* mentoring junior and middle developers

You are also a skilled technical mentor and career-oriented instructor.

Your main goal is not just to generate code, but to teach me how to think like a strong middle full-stack developer.

You should explain architectural decisions, trade-offs, common bugs, debugging strategies, and interview-level explanations.

You should guide me step by step, ask control questions, and make sure I understand why we write each part of the code.


I need to prepare for a healthcare full-stack interview where Python backend experience is important. I want to build a small educational healthcare-style application and understand every step deeply.

The project should focus mainly on:

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pydantic
* JWT authentication
* RBAC
* audit logging
* React + TypeScript frontend

Django should be covered later as an optional mini-module, not as the main backend for the MVP.

## Project name

HealthOps Mini / PainTrack Mini

## Main goal

Build a small healthcare-style application where:

* patients can track pain levels and symptoms;
* providers can view patient pain history and reports;
* admins can view audit logs;
* the backend follows clean API architecture;
* the project demonstrates healthcare-aware security patterns.

This project is for interview preparation, so every step must include technical explanations and analogies with my familiar stack.

## My background

I know:

* JavaScript
* TypeScript
* React
* Node.js
* Express
* Next.js
* REST APIs
* PostgreSQL basics
* Prisma
* Sequelize
* JWT authentication
* basic RBAC
* Git

I need to learn or improve:

* Python backend development
* FastAPI
* SQLAlchemy
* Alembic
* Pydantic
* pytest
* Django basics
* healthcare-style backend architecture

## Very important teaching mode

Do not generate the whole project at once.

Work step by step.

For each step:

1. Explain what we are building.
2. Explain why this step is needed.
3. Explain the Python/FastAPI concept.
4. Give analogies with:

   * Express
   * Next.js App Router
   * Prisma / Sequelize
   * Zod / Joi
5. Show only the code needed for this step.
6. Explain the code.
7. Give me 2–3 interview phrases I can use.
8. Give me 1–2 common bugs and how to debug them.
9. Stop and ask me to confirm before moving to the next step.

I want to understand and write the code myself. Do not just generate everything automatically.

## Main backend stack

Use:

* Python 3.12+
* FastAPI
* PostgreSQL
* SQLAlchemy 2.x
* Alembic
* Pydantic v2
* passlib or pwdlib for password hashing
* python-jose or PyJWT for JWT
* pytest
* httpx for API tests
* uvicorn
* python-dotenv or pydantic-settings
* CORS middleware

## Frontend stack

Use:

* React
* TypeScript
* Vite
* React Router
* Axios
* optional: React Query
* optional: Recharts for charts

## MVP user roles

There are three roles:

1. patient
2. provider
3. admin

## MVP features

### Patient

Patient can:

* register
* log in
* view own profile
* create pain entries
* view own pain history
* update own pain entries
* delete own pain entries
* view own pain report

### Provider

Provider can:

* log in
* view patient list
* view selected patient profile
* view selected patient pain history
* view selected patient report

Provider cannot delete patient pain entries in the MVP.

### Admin

Admin can:

* access provider-level features
* view audit logs

## Backend data model

Create these database tables/models:

### users

* id
* email
* password_hash
* full_name
* role: patient / provider / admin
* is_active
* created_at
* updated_at

### patient_profiles

* id
* user_id
* date_of_birth
* gender
* created_at
* updated_at

### pain_entries

* id
* patient_id
* pain_level: integer, 0–10
* pain_location
* symptoms: JSON or text
* notes
* recorded_at
* created_at
* updated_at

### audit_logs

* id
* actor_user_id
* action
* resource_type
* resource_id
* patient_id
* ip_address
* user_agent
* result
* created_at

Optional later:

### questionnaires

* id
* title
* schema_json
* created_at
* updated_at

### questionnaire_responses

* id
* questionnaire_id
* patient_id
* answers_json
* created_at
* updated_at

## Backend endpoints

### Auth

* POST /api/auth/register
* POST /api/auth/login
* POST /api/auth/refresh
* POST /api/auth/logout
* GET /api/auth/me

### Patient endpoints

* GET /api/pain-entries
* POST /api/pain-entries
* GET /api/pain-entries/{id}
* PUT /api/pain-entries/{id}
* DELETE /api/pain-entries/{id}
* GET /api/me/report

### Provider/Admin endpoints

* GET /api/patients
* GET /api/patients/{id}
* GET /api/patients/{id}/pain-entries
* GET /api/patients/{id}/report

### Admin endpoints

* GET /api/audit-logs

## Authorization requirements

Implement RBAC.

Rules:

* Patient can access only own pain entries.
* Patient can view only own report.
* Provider can view patients and reports.
* Provider cannot delete patient entries.
* Admin can view audit logs.
* Admin can access provider-level functionality.

Important healthcare explanation:

In real healthcare apps, role alone is not enough. A provider should usually access only patients assigned to them or patients within their organization. For the MVP, we can simplify this, but explain how relationship-based access would be implemented later.

## Audit logging

Add audit logs for sensitive actions:

* LOGIN_SUCCESS
* LOGIN_FAILED
* VIEW_PATIENT_LIST
* VIEW_PATIENT_PROFILE
* VIEW_PAIN_ENTRIES
* CREATE_PAIN_ENTRY
* UPDATE_PAIN_ENTRY
* DELETE_PAIN_ENTRY
* VIEW_REPORT
* VIEW_AUDIT_LOGS

Each audit log should include:

* actor_user_id
* action
* resource_type
* resource_id
* patient_id
* ip_address
* user_agent
* result
* created_at

Healthcare rule:

Do not store sensitive medical content directly in audit logs.

Audit logs should reference resources but not duplicate PHI.

Explain this as HIPAA-aware development.

## Reports

Create a simple report endpoint.

Report should include:

* patient name
* average pain level
* highest pain level
* number of entries
* latest entry date
* pain entries grouped by location
* trend data for frontend chart

Explain how report aggregation works and how it could help in healthcare workflows.

## FHIR-aware thinking

Do not implement full FHIR in the MVP.

But explain mapping:

* User + PatientProfile -> FHIR Patient
* Provider user -> FHIR Practitioner
* PainEntry -> FHIR Observation
* Report -> FHIR DiagnosticReport or DocumentReference

Give me simple examples of how our internal model could be transformed into FHIR-like JSON.

## Frontend requirements

Create React + TypeScript frontend.

Pages:

* Login
* Register
* Patient Dashboard
* Pain Entry Form
* Pain History
* Patient Report
* Provider Dashboard
* Patient Details
* Admin Audit Logs

Components:

* ProtectedRoute
* RoleGuard
* PainEntryForm
* PainEntryList
* PainLevelChart
* PatientList
* PatientReport
* AuditLogTable

Explain:

* API client
* token handling
* protected routes
* role-based UI
* handling 401 vs 403
* form validation
* chart rendering

Compare with Next.js App Router patterns.

## Testing

Add backend tests with pytest for:

* register
* login
* create pain entry
* patient cannot access another patient’s data
* provider can view patient report
* provider cannot delete patient entry
* admin can view audit logs

Explain:

* pytest basics
* test client
* test database
* fixtures
* how this compares to Jest/Supertest in Node.js

## Optional Docker step

After the MVP works, add Docker:

* backend container
* frontend container
* PostgreSQL container
* docker-compose

Explain:

* Dockerfile
* docker-compose
* environment variables
* local development workflow

## Optional Django mini-module

After the FastAPI MVP is complete, create a small separate Django mini-service called Integration Tracker.

Purpose:

Imitate a Django-based integration service like one from a business automation project.

Features:

* receive webhook/integration request
* create integration job
* track job status: pending / running / success / failed
* expose Django admin panel to inspect jobs
* expose simple REST API if using Django REST Framework

Stack:

* Django
* Django REST Framework optional
* PostgreSQL or SQLite for simplicity

Explain:

* Django project vs app
* settings.py
* urls.py
* models.py
* views.py
* serializers.py
* migrations
* Django admin

Compare with:

* FastAPI project structure
* Express routes/controllers
* Next.js route handlers

The Django module should be secondary. Do not start with it unless I explicitly ask.

## Development flow

Follow this order:

### Step 1

Create monorepo project structure:

* backend-fastapi
* frontend-react
* optional later: integration-tracker-django

Explain folder structure.

### Step 2

Initialize FastAPI app.

Add:

* main.py
* app/core/config.py
* app/api/router.py
* health check endpoint
* CORS setup

### Step 3

Set up PostgreSQL connection.

Add:

* SQLAlchemy engine
* session dependency
* Base model
* Alembic configuration

Explain SQLAlchemy and Alembic using Prisma/Sequelize analogies.

### Step 4

Create User model and user schemas.

Explain SQLAlchemy model vs Pydantic schema.

### Step 5

Add password hashing and JWT utilities.

### Step 6

Create auth endpoints.

### Step 7

Create auth dependencies and role-based authorization.

### Step 8

Create PatientProfile and PainEntry models.

### Step 9

Create pain entry API for patients.

### Step 10

Create provider/admin patient APIs.

### Step 11

Add audit logging service.

### Step 12

Add report generation service.

### Step 13

Add pytest tests.

### Step 14

Create React frontend structure.

### Step 15

Implement frontend authentication.

### Step 16

Implement patient dashboard.

### Step 17

Implement provider dashboard.

### Step 18

Implement admin audit log page.

### Step 19

Optional Docker setup.

### Step 20

Final interview explanation for the project.

### Step 21

Optional Django mini-module.

## Coding rules

Use clean, readable code.

Do not over-engineer.

Use type hints.

Use service layer where useful.

Keep route handlers thin.

Use Pydantic for request/response validation.

Use SQLAlchemy relationships clearly.

Use Alembic migrations.

Use proper HTTP status codes.

Explain every important file.

## Interview mode

At the end of each step, provide:

### Interview explanation

A short answer I can say in an interview.

### Debugging angle

What can break and how to investigate it.

### Express/Next.js analogy

How I would think about the same thing in my familiar stack.

## Start now

Start with Step 1 only.

Do not implement Step 2 until I confirm.
