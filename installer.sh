#!/bin/bash
set -e

python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install pre-commit black flake8 cyclonedx-bom pip-audit

# Generate secure .env if missing
if [ ! -f .env ]; then
  echo "No .env file detected. Generating a secure one..."
  python3 scripts/create_secure_env.py
fi

cyclonedx-py -o sbom.json
pip-audit || echo "pip audit completed with warnings."
python3 -c 'import platform, json, pkg_resources; json.dump({"python_version": platform.python_version(),"platform": platform.platform(),"installed_packages":{d.project_name:d.version for d in pkg_resources.working_set}}, open("build-metadata.json", "w"), indent=4)'
pre-commit install

echo "Setup complete."
