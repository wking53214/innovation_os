# Innovation OS

[![Innovation OS Tests](https://github.com/wking53214/innovation_os/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/wking53214/innovation_os/actions/workflows/tests.yml)

## Governed Innovation Operating System

Innovation OS is a framework for capturing, connecting, evaluating, and developing ideas.

## Traceability Model

Problem
↓
Idea
↓
Decision
↓
Branch
↓
Review
↓
Solution
↓
Approval
↓
Implementation

## MVP Capabilities

- Problem Management
- Ideation Engine
- Problem Alignment
- Review Engine
- Branch Engine
- Decision Replay
- Code Registry
- Solution Engine
- Forecast Engine
- Nature Inspired Engine
- Human Approval Governance

## Setup

python3 -m venv .venv

source .venv/bin/activate

pip install -e ".[dev]"

## Running Tests

pytest

## Running Demo

python3 -m demos.run_innovation_demo

## Running MVP 2.0 Demo

python3 -m demos.mvp2_demo

## CLI

python3 -m innovation_os.cli.main status

python3 -m innovation_os.ingest <folder>
