# Asistente de Soporte IA Generativa

Este proyecto implementa un asistente de soporte técnico basado en inteligencia artificial generativa, desarrollado como un MVP funcional para automatizar la atención a consultas frecuentes dentro de un sistema de gestión de cartera.

La solución utiliza un modelo Transformer autoregresivo (GPT-2 en español) ajustado mediante fine-tuning con un dataset específico del dominio, permitiendo generar respuestas textuales claras, contextualizadas y alineadas con el funcionamiento real del sistema.

---

## Enlaces del proyecto

- Notebook de entrenamiento (Google Colab):  
  https://colab.research.google.com/drive/12GrqqZKW9q527PQaZTqdaXb5QlECuZWS

- Aplicación desplegada (Hugging Face Spaces):  
  https://huggingface.co/spaces/terrygarcia/soporte-ia-generativa

- Repositorio GitHub:  
  https://github.com/terrygarcia-afk/Asistente-de-Soporte-IA

---

## Estructura del repositorio

```text
├── app.py
├── requirements.txt
├── finetuned_model.zip
├── README.md



Requisitos

Python 3.9 o superior

torch

transformers

datasets

gradio

Instalación y ejecución local

Clonar el repositorio:

git clone https://github.com/terrygarcia-afk/Asistente-de-Soporte-IA.git
cd Asistente-de-Soporte-IA


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la aplicación:

python app.py


Abrir en el navegador:

http://localhost:7860

Guía de usuario

La aplicación permite interactuar con un asistente de soporte técnico entrenado con IA generativa.

Pasos de uso

Selecciona el módulo correspondiente a tu consulta (Cierres, Cartera, Reportes, AppMovil, ComprarDias, etc.).

Escribe tu pregunta en lenguaje natural.

Presiona el botón Submit para obtener la respuesta generada.

Ejemplos de preguntas

Cierres

¿Cómo generar un cierre?

¿Quién puede validar un cierre?

¿Por qué no puedo editar un cierre validado?

Reportes

¿Cómo exportar un reporte a Excel?

¿Por qué un reporte sale vacío?

¿Cómo generar un reporte por periodo?

AppMovil

¿Qué hago si la app no se sincroniza?

¿La app funciona sin internet?

¿Qué pasa cuando vuelve la conexión?

Cartera

¿Qué significa cartera atrasada?

¿Cuál es la diferencia entre cartera vencida y atrasada?

¿Qué significa el saldo pendiente?

ComprarDias

¿Cómo comprar un paquete de días?

¿Qué hago si compré días y no se reflejan?

¿Qué planes están disponibles?

Descripción técnica

Modelo base: GPT-2 en español (datificate/gpt2-small-spanish)

Tipo: Modelo Transformer autoregresivo

Técnica aplicada: Fine-tuning con dataset propio

Tipo de contenido: Generación de texto

Interfaz: Gradio

Despliegue: Hugging Face Spaces

El dataset fue construido y reforzado manualmente a partir de preguntas reales de soporte técnico, incorporando variaciones controladas para mejorar la robustez y coherencia del modelo.

Evaluación del modelo

El modelo fue evaluado mediante:

Métrica de entrenamiento (training loss)

Métricas automáticas de texto (ROUGE)

Evaluación humana comparando resultados antes y después del ajuste fino

La evaluación humana confirmó mejoras claras en coherencia, precisión y alineación con el dominio del sistema.

Limitaciones

Puede generar respuestas generales ante preguntas ambiguas.

Depende directamente de la calidad del dataset.

No reemplaza completamente al soporte humano en casos críticos.

Posibles mejoras

Ampliar el dataset con más casos reales.

Integrar el asistente directamente con WhatsApp.

Implementar detección automática de intención.

Incorporar retroalimentación del usuario para reentrenamiento continuo.




Licencia

Proyecto desarrollado con fines académicos y de demostración.




