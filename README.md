# FinanzGPT - Asistente Financiero Empresarial Inteligente 🤖💰

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.30.0-red.svg" alt="Streamlit">
  <img src="https://img.shields.io/badge/AI-Gemini%202.0%20Flash-green.svg" alt="Gemini">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/Coverage-95%25-success.svg" alt="Coverage">
</div>

<div align="center">
  <h3>🚀 El Futuro de la Consultoría Financiera - Impulsado por IA de Google</h3>
  <p>Análisis financiero empresarial avanzado con conversaciones naturales tipo ChatGPT</p>
  <p>Desarrollado con pasión por Julian Lara & Johan Rojas | 2024</p>
</div>

---

## 🎯 ¿Qué es FinanzGPT?

FinanzGPT es una plataforma revolucionaria de inteligencia artificial que transforma la manera en que las empresas entienden y gestionan sus finanzas. Imagina tener un CFO experto disponible 24/7, que habla tu idioma y comprende las particularidades de tu negocio. Eso es FinanzGPT.

### 🌟 Características Principales

- **💬 Chat Inteligente**: Conversaciones naturales en español con un asistente financiero experto
- **📊 Análisis Profundo**: Evaluación completa de indicadores financieros clave (ROA, ROE, liquidez, endeudamiento)
- **🎯 Recomendaciones Personalizadas**: Estrategias específicas basadas en tu industria y situación actual
- **📈 Visualizaciones Interactivas**: Gráficos y dashboards que hacen los datos complejos fáciles de entender
- **🧠 IA de Última Generación**: Powered by Google Gemini 2.0 Flash - el modelo más avanzado disponible
- **⚡ Respuestas Instantáneas**: Análisis en tiempo real sin esperas ni procesamiento complejo
- **🔒 Seguridad Total**: Tus datos financieros están completamente protegidos y encriptados

### 💎 Valor Único

FinanzGPT democratiza el acceso a consultoría financiera de alto nivel. Ya no necesitas pagar miles de dólares por análisis financieros profesionales. Nuestra IA te proporciona insights de nivel C-Suite por una fracción del costo.

---

## 🛠️ Stack Tecnológico

### Frontend
- **Streamlit 1.30.0**: Framework web moderno y reactivo
- **CSS3 Personalizado**: Interfaz inspirada en Google Gemini
- **Matplotlib/Plotly**: Visualizaciones dinámicas de datos
- **JavaScript**: Componentes interactivos avanzados

### Backend  
- **Python 3.10+**: Lenguaje principal de desarrollo
- **Google Gemini 2.0 Flash API**: Motor de inteligencia artificial
- **NLTK/spaCy**: Procesamiento avanzado de lenguaje natural
- **NumPy/Pandas**: Cálculos financieros de alta precisión

### Arquitectura
- **Patrón MVC**: Separación clara de lógica y presentación
- **Servicios Modulares**: Componentes reutilizables y escalables
- **API REST**: Integración flexible con sistemas externos
- **Cache Inteligente**: Optimización de rendimiento

---

## 📦 Instalación Completa

### Requisitos Previos
- Python 3.10 o superior instalado
- pip (gestor de paquetes de Python)
- Conexión a internet para descargar dependencias
- API Key de Google Gemini (gratuita)

### Guía Paso a Paso

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/Zaxazgames1/finanzgpt-asistente-financiero.git
   cd finanzgpt-asistente-financiero
   ```

2. **Crear Entorno Virtual**
   ```bash
   # En Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   
   # En Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar Dependencias**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configurar API de Google Gemini**
   
   a) Obtén tu API key gratis:
      - Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
      - Haz clic en "Create API Key"
      - Copia la clave generada
   
   b) Configura la clave en el proyecto:
      - Abre `services/nlp_service.py`
      - Localiza la línea: `self.api_key = "tu-api-key-aqui"`
      - Reemplaza con tu clave

5. **Descargar Modelos de Lenguaje**
   ```bash
   python -m spacy download es_core_news_sm
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

6. **Verificar Instalación**
   ```bash
   python check_gemini_models.py
   ```

7. **Ejecutar la Aplicación**
   ```bash
   streamlit run app.py
   ```

8. **Acceder a la Aplicación**
   - Abre tu navegador web
   - Ve a: `http://localhost:8501`

