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
    Clase principal que coordina la aplicación FinanzGPT con diseño ultra moderno.
    """
    def __init__(self):
        """
        Inicializa la aplicación FinanzGPT.
        """
        # Configuración de la página con tema oscuro
        st.set_page_config(
            page_title="FinanzGPT - Asistente Financiero",
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="collapsed"  # Sidebar colapsado por defecto
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
            st.session_state.page_view = "chat"  # Chat por defecto
        
        if 'datos_empresa' not in st.session_state:
            st.session_state.datos_empresa = None
        
        # Aplicar estilos CSS ultra modernos
        st.markdown(self.styles_ui.get_css(), unsafe_allow_html=True)
    
    def render_sidebar(self):
        """
        Renderiza la barra lateral con diseño moderno minimalista.
        """
        with st.sidebar:
            # Logo y título con animación
            st.markdown("""
                <div style="text-align: center; padding: 2rem 0;">
                    <div style="font-size: 3rem; margin-bottom: 0.5rem;">🤖</div>
                    <div class="main-title" style="font-size: 1.8rem;">FinanzGPT</div>
                    <div style="color: var(--text-secondary); font-size: 0.9rem;">
                        Asistente Financiero Inteligente
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<div style="border-top: 1px solid var(--border-color); margin: 1rem 0;"></div>', unsafe_allow_html=True)
            
            # Navegación moderna con iconos
            st.markdown("### 🧭 Navegación", unsafe_allow_html=True)
            
            # Botones de navegación con estilo moderno
            nav_options = [
                ("💬", "Chat", "chat"),
                ("📝", "Datos", "form"),
                ("📊", "Análisis", "results")
            ]
            
            for icon, label, page in nav_options:
                col1, col2 = st.columns([1, 5])
                with col1:
                    st.markdown(f'<div style="font-size: 1.5rem; text-align: center;">{icon}</div>', unsafe_allow_html=True)
                with col2:
                    btn_style = """
                        <style>
                            .nav-btn {
                                background: transparent;
                                border: 1px solid var(--border-color);
                                color: var(--text-primary);
                                padding: 0.75rem 1rem;
                                border-radius: 8px;
                                cursor: pointer;
                                transition: all 0.3s ease;
                                width: 100%;
                                text-align: left;
                                font-weight: 500;
                            }
                            .nav-btn:hover {
                                background: var(--bg-light);
                                border-color: var(--primary-color);
                                transform: translateX(5px);
                            }
                            .nav-btn.active {
                                background: var(--primary-color);
                                border-color: var(--primary-color);
                                color: white;
                                box-shadow: var(--shadow);
                            }
                        </style>
                    """
                    is_active = st.session_state.page_view == page
                    if st.button(label, key=f"nav_{page}", use_container_width=True):
                        if page == "results" and not st.session_state.datos_empresa:
                            st.warning("⚠️ Primero debes ingresar los datos de tu empresa.")
                        else:
                            st.session_state.page_view = page
                            st.rerun()
            
            st.markdown('<div style="border-top: 1px solid var(--border-color); margin: 2rem 0 1rem 0;"></div>', unsafe_allow_html=True)
            
            # Estado de la empresa si hay datos
            if st.session_state.datos_empresa:
                resultados = st.session_state.datos_empresa.get('resultados', {})
                estado = resultados.get('estado_general', 'Sin evaluar')
                color = '#10a37f' if estado in ['Excelente', 'Bueno'] else '#f59e0b' if estado == 'Regular' else '#ef4444'
                
                st.markdown(f"""
                    <div class="card" style="text-align: center;">
                        <h4 style="margin-bottom: 0.5rem;">🏢 {resultados.get('nombre', 'Empresa')}</h4>
                        <div style="
                            background: {color};
                            color: white;
                            padding: 0.5rem 1rem;
                            border-radius: 20px;
                            font-weight: 600;
                            display: inline-block;
                        ">
                            {estado}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Acciones rápidas
            st.markdown("### ⚡ Acciones Rápidas", unsafe_allow_html=True)
            
            if st.button("🗑️ Limpiar historial", use_container_width=True):
                if 'chat_history' in st.session_state:
                    st.session_state.chat_history = []
                st.success("✅ Historial limpio")
                time.sleep(1)
                st.rerun()
            
            if st.button("🔄 Nueva empresa", use_container_width=True):
                st.session_state.datos_empresa = None
                st.session_state.page_view = "form"
                st.rerun()
            
            # Footer
            st.markdown("""
                <div style="
                    position: absolute;
                    bottom: 20px;
                    left: 0;
                    right: 0;
                    text-align: center;
                    color: var(--text-secondary);
                    font-size: 0.8rem;
                ">
                    <div>Desarrollado con ❤️ por FinanzGPT</div>
                    <div style="margin-top: 0.5rem;">
                        <a href="#" style="color: var(--primary-color); text-decoration: none;">
                            Términos
                        </a>
                        •
                        <a href="#" style="color: var(--primary-color); text-decoration: none;">
                            Privacidad
                        </a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    def render_header(self):
        """
        Renderiza un header moderno minimalista.
        """
        col1, col2, col3 = st.columns([1, 3, 1])
        
        with col1:
            # Botón para abrir/cerrar sidebar
            if st.button("☰", help="Menú"):
                st.session_state.sidebar_state = not st.session_state.get('sidebar_state', False)
                st.rerun()
        
        with col2:
            # Indicador de página actual
            page_titles = {
                "chat": "💬 Chat Inteligente",
                "form": "📝 Datos de Empresa",
                "results": "📊 Análisis Financiero"
            }
            current_title = page_titles.get(st.session_state.page_view, "FinanzGPT")
            st.markdown(f"""
                <div style="text-align: center;">
                    <h2 style="margin: 0; color: var(--primary-color);">
                        {current_title}
                    </h2>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # Indicador de estado del modelo
            st.markdown("""
                <div style="text-align: right;">
                    <div class="badge badge-success" style="
                        display: inline-flex;
                        align-items: center;
                        gap: 0.5rem;
                    ">
                        <div class="loading-spinner" style="
                            width: 8px;
                            height: 8px;
                            border-width: 2px;
                        "></div>
                        IA Activa
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    def render_welcome_modern(self):
        """
        Renderiza la pantalla de bienvenida con diseño ultra moderno.
        """
        # Hero section
        st.markdown("""
            <div style="text-align: center; padding: 3rem 0;">
                <div style="font-size: 6rem; margin-bottom: 1rem;">🤖</div>
                <h1 class="main-title" style="font-size: 3rem; margin-bottom: 1rem;">
                    Bienvenido a FinanzGPT
                </h1>
                <p style="color: var(--text-secondary); font-size: 1.3rem; max-width: 600px; margin: 0 auto;">
                    Tu asistente financiero inteligente potenciado por IA de última generación
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Feature cards
        col1, col2, col3 = st.columns(3)
        
        features = [
            ("📊", "Análisis Inteligente", "Evaluación profunda de indicadores financieros con IA"),
            ("💡", "Recomendaciones", "Estrategias personalizadas para tu empresa"),
            ("🚀", "Crecimiento", "Planes de acción para maximizar resultados")
        ]
        
        for col, (icon, title, desc) in zip([col1, col2, col3], features):
            with col:
                st.markdown(f"""
                    <div class="card" style="text-align: center; height: 180px;">
                        <div style="font-size: 3rem; margin-bottom: 0.5rem;">{icon}</div>
                        <h3 style="color: var(--primary-color); margin-bottom: 0.5rem;">
                            {title}
                        </h3>
                        <p style="color: var(--text-secondary); font-size: 0.9rem;">
                            {desc}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
        
        # CTA buttons
        st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Comenzar Análisis", use_container_width=True):
                st.session_state.page_view = "form"
                st.rerun()
            
            st.markdown('<div style="margin: 1rem 0;"></div>', unsafe_allow_html=True)
            
            if st.button("💬 Ir al Chat", use_container_width=True):
                st.session_state.page_view = "chat"
                st.rerun()
    
    def run(self):
        """
        Ejecuta la aplicación principal con diseño moderno.
        """
        # Renderizar header
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
        
        else:
            self.render_welcome_modern()

# Código principal
if __name__ == "__main__":
    app = FinanzGPTApp()
    app.run()