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
            initial_sidebar_state="collapsed"
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
        
        # Aplicar estilos CSS ultra modernos
        st.markdown(self.styles_ui.get_css(), unsafe_allow_html=True)
    
    def render_sidebar(self):
        """
        Renderiza la barra lateral con diseño moderno minimalista.
        """
        with st.sidebar:
            # Header del Sidebar
            st.markdown("""
                <div class="sidebar-header">
                    <div class="logo-container">
                        <div class="logo">🤖</div>
                        <div class="logo-text">
                            <div class="brand-name">FinanzGPT</div>
                            <div class="brand-tagline">Asistente Financiero IA</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
            
            # Navegación
            st.markdown("""
                <div class="nav-section">
                    <div class="nav-title">🧭 NAVEGACIÓN</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Botones de navegación
            nav_options = [
                ("💬", "Chat", "chat"),
                ("📝", "Datos", "form"),
                ("📊", "Análisis", "results")
            ]
            
            current_page = st.session_state.page_view
            
            for icon, label, page in nav_options:
                is_active = current_page == page
                
                if st.button(
                    f"{icon} {label}", 
                    key=f"nav_{page}", 
                    use_container_width=True,
                    disabled=is_active
                ):
                    if page == "results" and not st.session_state.datos_empresa:
                        st.warning("⚠️ Primero debes ingresar los datos de tu empresa.")
                    else:
                        st.session_state.page_view = page
                        st.rerun()
            
            # Estado de la empresa si hay datos
            if st.session_state.datos_empresa:
                st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
                
                resultados = st.session_state.datos_empresa.get('resultados', {})
                estado = resultados.get('estado_general', 'Sin evaluar')
                nombre = resultados.get('nombre', 'Empresa')
                
                estado_class = {
                    'Excelente': 'status-excellent',
                    'Bueno': 'status-good',
                    'Regular': 'status-regular',
                    'Crítico': 'status-critical'
                }.get(estado, 'status-regular')
                
                st.markdown(f"""
                    <div class="company-status-card">
                        <div class="company-icon">🏢</div>
                        <div class="company-info">
                            <div class="company-name">{nombre}</div>
                            <div class="status-badge {estado_class}">{estado}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Acciones rápidas
            st.markdown("""
                <div class="sidebar-divider"></div>
                <div class="nav-section">
                    <div class="nav-title">⚡ ACCIONES RÁPIDAS</div>
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🗑️ Limpiar historial", use_container_width=True):
                    if 'chat_history' in st.session_state:
                        st.session_state.chat_history = []
                    st.success("✅ Historial limpio")
                    time.sleep(1)
                    st.rerun()
            
            with col2:
                if st.button("🔄 Nueva empresa", use_container_width=True):
                    st.session_state.datos_empresa = None
                    st.session_state.page_view = "form"
                    st.rerun()
            
            # CSS adicional para el sidebar
            st.markdown("""
                <style>
                    /* Sidebar específico */
                    .sidebar-header {
                        padding: 2rem 1rem;
                    }
                    
                    .logo-container {
                        display: flex;
                        align-items: center;
                        gap: 1rem;
                    }
                    
                    .logo {
                        font-size: 2.5rem;
                        width: 60px;
                        height: 60px;
                        background: linear-gradient(135deg, #10a37f, #2dd4bf);
                        border-radius: 12px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                    }
                    
                    .logo-text {
                        display: flex;
                        flex-direction: column;
                    }
                    
                    .brand-name {
                        font-size: 1.5rem;
                        font-weight: 700;
                        color: #f4f4f5;
                        letter-spacing: -0.02em;
                    }
                    
                    .brand-tagline {
                        font-size: 0.875rem;
                        color: #a1a1aa;
                    }
                    
                    .sidebar-divider {
                        height: 1px;
                        background-color: #27272a;
                        margin: 1.5rem 0;
                    }
                    
                    .nav-section {
                        padding: 0 1rem;
                        margin-bottom: 1rem;
                    }
                    
                    .nav-title {
                        font-size: 0.75rem;
                        font-weight: 600;
                        color: #71717a;
                        margin-bottom: 0.75rem;
                        letter-spacing: 0.05em;
                    }
                    
                    .company-status-card {
                        background-color: #1a1a1a;
                        border: 1px solid #27272a;
                        border-radius: 12px;
                        padding: 1rem;
                        margin: 0 1rem;
                        display: flex;
                        gap: 1rem;
                        align-items: center;
                    }
                    
                    .company-icon {
                        font-size: 2rem;
                        width: 48px;
                        height: 48px;
                        background-color: #262626;
                        border-radius: 8px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    }
                    
                    .company-info {
                        flex: 1;
                    }
                    
                    .company-name {
                        font-size: 1rem;
                        font-weight: 600;
                        color: #f4f4f5;
                        margin-bottom: 0.25rem;
                    }
                    
                    .status-badge {
                        font-size: 0.875rem;
                        font-weight: 500;
                        padding: 0.25rem 0.75rem;
                        border-radius: 9999px;
                        display: inline-block;
                    }
                    
                    .status-excellent {
                        background-color: rgba(34, 197, 94, 0.2);
                        color: #22c55e;
                    }
                    
                    .status-good {
                        background-color: rgba(59, 130, 246, 0.2);
                        color: #3b82f6;
                    }
                    
                    .status-regular {
                        background-color: rgba(250, 204, 21, 0.2);
                        color: #facc15;
                    }
                    
                    .status-critical {
                        background-color: rgba(220, 38, 38, 0.2);
                        color: #dc2626;
                    }
                </style>
            """, unsafe_allow_html=True)
    
    def render_header(self):
        """
        Renderiza un header moderno minimalista.
        """
        col1, col2, col3 = st.columns([1, 2, 1])
        
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
                    <h2 style="
                        margin: 1rem 0;
                        color: #10a37f;
                        font-weight: 600;
                        font-size: 1.5rem;
                    ">
                        {current_title}
                    </h2>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # Indicador de estado del modelo
            st.markdown("""
                <div style="text-align: right; padding: 1rem;">
                    <div style="
                        display: inline-flex;
                        align-items: center;
                        gap: 0.5rem;
                        background-color: #1a1a1a;
                        border: 1px solid #27272a;
                        border-radius: 9999px;
                        padding: 0.5rem 1rem;
                    ">
                        <div style="
                            width: 8px;
                            height: 8px;
                            background-color: #22c55e;
                            border-radius: 50%;
                            animation: pulse 2s ease-in-out infinite;
                        "></div>
                        <span style="
                            color: #a1a1aa;
                            font-size: 0.875rem;
                        ">IA Activa</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    def render_welcome_modern(self):
        """
        Renderiza la pantalla de bienvenida con diseño ultra moderno.
        """
        st.markdown("""
            <style>
                .welcome-container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 4rem 2rem;
                    text-align: center;
                }
                
                .welcome-content {
                    margin-bottom: 4rem;
                }
                
                .welcome-icon {
                    font-size: 5rem;
                    margin-bottom: 2rem;
                    display: inline-block;
                    animation: float 3s ease-in-out infinite;
                }
                
                @keyframes float {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-10px); }
                }
                
                .welcome-title {
                    font-size: 3rem;
                    font-weight: 700;
                    color: #f4f4f5;
                    margin-bottom: 1rem;
                    letter-spacing: -0.02em;
                }
                
                .welcome-subtitle {
                    font-size: 1.25rem;
                    color: #a1a1aa;
                    max-width: 600px;
                    margin: 0 auto;
                    line-height: 1.6;
                }
                
                .features-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 2rem;
                    margin-bottom: 4rem;
                }
                
                .feature-card {
                    background-color: #1a1a1a;
                    border: 1px solid #27272a;
                    border-radius: 16px;
                    padding: 2rem;
                    transition: all 0.2s ease;
                    cursor: default;
                }
                
                .feature-card:hover {
                    border-color: #10a37f;
                    transform: translateY(-4px);
                    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
                }
                
                .feature-icon {
                    font-size: 3rem;
                    margin-bottom: 1rem;
                }
                
                .feature-title {
                    font-size: 1.25rem;
                    font-weight: 600;
                    color: #f4f4f5;
                    margin-bottom: 0.5rem;
                }
                
                .feature-description {
                    font-size: 1rem;
                    color: #a1a1aa;
                    line-height: 1.5;
                }
                
                .welcome-actions {
                    display: flex;
                    gap: 1rem;
                    justify-content: center;
                    flex-wrap: wrap;
                }
            </style>
            
            <div class="welcome-container">
                <div class="welcome-content">
                    <div class="welcome-icon">🤖</div>
                    <h1 class="welcome-title">Bienvenido a FinanzGPT</h1>
                    <p class="welcome-subtitle">Tu asistente financiero inteligente potenciado por IA de última generación</p>
                </div>
                
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">📊</div>
                        <h3 class="feature-title">Análisis Inteligente</h3>
                        <p class="feature-description">Evaluación profunda de indicadores financieros con IA</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">💡</div>
                        <h3 class="feature-title">Recomendaciones</h3>
                        <p class="feature-description">Estrategias personalizadas para tu empresa</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">🚀</div>
                        <h3 class="feature-title">Crecimiento</h3>
                        <p class="feature-description">Planes de acción para maximizar resultados</p>
                    </div>
                </div>
                
                <div class="welcome-actions">
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            col_btn1, col_btn2 = st.columns(2)
            
            with col_btn1:
                if st.button("🚀 Comenzar Análisis", use_container_width=True):
                    st.session_state.page_view = "form"
                    st.rerun()
            
            with col_btn2:
                if st.button("💬 Ir al Chat", use_container_width=True):
                    st.session_state.page_view = "chat"
                    st.rerun()
        
        st.markdown("""
                </div>
            </div>
        """, unsafe_allow_html=True)
    
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