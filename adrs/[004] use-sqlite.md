# [004] Use SQLite + SQLAlchemy

## Status - ACTIVE

## Context

For **MadChatter**, we require some way to persist data. For this, a relational database is ideal.
It should be lightweight and have strong python support.

## Decided Approach

We have decided to use SQLite as our database engine, along with SQLalchemy as a Python based ORM
layer.

## Consequences

- Simplified deployment due to a local db.
- Slight increase in cognitive load due to adding ORM abstraction.

