import streamlit as st
import time

# Importaciones de clases
from models.empresa import Empresa
from services.analizador_financiero import AnalizadorFinanciero
from services.nlp_service import NLPService
from services.conversational_analyzer import ConversationalAnalyzer
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
        
        # Inicializar analizador conversacional
        self.conversational_analyzer = ConversationalAnalyzer(
            self.analizador_financiero, 
            self.nlp_service
        )
        
        # Inicializar utilidades
        self.formatters = Formatters()
        self.validators = Validators()
        
        # Inicializar componentes de UI con el analizador conversacional
        self.styles_ui = StylesUI()
        self.chat_ui = ChatUI(self.nlp_service, self.formatters, self.conversational_analyzer)
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
                # Resetear el estado conversacional
                self.conversational_analyzer.resetear_conversacion()
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
            
            # Chat - siempre disponible
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
                        st.session_state.page_view = "chat"
                        st.rerun()
            
            # Ya no necesitamos el botón de formulario
            # Solo mantenemos el botón de GUI
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
    
    def run(self):
        """
        Ejecuta la aplicación principal con diseño tipo Gemini.
        """
        # Renderizar header (vacío o minimalista)
        self.render_header()
        
        # Renderizar sidebar
        self.render_sidebar()
        
        # Siempre mostrar el chat como vista principal
        if st.session_state.page_view == "chat":
            self.chat_ui.renderizar_chat(st.session_state.datos_empresa)
        
        elif st.session_state.page_view == "about":
            self.render_about()
        
        else:
            # Por defecto, mostrar chat
            self.chat_ui.renderizar_chat(st.session_state.datos_empresa)

    def render_about(self):
        """
        Renderiza la página Acerca de con información detallada y profesional.
        """
        # [Mantener el código existente de render_about]
        pass

# Código principal
if __name__ == "__main__":
    app = FinanzGPTApp()
    app.run()