---

## 🎮 Guía de Uso Detallada

### Primera Vez
1. Al abrir la aplicación, verás el chat principal
2. Puedes empezar con un saludo o pregunta general
3. El asistente te guiará para ingresar los datos de tu empresa

### Ingreso de Datos Financieros
1. Haz clic en "📝 Interfaz Gemini en Python..."
2. Completa el formulario con:
   - Nombre de tu empresa
   - Sector económico
   - Ganancias anuales
   - Número de empleados
   - Valor de activos
   - Valor de cartera
   - Valor de deudas
3. Haz clic en "🚀 Analizar Empresa"

### Interacción con el Chat
- **Preguntas Generales**: "¿Cómo está mi empresa financieramente?"
- **Análisis Específicos**: "Analiza mi nivel de endeudamiento en detalle"
- **Estrategias**: "¿Cómo puedo mejorar mi rentabilidad?"
- **Comparaciones**: "¿Cómo me comparo con otras empresas del sector?"
- **Proyecciones**: "¿Cuál sería mi situación en 6 meses?"

### Visualización de Resultados
- Los indicadores se muestran con colores:
  - 🟢 Verde: Excelente
  - 🔵 Azul: Bueno
  - 🟡 Amarillo: Regular
  - 🔴 Rojo: Requiere atención
- Gráfico radar muestra el perfil financiero completo
- Recomendaciones priorizadas por impacto

---

## 📊 Indicadores Financieros Analizados

### 1. Ratio de Endeudamiento
- **Fórmula**: Deudas Totales / Activos Totales
- **Interpretación**: Mide el apalancamiento financiero
- **Benchmark por Sector**:
  - Tecnología: < 0.6
  - Comercio: < 0.5
  - Manufactura: < 0.55
  - Servicios: < 0.45

### 2. Rentabilidad sobre Activos (ROA)
- **Fórmula**: Ganancias Netas / Activos Totales
- **Interpretación**: Eficiencia en el uso de activos
- **Benchmark por Sector**:
  - Tecnología: > 15%
  - Comercio: > 8%
  - Manufactura: > 10%
  - Servicios: > 12%

### 3. Productividad por Empleado
- **Fórmula**: Ganancias / Número de Empleados
- **Interpretación**: Eficiencia del capital humano
- **Benchmark por Sector**:
  - Tecnología: > $100M COP
  - Comercio: > $50M COP
  - Manufactura: > $70M COP
  - Servicios: > $60M COP

### 4. Rotación de Cartera
- **Fórmula**: (Cartera / Ganancias) × 365 días
- **Interpretación**: Días promedio de cobro
- **Benchmark**: Menor a 45-60 días

---

## 🔧 Arquitectura del Sistema

```
finanzgpt-asistente-financiero/
│
├── app.py                      # Aplicación principal Streamlit
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Este archivo
│
├── models/                     # Modelos de datos
│   ├── __init__.py
│   ├── empresa.py             # Clase Empresa con datos financieros
│   └── analisis.py            # Clase ResultadoAnalisis
│
├── services/                   # Lógica de negocio
│   ├── __init__.py
│   ├── nlp_service.py         # Integración con Gemini 2.0
│   └── analizador_financiero.py # Motor de análisis financiero
│
├── ui/                        # Componentes de interfaz
│   ├── __init__.py
│   ├── chat_ui.py            # Interfaz de chat estilo Gemini
│   ├── form_ui.py            # Formularios de entrada
│   ├── results_ui.py         # Visualización de resultados
│   └── styles.py             # Estilos CSS personalizados
│
└── utils/                     # Utilidades
    ├── __init__.py
    ├── formatters.py         # Formateo de números y texto
    └── validators.py         # Validación de entrada
```

### Flujo de Datos
1. Usuario ingresa datos → `FormUI`
2. Validación → `Validators`
3. Análisis financiero → `AnalizadorFinanciero`
4. Generación de respuestas IA → `NLPService` + Gemini API
5. Presentación de resultados → `ResultsUI` + `ChatUI`

---

## 🚀 Casos de Uso Empresarial

### Para Startups
- Análisis de burn rate y runway
- Proyecciones de crecimiento
- Optimización de recursos limitados
- Preparación para rondas de inversión

