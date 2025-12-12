#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="${PROJECT_ROOT}:${PROJECT_ROOT}/chatmate_src:${PYTHONPATH:-}"

cd "${PROJECT_ROOT}"

poetry run pytest chatmate_test/tests/base
