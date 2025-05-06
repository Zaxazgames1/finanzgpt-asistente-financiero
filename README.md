
```markdown
# FinanzGPT - Asistente Financiero Empresarial

FinanzGPT es una aplicación web desarrollada en Streamlit que funciona como un asistente financiero inteligente para el análisis de indicadores económicos empresariales. Utilizando técnicas de procesamiento de lenguaje natural (NLP), la aplicación permite analizar la salud financiera de las empresas e interactuar mediante un chat para obtener recomendaciones personalizadas.

## Características

- **Análisis financiero completo**: Evalúa indicadores clave como endeudamiento, rentabilidad, productividad y rotación de cartera.
- **Interfaz conversacional**: Chat con FinanzGPT para consultar aspectos específicos de los resultados financieros.
- **Procesamiento de lenguaje natural**: Utiliza técnicas de NLP para comprender consultas y generar respuestas contextuales.
- **Visualización de datos**: Representa gráficamente los indicadores para una mejor interpretación.
- **Recomendaciones personalizadas**: Sugiere acciones específicas para mejorar la salud financiera de la empresa.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/finanzgpt.git
   cd finanzgpt
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## Uso

1. Ingresa los datos financieros básicos de tu empresa.
2. Explora el análisis detallado generado automáticamente.
3. Interactúa con el chatbot para obtener recomendaciones específicas:
   - Consulta sobre endeudamiento
   - Análisis de rentabilidad
   - Sugerencias para mejorar productividad
   - Optimización de rotación de cartera

## Estructura del Proyecto

El proyecto está organizado siguiendo principios de programación orientada a objetos:

- `app.py`: Punto de entrada de la aplicación
- `models/`: Clases y modelos de datos
  - `empresa.py`: Modelo para gestionar datos empresariales
  - `analisis.py`: Modelo para resultados de análisis
- `services/`: Servicios y lógica de negocio
  - `analizador_financiero.py`: Servicios de análisis financiero
  - `nlp_service.py`: Procesamiento de lenguaje natural
- `utils/`: Utilidades generales
  - `formatters.py`: Formateo de datos y valores
  - `validators.py`: Validación de entradas
- `ui/`: Componentes de interfaz de usuario
  - `styles.py`: Definiciones de estilos CSS
  - `chat_ui.py`: Interfaz de chat
  - `form_ui.py`: Formularios de ingreso de datos
  - `results_ui.py`: Visualización de resultados

## Tecnologías Utilizadas

- **Streamlit**: Framework para aplicaciones web con Python
- **NLTK y spaCy**: Bibliotecas para procesamiento de lenguaje natural
- **Matplotlib**: Visualización de datos
- **scikit-learn**: Operaciones ML para análisis de texto
- **Pandas**: Manipulación y análisis de datos

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios importantes.

## Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).
```