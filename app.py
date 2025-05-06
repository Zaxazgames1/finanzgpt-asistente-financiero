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
    Clase principal que coordina la aplicación FinanzGPT.
    """
    def __init__(self):
        """
        Inicializa la aplicación FinanzGPT.
        """
        # Configuración de la página
        st.set_page_config(
            page_title="FinanzGPT - Asistente Financiero",
            page_icon="💹",
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
            st.session_state.page_view = "welcome"  # Opciones: "welcome", "chat", "form", "results"
        
        if 'datos_empresa' not in st.session_state:
            st.session_state.datos_empresa = None
        
        # Aplicar estilos CSS
        st.markdown(self.styles_ui.get_css(), unsafe_allow_html=True)
    
    def render_sidebar(self):
        """
        Renderiza la barra lateral con navegación y opciones.
        """
        with st.sidebar:
            st.markdown('<div class="main-title">FinanzGPT</div>', unsafe_allow_html=True)
            st.markdown('<div class="sub-title">Asistente Financiero Empresarial</div>', unsafe_allow_html=True)
            
            # Opciones de navegación
            st.markdown("### Navegación")
            
            # Contenedor para botones de navegación
            nav_col1, nav_col2 = st.columns([1, 1])
            
            with nav_col1:
                # Botón de Inicio
                if st.session_state.page_view == "welcome":
                    st.markdown('<div class="nav-button-active">🏠 Inicio</div>', unsafe_allow_html=True)
                else:
                    if st.button("🏠 Inicio", key="home_btn", use_container_width=True):
                        st.session_state.page_view = "welcome"
                        st.rerun()
                
                # Botón de Chat
                if st.session_state.page_view == "chat":
                    st.markdown('<div class="nav-button-active">💬 Chat</div>', unsafe_allow_html=True)
                else:
                    if st.button("💬 Chat", key="chat_btn", use_container_width=True):
                        st.session_state.page_view = "chat"
                        st.rerun()
            
            with nav_col2:
                # Botón de Formulario
                if st.session_state.page_view == "form":
                    st.markdown('<div class="nav-button-active">📝 Datos</div>', unsafe_allow_html=True)
                else:
                    if st.button("📝 Datos", key="form_btn", use_container_width=True):
                        st.session_state.page_view = "form"
                        st.rerun()
                
                # Botón de Resultados
                if st.session_state.page_view == "results":
                    st.markdown('<div class="nav-button-active">📊 Análisis</div>', unsafe_allow_html=True)
                else:
                    if st.button("📊 Análisis", key="results_btn", use_container_width=True):
                        if st.session_state.datos_empresa:
                            st.session_state.page_view = "results"
                            st.rerun()
                        else:
                            st.warning("Primero debes ingresar los datos de tu empresa.")
            
            st.markdown("---")
            
            # Información sobre la aplicación
            with st.expander("ℹ️ Acerca de FinanzGPT"):
                st.markdown("""
                FinanzGPT utiliza técnicas avanzadas de procesamiento de lenguaje natural para analizar y evaluar la salud financiera de empresas.
                
                **Tecnologías utilizadas:**
                
                * **Tokenización**: Divide el texto en unidades individuales
                * **Lematización**: Reduce palabras a su forma base
                * **POS Tagging**: Etiquetado gramatical
                * **Embedding**: Representación vectorial del texto
                
                **Indicadores financieros analizados:**
                * Ratio de endeudamiento
                * Rentabilidad sobre activos
                * Productividad por empleado
                * Rotación de cartera
                """)
            
            # Botón para limpiar historial de chat
            if st.button("🗑️ Limpiar conversación", use_container_width=True):
                if 'chat_history' in st.session_state:
                    st.session_state.chat_history = []
                st.info("Historial de chat borrado")
                time.sleep(1)
                st.rerun()
            
            st.markdown("---")
            st.markdown('<div style="text-align: center; color: #888;">Desarrollado con ❤️ usando Python y Streamlit</div>', unsafe_allow_html=True)
    
    def render_welcome(self):
        """
        Renderiza la pantalla de bienvenida.
        """
        st.markdown('<div class="main-title">Bienvenido a FinanzGPT</div>', unsafe_allow_html=True)
        
        # Contenedor principal
        welcome_container = st.container()
        
        with welcome_container:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("""
            ### Tu asistente inteligente para análisis financiero empresarial
            
            FinanzGPT te permite analizar la salud económica de tu empresa a través de un análisis detallado de tus principales indicadores financieros.
            
            **¿Cómo funciona?**
            
            1. Ingresa los datos básicos de tu empresa
            2. Nuestro sistema realiza un análisis completo
            3. Conversa con FinanzGPT y recibe respuestas personalizadas
            
            Utiliza el poder del procesamiento de lenguaje natural para obtener insights valiosos sobre tu negocio.
            """)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Botones de inicio
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("📝 Ingresar datos de mi empresa", use_container_width=True):
                    st.session_state.page_view = "form"
                    st.rerun()
            
            with col2:
                if st.session_state.datos_empresa:
                    if st.button("💬 Ir al chat", use_container_width=True):
                        st.session_state.page_view = "chat"
                        st.rerun()
                else:
                    st.button("💬 Ir al chat (primero ingresa datos)", use_container_width=True, disabled=True)
            
            # Ejemplos de preguntas
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("""
            ### Ejemplos de preguntas que puedes hacer
            
            Una vez que hayas ingresado los datos de tu empresa, podrás consultar a FinanzGPT sobre:
            
            - "¿Cómo optimizar mi rotación de cartera?"
            - "¿Es mi liquidez adecuada para el sector?"
            - "Dame un resumen general de mi empresa"
            - "Ayuda" (para ver un menú de opciones)
            """)
            st.markdown('</div>', unsafe_allow_html=True)
    
    def run(self):
        """
        Ejecuta la aplicación principal.
        """
        # Renderizar sidebar
        self.render_sidebar()
        
        # Renderizar la vista correspondiente
        if st.session_state.page_view == "welcome":
            self.render_welcome()
        
        elif st.session_state.page_view == "chat":
            self.chat_ui.renderizar_chat(st.session_state.datos_empresa)
        
        elif st.session_state.page_view == "form":
            datos_procesados = self.form_ui.renderizar_formulario()
            if datos_procesados:
                st.session_state.datos_empresa = datos_procesados
                st.session_state.page_view = "results"
                st.rerun()
        
        elif st.session_state.page_view == "results":
            self.results_ui.renderizar_resultados(st.session_state.datos_empresa)
        
        # Caso de error - redirigir a bienvenida
        else:
            st.session_state.page_view = "welcome"
            st.rerun()

# Código principal
if __name__ == "__main__":
    app = FinanzGPTApp()
    app.run()