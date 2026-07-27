# Development Guide

## Environment

Create virtual environment:

python3 -m venv .venv

Activate:

source .venv/bin/activate

Install:

python -m pip install -e .

Run tests:

pytest -q

## Project Structure

src/
    innovation_os/

tests/

docs/

## Development Workflow

1. Create change
2. Add tests
3. Run pytest
4. Commit changes
