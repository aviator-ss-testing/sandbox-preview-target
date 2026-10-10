# sandbox-preview-target

Target repository for the mergeit sandbox VM's Verify runs. Its `deploy-preview.yml`
workflow only echoes the `workflow_dispatch` inputs it receives.

Run locally: `pip install -r requirements.txt && python app.py`, then open http://localhost:8080/.
