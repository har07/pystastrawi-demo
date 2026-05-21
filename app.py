import gradio as gr
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def stem_indonesian(text):
    if not text.strip():
        return ""
    return stemmer.stem(text)


with gr.Blocks(
    title="PySastrawi Demo",
    theme=gr.themes.Soft(),
) as demo:
    gr.Markdown("# 🇮🇩 PySastrawi — Stemmer Bahasa Indonesia")
    gr.Markdown("Masukkan teks bahasa Indonesia, dapatkan kata dasar masing-masing kata.")

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


if __name__ == "__main__":
    demo.launch()
