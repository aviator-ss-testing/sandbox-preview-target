#!/usr/bin/env bash
set -euo pipefail
pip install -r requirements.txt
nohup python app.py >/tmp/app.log 2>&1 &
