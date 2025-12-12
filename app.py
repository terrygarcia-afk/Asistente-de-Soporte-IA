import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import zipfile
import os

# ========== Cargar modelo ==========
MODEL_ZIP = "finetuned_model.zip"
MODEL_DIR = "model"

if not os.path.exists(MODEL_DIR):
    with zipfile.ZipFile(MODEL_ZIP, "r") as zip_ref:
        zip_ref.extractall(MODEL_DIR)

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# ========== Limpieza de respuestas ==========
def clean_answer(ans, module):
    ans = ans.strip()

    forbidden = {
        "Cartera": ["pago", "planes", "comprar", "días"],
        "Cierres": ["planes", "pago", "comprar"],
        "ComprarDias": ["cartera", "cierres"],
    }

    for word in forbidden.get(module, []):
        idx = ans.lower().find(word)
        if idx != -1:
            ans = ans[:idx].strip()

    # máximo 2 frases
    parts = ans.split(". ")
    return ". ".join(parts[:2]).strip()

# ========== Función de inferencia ==========
def generate_answer(module, question):
    prompt = (
        "Eres un asistente de soporte técnico.\n"
        "Responde únicamente sobre el módulo indicado.\n"
        "No menciones otros módulos ni procesos diferentes.\n"
        "Sé claro, preciso y conciso.\n\n"
        f"Módulo: {module}\n"
        f"Pregunta: {question}\n"
        "Respuesta:"
    )

    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    outputs = model.generate(
        **inputs,
        max_new_tokens=80,
        do_sample=False,
        num_beams=4,
        repetition_penalty=1.3,
        no_repeat_ngram_size=4,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = text.split("Respuesta:")[-1].strip()
    answer = answer.split("Módulo:")[0].split("Pregunta:")[0].strip()

    return clean_answer(answer, module)

# ========== Interfaz Gradio ==========
interface = gr.Interface(
    fn=generate_answer,
    inputs=[
        gr.Dropdown(
            choices=[
                "General", "Rutas", "Cierres", "Cartera",
                "Movimientos", "Cajas", "Reportes",
                "Seguridad", "AppMovil", "ComprarDias"
            ],
            label="Módulo"
        ),
        gr.Textbox(
            label="Pregunta",
            placeholder="Ej: ¿Qué significa cartera atrasada?"
        )
    ],
    outputs=gr.Textbox(label="Respuesta"),
    title="Asistente de Soporte IA",
    description="Asistente de soporte técnico entrenado con fine-tuning sobre un sistema de cartera."
)

interface.launch()
