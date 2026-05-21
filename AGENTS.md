# PySastrawi Demo — Agent Notes

## What this is
Gradio web app demonstrating PySastrawi (Indonesian language stemmer). Deployed on Hugging Face Spaces.

## Run locally
```bash
pip install -r requirements.txt
python app.py
```
Server starts at `http://127.0.0.1:7860` (Gradio default).

## Deploy
Push to a Hugging Face Space with Gradio SDK:
1. Create Space at huggingface.co/new-space (SDK: Gradio)
2. Connect GitHub repo or upload files
3. Auto-deploys on push to main branch

## Architecture
- `app.py` — single Gradio Blocks app with stemming function and UI
- `requirements.txt` — PySastrawi + gradio dependencies

## Key constraint
Requires Hugging Face account for deployment. Free CPU tier is sufficient.
