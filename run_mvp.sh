#!/bin/bash
set -e

echo "Running Innovation OS MVP"

pytest

echo ""
echo "Launching demonstration"

python3 demos/run_innovation_demo.py
