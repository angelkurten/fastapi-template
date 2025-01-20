# My Service #

## About

FastAPI template for serious projects. This template is designed to be a starting point for building robust, scalable,
and maintainable applications with FastAPI. It includes a set of best practices, tools, and libraries to help you get
started quickly. Also provides a complex example of how to structure your application using Domain-Driven Design (DDD),
Clean Architecture, and Hexagonal Architecture principles with FastAPI.

## Source Code Structure and Architectural Justification

This repository’s structure aligns with established architectural principles
from Domain-Driven Design (DDD), Clean Architecture, and Hexagonal Architecture.
The aim is to keep core business logic independent of external frameworks,
infrastructure details, and technology-specific concerns. This approach ensures
long-term maintainability, flexibility, and testability.

### High-Level Directory Layout Example

```text

src/
├─ app/
│  ├─ application.py
│  └─ container.py
│
├─ config/
│  └─ app.py
│
└─ module/
   ├─ common/
   │
   └─ <my-example-module>/
      ├─ application/
      │  ├─ http/
      │  │  ├─ __init__.py
      │  │  ├─ router.py
      │  │  └─ <my_http_controller>.py
      │  ├─ service/
      │  │  ├─ __init__.py
      │  │  └─ <my_service>.py
      │  └─ use_case/
      │     ├─ __init__.py
      │     └─ <my_use_case>>.py
      │
      ├─ domain/
      │  ├─ user/
      │  │  ├─ __init__.py
      │  │  ├─ password_rules.py -> contains a set of rules
      │  │  ├─ repository.py -> contains UserRepository contract
      │  │  ├─ user.py -> contains the entity
      │  │  └─ values.py -> used values for the domain
      │  └─ __init__.py
      │
      ├─ infrastructure/
      │  ├─ repository/
      │  │  ├─ in_memory/
      │  │  │  ├─ __init__.py
      │  │  │  └─ user_repository.py
      │  │
      │  └─ service/
      │     ├─ email_notifier/
      │     │  ├─ __init__.py
      │     │  ├─ contract.py
      │     │  └─ mailchimp_email_notifier.py
      │
      ├─ container.py
      ├─ providers.py
      └─ __init__.py

```

### Layered Architecture

**Domain Layer:**
Contains core entities, value objects, and domain services, free of external
dependencies. DDD encourages a pure domain model using a ubiquitous language
that reflects real business concepts. By isolating the domain layer, we ensure
that evolving business rules remain unaffected by technical details.

**Application Layer:**
Implements application-specific workflows (use cases) that orchestrate domain
logic. It adapts external requests (e.g., HTTP calls) into domain operations,
while not introducing domain rules itself. This layer coordinates interaction
between the domain and infrastructure, maintaining clear boundaries.

**Infrastructure Layer:**
Provides technical capabilities, implementing interfaces defined in the domain
and application layers. Repositories, external services, and other adapters
reside here. This separation allows infrastructure details to change without
affecting the core business logic.

### DDD, Clean Architecture, and Hexagonal Principles

**From DDD (Eric Evans):**
DDD focuses on a rich domain model that evolves with business requirements. By
keeping domain logic pure, we can refine and adjust it as concepts become clearer
or shift, without entangling infrastructure concerns.

**From Clean Architecture (Robert C. Martin):**
The Dependency Rule states dependencies should point inward. Domain and
application layers remain stable and framework-agnostic, while external details
depend on them. This ensures that changes to frameworks or databases do not
ripple through the entire codebase.

**From Hexagonal Architecture (Ports and Adapters):**
The system core defines ports (interfaces), while adapters (infrastructure
implementations) plug in without altering the domain model. External changes,
like replacing an email provider, do not affect the domain logic.

### Preserving Dependency Scope and Contracts

By enforcing these architectural patterns, we maintain a stable, testable core:

- **Stable Core:**
  The domain model remains intact and testable in isolation.

- **Flexible Infrastructure:**
  Changes in databases, APIs, or services happen in the infrastructure layer,
  sparing the domain and application layers from refactoring.

- **Clear Contracts:**
  Interfaces ensure consistent interactions. Mocks and in-memory repositories
  simplify testing and accelerate iteration.

- **Conceptual Clarity:**
  Developers know where to place code. The domain layer holds business logic,
  the application layer orchestrates, and the infrastructure layer adapts
  technical details.

## Set Up

### Requirements

- Docker or any OCI Container compatible implementation
- Python 3+ (check the .python-version file to get the current version)
  - We recommend to manage the python versions with py-env
- Poetry (it's possible to use without be installed on the OS, but is a little trickier)

### Install the correct python version
- (Recommend) Using PyEnv: `pyenv install`
- Using Nix

### Init the project and install the scripts
- (Recommend) Using make: `make install`
- Running manually the commands (check the make `install` target for the current steps)
  - Install the project with poetry: `poetry install`
  - Install pre-commit scripts: `poetry run pre-commit install`

## Run tests

> Run all tests and coverage: `make test`

We use pytest as testing platform.
The tests are differentiated by the typology. Currently, we have two:

- Integration
- Unitary
