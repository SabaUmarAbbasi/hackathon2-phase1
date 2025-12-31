<!--
# Sync Impact Report
- Version change: null → 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → I. Mandatory Spec-Driven Development
  - [PRINCIPLE_2_NAME] → II. Agent Behavior Rules
  - [PRINCIPLE_3_NAME] → III. Phase Governance (Scope Lock)
  - [PRINCIPLE_4_NAME] → IV. Technology constraints
  - [PRINCIPLE_5_NAME] → V. Structure & Organization
  - [PRINCIPLE_6_NAME] → VI. Quality Principles
- Added sections: Phase I Governance, Success Definition
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md (Logic alignment)
  - ✅ .specify/templates/spec-template.md (Logic alignment)
  - ✅ .specify/templates/tasks-template.md (Logic alignment)
- Follow-up TODOs: None
-->
# the-todo-app Constitution

## Core Principles

### I. Mandatory Spec-Driven Development
Spec-driven development is non-negotiable. All work MUST follow this exact order: Constitution → Specs → Plan → Tasks → Implement.
- No agent may write code without an approved specification.
- No implementation may begin without an approved plan and task breakdown.
- Refinement and changes must occur at the spec level, never directly in code.
- Specs are the single source of truth.

### II. Agent Behavior Rules
All agents (Claude Code or otherwise) MUST obey:
- NO manual coding by humans.
- NO feature invention or assumptions beyond written specs.
- NO deviation from approved requirements.
- NO future-phase features allowed in Phase I.
- All outputs must be traceable to specs.
- Any ambiguity must be resolved by updating specs, not code.

### III. Phase Governance (Scope Lock)
Phase I includes ONLY: In-memory task storage, Command-line interface, and Basic CRUD (Add, View, Update, Delete, Toggle Complete).
- Phase I must remain simple and synchronous.
- NO persistence (no files, no database), NO async, NO API, NO UI, NO networking.
- Future phases MUST NOT leak into Phase I.

### IV. Technology Constraints
- **Required Stack**: Python 3.13+, UV for environment and dependency management.
- **Explicitly Disallowed**: Databases, File storage, Web frameworks, Frontend frameworks, External APIs.

### V. Project Structure Rules
The repository MUST maintain:
- `/specs/`: Constitution and specification history.
- `/src/`: Python source code only.
- `README.md`: Setup and usage instructions.
- `CLAUDE.md`: Claude Code execution rules.

### VI. Quality Principles
All generated code MUST follow:
- Clean architecture and clear separation of concerns.
- Readable and maintainable Python code with meaningful naming.
- Deterministic behavior and proper error handling.
- CLI-friendly user experience.

## Governance

### Amendment Procedure
This constitution remains stable throughout Phase I. It overrides all other documents and can only be changed through an explicit constitution revision.

### Success Definition (Phase I)
Phase I is successful ONLY IF:
- All 5 basic features work correctly (Add, View, Update, Delete, Toggle).
- The application runs entirely in memory with CLI output reflecting status correctly.
- All work follows the mandatory SDD flow.
- No manual coding was performed.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
