# Asistente-de-Soporte-IA
implementa un modelo de lenguaje generativo basado en GPT-2


# Asistente IA Generativa para Soporte Técnico (Sistema de Cartera)

Este repositorio contiene un MVP de **IA generativa** para automatizar respuestas de soporte técnico (tipo FAQ) en un sistema de gestión de cartera.  
Se entrenó un modelo tipo GPT-2 en español mediante **fine-tuning** con un dataset del dominio y se desplegó una interfaz web con **Gradio**.

## Enlaces
- **Notebook (Google Colab):** https://colab.research.google.com/drive/12GrqqZKW9q527PQaZTqdaXb5QlECuZWS#scrollTo=l61UEk3oeIk2
- **Aplicación desplegada (Hugging Face Space):** https://huggingface.co/spaces/terrygarcia/soporte-ia-generativa

---

## Estructura del proyecto

- `colab/` (opcional)  
  Contiene el notebook o export del entrenamiento.
- `dataset/` (opcional)  
  Dataset final en formato JSON/CSV.
- `finetuned_model.zip`  
  Modelo ajustado (exportado) listo para cargar en la app.
- `app.py`  
  Aplicación Gradio para probar el modelo en una web.
- `requirements.txt`  
  Dependencias para ejecutar el proyecto.
- `README.md`  
  Manual de instalación y guía de usuario.

> Nota: El proyecto no incluye el nombre real de la aplicación/empresa para mantener neutralidad y privacidad.

---

## Requisitos

- Python 3.10+ (recomendado)
- pip
- (Opcional) GPU para entrenamiento. Para ejecutar la app puede funcionar en CPU, aunque será más lenta.

---

## Instalación (modo local)

1) Clona el repositorio:
```bash
git clone https://github.com/terrygarcia-afk/Asistente-de-Soporte-IA
cd Asistente-de-Soporte-IA
