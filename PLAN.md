# Plan: PySastrawi Web Demo (HF Spaces + Gradio)

## Goal
Deploy a single-page web app that accepts Indonesian text input and returns stemmed output, using PySastrawi, with zero infra cost and minimal effort.

## Platform
**Hugging Face Spaces + Gradio** — free, no credit card, built for Python demos, git push deploy, always-on.

## Project Structure

```
pysastrawi-demo/
├── app.py              # Gradio UI + stemming logic
├── requirements.txt    # PySastrawi + gradio
├── README.md           # How to use
└── .gitignore
```

## API Reference (from PySastrawi README)

```python
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Single call handles whole sentence
output = stemmer.stem("Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan")
# → "ekonomi indonesia sedang dalam tumbuh yang bangga"
```

## Implementation Steps

### Step 1 — Scaffold `app.py`

```python
import gradio as gr
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Lazy-init stemmer (loaded once at import time)
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stem_indonesian(text):
    """Process input text and return stemmed version."""
    if not text.strip():
        return ""
    return stemmer.stem(text)

with gr.Blocks(
    title="PySastrawi Demo",
    theme=gr.themes.Soft(),
) as demo:
    gr.Markdown("# 🇮🇩 PySastrawi — Stemmer Bahasa Indonesia")
    gr.Markdown(
        "Masukkan teks bahasa Indonesia, dapatkan kata dasar masing-masing kata."
    )

    with gr.Row():
        input_text = gr.Textbox(
            label="Input Teks",
            placeholder="Contoh: Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan...",
            lines=8,
        )
        output_text = gr.Textbox(
            label="Hasil Stemming",
            placeholder="Hasil akan muncul di sini...",
            lines=8,
            interactive=False,
        )

    with gr.Row():
        submit_btn = gr.Button("Stemming 🚀", variant="primary", scale=2)
        clear_btn = gr.Button("Hapus", scale=1)

    # Wire up events
    submit_btn.click(
        fn=stem_indonesian,
        inputs=input_text,
        outputs=output_text,
    )
    clear_btn.click(
        fn=lambda: ("", ""),
        inputs=None,
        outputs=[input_text, output_text],
    )

    # Example inputs
    gr.Examples(
        examples=[
            ["Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan"],
            ["Mereka meniru-nirukannya"],
            ["Kebersamaan dan keberhasilan adalah kunci pembangunan"],
            ["Mengekspor barang-barang berkualitas tinggi"],
        ],
        inputs=input_text,
        outputs=output_text,
        fn=stem_indonesian,
    )

# Launch with server config for HF Spaces
if __name__ == "__main__":
    demo.launch()
```

### Step 2 — Write `requirements.txt`

```
PySastrawi>=1.2.1
gradio>=5.0
```

### Step 3 — Write `README.md`

Brief description, screenshot of the UI, link to live demo, and instructions to run locally:

```markdown
# PySastrawi Demo

Web demo for [PySastrawi](https://github.com/har07/PySastrawi) — Indonesian language stemmer.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Deploy

Push to a Hugging Face Space with Gradio SDK, or run locally.
```

### Step 4 — Write `.gitignore`

```
__pycache__/
*.pyc
.env
```

### Step 5 — Create HF Space

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Space name: `pysastrawi-demo`
3. License: `MIT`
4. SDK: `Gradio`
5. Hardware: `CPU basic` (free)
6. Space visibility: `Public`
7. Connect GitHub repo (or upload files directly)

### Step 6 — Deploy

- **If connected to GitHub:** Push to main branch → auto-deploys
- **If uploading directly:** Drag files or use `git push` to HF

### Step 7 — Verify

- Lite demo URL: `https://huggingface.co/spaces/{your-username}/pysastrawi-demo`
- Full URL: `https://{your-username}-pysastrawi-demo.hf.space`

## Optional Enhancement (post-MVP)

- Add a per-word breakdown table (word → stem) so users can see each mapping
- Add character/word counters
- Dark mode toggle (Gradio has built-in theme support)
