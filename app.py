import streamlit as st
import time

# Importaciones de clases
from models.empresa import Empresa
from services.analizador_financiero import AnalizadorFinanciero
from services.nlp_service import NLPService
from utils.formatters import Formatters
from utils.validators import Validators
from ui.styles import StylesUI
from ui.chat_ui import ChatUI
from ui.form_ui import FormUI
from ui.results_ui import ResultsUI

# Clase principal de la aplicación
class FinanzGPTApp:
    """
    Clase principal que coordina la aplicación FinanzGPT con diseño tipo Gemini.
    """
    def __init__(self):
        """
        Inicializa la aplicación FinanzGPT.
        """
        # Configuración de la página
        st.set_page_config(
            page_title="FinanzGPT - Asistente Financiero",
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Inicializar servicios
        self.nlp_service = NLPService()
        self.analizador_financiero = AnalizadorFinanciero()
        
        # Inicializar utilidades
        self.formatters = Formatters()
        self.validators = Validators()
        
        # Inicializar componentes de UI
        self.styles_ui = StylesUI()
        self.chat_ui = ChatUI(self.nlp_service, self.formatters)
        self.form_ui = FormUI(self.analizador_financiero, self.validators)
        self.results_ui = ResultsUI(self.formatters)
        
        # Inicializar estado de la aplicación
        if 'page_view' not in st.session_state:
            st.session_state.page_view = "chat"
        
        if 'datos_empresa' not in st.session_state:
            st.session_state.datos_empresa = None
        
        # Aplicar estilos CSS tipo Gemini
        st.markdown(self.styles_ui.get_css(), unsafe_allow_html=True)
    
    def render_sidebar(self):
        """
        Renderiza la barra lateral estilo Gemini.
        """
        with st.sidebar:
            # Logo y título
            st.markdown("""
                <div style="padding: 1.5rem 0; text-align: center;">
                    <div style="font-size: 1.25rem; font-weight: 500; color: var(--text-primary); display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
                        <span style="background: linear-gradient(135deg, #FA8B00, #8B00FA); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.5rem;">🤖</span>
                        FinanzGPT
                    </div>
                    <div style="font-size: 0.8125rem; color: var(--text-muted); margin-top: 0.25rem;">
                        2.0 Flash
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Nueva conversación
            if st.button("➕ Nueva conversación", use_container_width=True):
                if 'chat_history' in st.session_state:
                    st.session_state.chat_history = []
                st.rerun()
            
            # Navegación principal
            st.markdown("""
                <div style="margin: 1.5rem 0; padding: 0 1rem;">
                    <div style="font-size: 0.75rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem;">
                        Navegación
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            current_page = st.session_state.page_view
            
            # Chat
            if st.button("💬 Chat", use_container_width=True, disabled=(current_page == "chat")):
                st.session_state.page_view = "chat"
                st.rerun()
            
            # Descubrir Gems
            if st.button("🌟 Descubrir Gems", use_container_width=True, disabled=(current_page == "gems")):
                st.toast("Función en desarrollo", icon="🚧")
            
            # Historial
            st.markdown("""
                <div style="margin: 1.5rem 0; padding: 0 1rem;">
                    <div style="font-size: 0.75rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem;">
                        Reciente
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Conversaciones recientes
            if st.session_state.datos_empresa:
                empresa_nombre = st.session_state.datos_empresa.get('resultados', {}).get('nombre', 'Empresa')
                with st.container():
                    if st.button(f"🏢 {empresa_nombre}", use_container_width=True):
                        st.session_state.page_view = "results"
                        st.rerun()
            
            # Crear GUI con texto reflejado
            if st.button("📝 Interfaz Gemini en Python...", use_container_width=True, disabled=(current_page == "form")):
                st.session_state.page_view = "form"
                st.rerun()
            
            if st.button("📑 Crear GUI con texto reflejado", use_container_width=True):
                st.toast("Creando interfaz tipo Gemini...", icon="✨")
            
            # Espacio flexible
            st.markdown("""
                <div style="flex: 1;"></div>
            """, unsafe_allow_html=True)
            
            # Footer del sidebar
            st.markdown("""
                <hr style="margin: 2rem 0 1rem 0; border: none; border-top: 1px solid var(--border-color);">
                <div style="padding: 0 1rem 2rem 1rem;">
                    <button id="settings-btn" style="display: flex; align-items: center; gap: 0.5rem; color: var(--text-secondary); background: none; border: none; text-decoration: none; font-size: 0.875rem; padding: 0.5rem 0; cursor: pointer; width: 100%; text-align: left;">
                        ⚙️ Ajustes y ayuda
                    </button>
                </div>
            """, unsafe_allow_html=True)
            
            # Botón de Ajustes y ayuda
            if st.button("⚙️ Ajustes y ayuda", use_container_width=True):
                st.toast("Configuración en desarrollo", icon="⚙️")
            
            # Botón de Acerca de
            if st.button("ℹ️ Acerca de FinanzGPT", use_container_width=True, disabled=(current_page == "about")):
                st.session_state.page_view = "about"
                st.rerun()
    
    def render_header(self):
        """
        Header minimalista o vacío para mantener el estilo Gemini.
        """
        pass
    
    def render_welcome(self):
        """
        Renderiza la pantalla de bienvenida estilo Gemini.
        """
        st.markdown("""
            <div class="welcome-container">
                <div class="welcome-icon">🤖</div>
                <h1 class="welcome-title">Hola, Johan Sebastián</h1>
                <p class="welcome-subtitle">
                    ¿Cómo puedo ayudarte con tus finanzas empresariales hoy?
                </p>
                
                <div style="max-width: 600px; margin: 3rem auto;">
                    <div class="suggestions-title">Sugerencias para comenzar:</div>
                    <div class="suggestion-chips">
                        <div class="suggestion-chip">Analiza mi situación financiera</div>
                        <div class="suggestion-chip">¿Cómo mejorar la rentabilidad?</div>
                        <div class="suggestion-chip">Estrategias de crecimiento</div>
                        <div class="suggestion-chip">Reducir deuda empresarial</div>
                    </div>
                </div>
                
                <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 3rem;">
                    <button class="deep-research-button" style="display: inline-flex; align-items: center; gap: 0.5rem;">
                        🔍 Deep Research
                    </button>
                    <button class="canvas-button">
                        📊 Canvas
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    def render_about(self):
        """
        Renderiza la página Acerca de con información de desarrolladores y tecnología.
        """
        # En lugar de usar HTML raw, usar componentes de Streamlit
        st.markdown("# 🤖 FinanzGPT")
        st.markdown("*Asistente Financiero Inteligente potenciado por IA de última generación*")
        
        st.markdown("---")
        
        # Sección de tecnología
        st.markdown("## 🧠 Google Gemini 2.0 Flash")
        st.markdown("### Motor de Inteligencia Artificial")
        
        st.info("""
        FinanzGPT utiliza **Google Gemini 2.0 Flash**, uno de los modelos de IA más avanzados del mercado. 
        Esta tecnología de vanguardia permite:
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("✅ Comprensión profunda del contexto financiero")
            st.markdown("✅ Respuestas en español natural y fluido")
            st.markdown("✅ Análisis en tiempo real con alta precisión")
        
        with col2:
            st.markdown("✅ Generación de recomendaciones personalizadas")
            st.markdown("✅ Procesamiento de datos financieros complejos")
            st.markdown("✅ Aprendizaje continuo y mejora constante")
        
        st.markdown("---")
        
        # Arquitectura y tecnología
        st.markdown("## ⚡ Arquitectura y Tecnología")
        st.markdown("### Stack tecnológico de vanguardia")
        
        st.info("FinanzGPT está construido con las mejores tecnologías disponibles:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("🐍 **Python 3.10+** - Lenguaje principal")
            st.markdown("🚀 **Streamlit** - Framework web moderno")
            st.markdown("🤖 **Gemini API** - Motor de IA")
        
        with col2:
            st.markdown("📊 **Matplotlib** - Visualización de datos")
            st.markdown("🔍 **NLTK & spaCy** - Procesamiento de lenguaje")
            st.markdown("💾 **NumPy & Pandas** - Análisis de datos")
        
        st.markdown("---")
        
        # Equipo de desarrollo
        st.markdown("## 👨‍💻 Equipo de Desarrollo")
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.markdown("### 🎯 Julian Lara")
                st.markdown("**Full Stack Developer & AI Engineer**")
                st.markdown("""
                Especialista en inteligencia artificial y arquitectura de software. 
                Experto en integración de modelos de IA y desarrollo de interfaces intuitivas.
                """)
        
        with col2:
            with st.container():
                st.markdown("### 💡 Johan Rojas")
                st.markdown("**Lead Developer & UX Designer**")
                st.markdown("""
                Líder en desarrollo de aplicaciones web y diseño de experiencia de usuario. 
                Experto en crear interfaces elegantes y funcionales.
                """)
        
        st.markdown("---")
        
        # Capacidades
        st.markdown("## 🎯 ¿Qué puede hacer FinanzGPT?")
        st.markdown("### Capacidades y funcionalidades")
        
        st.info("FinanzGPT es un asistente financiero completo que puede:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("📊 Analizar indicadores financieros clave (ROA, ROE, liquidez)")
            st.markdown("💡 Generar recomendaciones personalizadas para tu empresa")
            st.markdown("📈 Crear visualizaciones interactivas de datos")
        
        with col2:
            st.markdown("🎯 Diseñar estrategias de crecimiento")
            st.markdown("💬 Responder preguntas complejas sobre finanzas")
            st.markdown("🔮 Proyectar escenarios futuros")
        
        st.markdown("---")
        
        # Sección de contacto
        st.markdown("## 📞 ¿Interesado en nuestros servicios?")
        st.info("""
        Desarrollamos chatbots inteligentes personalizados para empresas. 
        Transformamos tu servicio al cliente con IA de última generación.
        """)
        
        if st.button("📧 Contáctanos para tu proyecto", type="primary", use_container_width=True):
            st.success("¡Gracias por tu interés! Nos pondremos en contacto pronto.")
    
    def run(self):
        """
        Ejecuta la aplicación principal con diseño tipo Gemini.
        """
        # Renderizar header (vacío o minimalista)
        self.render_header()
        
        # Renderizar sidebar
        self.render_sidebar()
        
        # Renderizar la vista correspondiente
        if st.session_state.page_view == "chat":
            self.chat_ui.renderizar_chat(st.session_state.datos_empresa)
        
        elif st.session_state.page_view == "form":
            datos_procesados = self.form_ui.renderizar_formulario()
            if datos_procesados:
                st.session_state.datos_empresa = datos_procesados
                st.session_state.page_view = "results"
                st.rerun()
        
        elif st.session_state.page_view == "results":
            if st.session_state.datos_empresa:
                self.results_ui.renderizar_resultados(st.session_state.datos_empresa)
            else:
                st.warning("⚠️ No hay datos para mostrar. Por favor, ingresa primero los datos de tu empresa.")
                if st.button("📝 Ir a Datos"):
                    st.session_state.page_view = "form"
                    st.rerun()
        
        elif st.session_state.page_view == "about":
            self.render_about()
        
        else:
            self.render_welcome()

# Código principal
if __name__ == "__main__":
    app = FinanzGPTApp()
    app.run()