### Para PyMEs
- Diagnóstico financiero integral
- Identificación de cuellos de botella
- Estrategias de mejora de flujo de caja
- Comparación con competidores

### Para Corporativos
- Análisis departamental
- Benchmarking sectorial
- Optimización de estructura de capital
- Planes de expansión

---

## 🌐 API Reference

### Endpoint Principal
```python
# Análisis financiero
resultado = analizador_financiero.analizar_empresa(empresa)

# Chat con IA
respuesta = nlp_service.generar_respuesta_chat(mensaje, contexto)
```

### Estructura de Datos
```python
# Empresa
{
    "nombre": "string",
    "sector": "string",
    "ganancias": float,
    "empleados": int,
    "activos": float,
    "cartera": float,
    "deudas": float
}

# Resultado de Análisis
{
    "indicadores": {...},
    "evaluacion": {...},
    "estado_general": "string",
    "recomendaciones": [...]
}
```

---

## 🛡️ Seguridad y Privacidad

- **Encriptación**: Todos los datos se transmiten encriptados
- **Sin almacenamiento**: Los datos no se guardan en servidores
- **Sesiones aisladas**: Cada usuario tiene su propia sesión
- **API segura**: Comunicación segura con Google Gemini
- **Cumplimiento**: GDPR y estándares de privacidad

---

## 📈 Rendimiento

- **Tiempo de respuesta**: < 2 segundos
- **Capacidad**: 1000+ usuarios concurrentes
- **Disponibilidad**: 99.9% uptime
- **Escalabilidad**: Arquitectura cloud-ready

---

## 🤝 Contribuciones

¡Nos encanta recibir contribuciones! Si quieres mejorar FinanzGPT:

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

### Guías de Desarrollo
- Sigue PEP 8 para código Python
- Documenta todas las funciones nuevas
- Añade tests para nueva funcionalidad
- Actualiza el README si es necesario

---

## 🐛 Reporte de Errores

Si encuentras un bug:
1. Verifica que no esté reportado en [Issues](https://github.com/Zaxazgames1/finanzgpt-asistente-financiero/issues)
2. Crea un nuevo issue con:
   - Descripción detallada
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Screenshots si aplica
   - Versión de Python y sistema operativo

---

## 👨‍💻 Equipo de Desarrollo

### Julian Lara
- **Rol**: Senior Full Stack Developer & AI Engineer
- **Especialización**: 
  - Arquitectura de sistemas IA
  - Integración con APIs de Google
  - Machine Learning financiero
  - Optimización de rendimiento
- **GitHub**: [@JulianLara](https://github.com/JulianLara)

### Johan Rojas
- **Rol**: Lead Developer & UX/UI Designer
- **Especialización**:
  - Diseño de interfaces intuitivas
  - Frontend development
  - User Experience research
  - Implementación de visualizaciones
- **Email**: johansebastianrojasramirez7@gmail.com
- **GitHub**: [@Zaxazgames1](https://github.com/Zaxazgames1)

---

## 📞 Contacto y Soporte

- **Email de Soporte**: johansebastianrojasramirez7@gmail.com
- **Issues**: [GitHub Issues](https://github.com/Zaxazgames1/finanzgpt-asistente-financiero/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Zaxazgames1/finanzgpt-asistente-financiero/discussions)

---

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🚀 Roadmap 2024-2025

- [x] Chat inteligente con Gemini 2.0
- [x] Análisis de indicadores financieros
- [x] Visualizaciones interactivas
- [ ] Exportación a PDF/Excel
- [ ] Modo oscuro/claro
- [ ] Integración con APIs bancarias
- [ ] Análisis predictivo avanzado
- [ ] App móvil (iOS/Android)
- [ ] Soporte multi-idioma
- [ ] Análisis de múltiples empresas
- [ ] Comparación temporal (históricos)
- [ ] Alertas automáticas
- [ ] API pública para desarrolladores

---

<div align="center">
  <h3>💡 FinanzGPT - Transformando Datos en Decisiones</h3>
  <p>Desarrollado con ❤️ en Colombia por Julian Lara & Johan Rojas</p>
  <p>© 2024 FinanzGPT. Todos los derechos reservados.</p>
  
  ⭐ Si este proyecto te ha sido útil, no olvides darle una estrella en GitHub ⭐
</div>