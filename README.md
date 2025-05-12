# FinanzGPT - Asistente Financiero Empresarial con IA

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.30.0-red.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/AI-Gemini%202.0-green.svg" alt="Gemini">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</div>

<div align="center">
  <h3>🤖 Tu CFO Virtual Potenciado por Inteligencia Artificial</h3>
  <p>Análisis financiero empresarial avanzado con conversaciones naturales tipo ChatGPT</p>
</div>

---

## 🚀 Descripción

FinanzGPT es una aplicación web de última generación que combina el poder de Google Gemini 2.0 Flash con análisis financiero empresarial profesional. Diseñada para democratizar el acceso a consultoría financiera de alto nivel, nuestra plataforma ofrece:

- 💬 **Chat conversacional tipo ChatGPT** especializado en finanzas
- 📊 **Análisis profundo de indicadores** financieros clave
- 🎯 **Recomendaciones personalizadas** basadas en IA
- 📈 **Visualizaciones interactivas** de datos financieros
- 🧠 **Procesamiento de lenguaje natural** en español

## ✨ Características Principales

### 🤖 Inteligencia Artificial Avanzada
- **Google Gemini 2.0 Flash**: Modelo de IA de última generación
- **Respuestas contextuales**: Comprende y mantiene el contexto de la conversación
- **Análisis predictivo**: Proyecciones y escenarios futuros
- **Procesamiento en español**: Optimizado para el mercado hispanohablante

### 📊 Análisis Financiero Integral
- **Ratio de Endeudamiento**: Evaluación de estructura de capital
- **Rentabilidad (ROA)**: Análisis de retorno sobre activos
- **Productividad**: Eficiencia por empleado
- **Rotación de Cartera**: Gestión de cobros y liquidez

### 💡 Características Únicas
- **Interfaz conversacional**: Similar a ChatGPT pero especializada
- **Análisis sectorial**: Comparación con estándares de la industria
- **Planes de acción**: Recomendaciones paso a paso
- **Visualizaciones**: Gráficos interactivos y dashboards

## 🛠️ Tecnologías Utilizadas

<table>
<tr>
<td>

### Frontend
- **Streamlit**: Framework web en Python
- **HTML/CSS**: Estilos personalizados
- **Matplotlib**: Visualización de datos

</td>
<td>

### Backend
- **Python 3.10+**: Lenguaje principal
- **Google Gemini API**: Generación de respuestas
- **NLTK/spaCy**: Procesamiento de texto

</td>
<td>

### IA/ML
- **Gemini 2.0 Flash**: Modelo de lenguaje
- **Scikit-learn**: Análisis de texto
- **Transformers**: NLP avanzado

</td>
</tr>
</table>

## 📦 Instalación

### Prerrequisitos
- Python 3.10 o superior
- pip (gestor de paquetes)
- API Key de Google Gemini (gratis)

### Pasos de Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/finanzgpt-asistente-financiero.git
   cd finanzgpt-asistente-financiero
   ```

2. **Crea un entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura tu API Key de Gemini**
   
   Obtén tu API key gratuita en [Google AI Studio](https://makersuite.google.com/app/apikey)
   
   Luego, abre `services/nlp_service.py` y reemplaza:
   ```python
   self.api_key = "tu-api-key-aqui"
   ```

5. **Ejecuta la aplicación**
   ```bash
   streamlit run app.py
   ```

6. **Abre en tu navegador**
   ```
   http://localhost:8501
   ```

## 🎮 Uso

### 1. Ingreso de Datos
- Navega a la sección "📝 Datos"
- Completa el formulario con información financiera de tu empresa
- Los datos se procesarán automáticamente

### 2. Chat Inteligente
- Ve a la sección "💬 Chat"
- Realiza preguntas sobre tus finanzas
- Recibe respuestas detalladas y recomendaciones

### 3. Análisis Visual
- Accede a "📊 Análisis"
- Visualiza gráficos interactivos
- Descarga informes ejecutivos

### Ejemplos de Preguntas

```
👤: "Hola, ¿cómo está mi empresa financieramente?"
🤖: "¡Hola! Basándome en los datos de tu empresa, veo que..."

👤: "¿Cómo puedo mejorar mi rentabilidad?"
🤖: "Para mejorar tu rentabilidad, te recomiendo estas estrategias..."

👤: "Dame un análisis completo de mi endeudamiento"
🤖: "Aquí está el análisis detallado de tu endeudamiento..."
```

## 🔧 Configuración Avanzada

### Personalización del Modelo
```python
# En services/nlp_service.py
generation_config = {
    "temperature": 0.9,  # Creatividad (0.0 - 1.0)
    "top_p": 0.95,      # Diversidad de respuestas
    "max_output_tokens": 2048,  # Longitud máxima
}
```

### Agregar Nuevos Indicadores
```python
# En services/analizador_financiero.py
def calcular_nuevo_indicador(self, parametro1, parametro2):
    return parametro1 / parametro2
```

## 📊 Estructura del Proyecto

```
finanzgpt-asistente-financiero/
│
├── app.py                      # Aplicación principal
├── requirements.txt            # Dependencias
├── README.md                   # Este archivo
│
├── models/                     # Modelos de datos
│   ├── empresa.py             # Clase Empresa
│   └── analisis.py            # Clase ResultadoAnalisis
│
├── services/                   # Lógica de negocio
│   ├── nlp_service.py         # Integración con Gemini
│   └── analizador_financiero.py # Análisis financiero
│
├── ui/                        # Interfaz de usuario
│   ├── chat_ui.py            # Componente de chat
│   ├── form_ui.py            # Formularios
│   ├── results_ui.py         # Visualización resultados
│   └── styles.py             # Estilos CSS
│
└── utils/                     # Utilidades
    ├── formatters.py         # Formateo de datos
    └── validators.py         # Validación de entrada
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

### Guías de Contribución
- Sigue el estilo de código PEP 8
- Añade tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario

## 🐛 Reporte de Errores

Si encuentras un bug, por favor abre un issue con:
- Descripción detallada del problema
- Pasos para reproducir
- Screenshots si es aplicable
- Versión de Python y sistema operativo

## 📈 Roadmap

- [ ] Soporte multi-idioma
- [ ] Exportación a PDF/Excel
- [ ] Integración con APIs bancarias
- [ ] Análisis de múltiples empresas
- [ ] Modo oscuro
- [ ] App móvil
- [ ] Webhooks para alertas

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👏 Agradecimientos

- Google Gemini Team por la increíble API
- Streamlit por el framework web
- La comunidad de Python por las herramientas

## 📞 Contacto

- **Autor**: Tu Nombre
- **Email**: tu-email@ejemplo.com
- **LinkedIn**: [tu-perfil](https://linkedin.com/in/tu-perfil)
- **GitHub**: [@tu-usuario](https://github.com/tu-usuario)

---

<div align="center">
  <p>Hecho con ❤️ y ☕ usando Python y Streamlit</p>
  <p>⭐ Si te gusta este proyecto, no olvides darle una estrella ⭐</p>
</div>