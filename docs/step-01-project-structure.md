# Step 1: Project Structure

## What we are building

We are creating the top-level structure for **PainTrack Mini**:

- `backend/` - Laravel REST API for authentication, pain entries, reports, and
  audit logs.
- `frontend/` - React + TypeScript Vite app for patients and providers.
- `docs/` - learning notes and project prompts.

## Why this step matters

Separating backend and frontend makes the data flow easier to explain:

1. React renders pages and forms in the browser.
2. React calls Laravel API endpoints over HTTP.
3. Laravel validates requests, checks auth/roles, talks to MySQL, and returns
   JSON.

This mirrors a common full-stack interview architecture: one API service and one
client application.

## Laravel view

In Laravel, the backend will eventually contain:

- routes in `routes/api.php`
- controllers in `app/Http/Controllers`
- models in `app/Models`
- migrations in `database/migrations`
- middleware and policies for authentication and authorization

## Analogy with your stack

- Laravel routes are like Express routes or Next.js route handlers.
- Laravel controllers are like Express controller functions.
- Eloquent models are closest to Sequelize models, and conceptually similar to
  Prisma models plus query methods.
- Laravel migrations serve the same purpose as Prisma or Sequelize migrations:
  they version database schema changes.
- Laravel request validation is similar to validating request bodies with Zod or
  Joi before running business logic.

## Commands used in this step

The frontend was generated with:

```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
```

The backend could not be generated yet because PHP and Composer are not
available in the current terminal PATH. Once installed, generate Laravel with:

```bash
composer create-project laravel/laravel backend
```

## Current folder map

```text
ManagingLife/
  backend/
    README.md
  docs/
    description.md
    step-01-project-structure.md
  frontend/
    src/
    public/
    package.json
    vite.config.ts
```

## Interview explanation

For Step 1, you can say:

"I split the project into a Laravel backend and a React TypeScript frontend. The
frontend is responsible for user interaction and API calls, while Laravel owns
authentication, authorization, validation, database access, audit logging, and
healthcare-sensitive data rules. This separation makes the system easier to
reason about and matches a typical REST API architecture."

