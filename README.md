# 🗣️ Service-Connect-ElevenLabs

**Integración en Python con los agentes de voz de [ElevenLabs](https://www.elevenlabs.io/)** para procesamiento conversacional de texto a voz (TTS) y reconocimiento de voz (STT), compatible tanto con **Linux como Windows**.

Este proyecto permite crear un asistente de voz interactivo que se comunica con los modelos de ElevenLabs en tiempo real. Ideal para proyectos de IA conversacional, asistentes virtuales o interfaces de voz personalizadas.

---

## 🚀 Características

- ✅ Soporte multiplataforma (Windows y Linux)
- 🎤 Entrada y salida de voz en tiempo real
- 🔄 Conversaciones activas gestionadas por un agente ElevenLabs
- 📡 Manejo de eventos y respuestas del agente de forma personalizada
- 🔐 Gestión de claves y configuraciones mediante variables de entorno

---

## 📦 Requisitos

- Python 3.8 o superior
- Claves de API de ElevenLabs
- Archivo `.env` con las siguientes variables:

```env
ELEVENLABS_API_KEY=tu_api_key_aqui
AGENT_ID=tu_agent_id_aqui
