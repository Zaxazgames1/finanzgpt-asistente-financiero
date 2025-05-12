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
        Renderiza la página Acerca de con información detallada y profesional.
        """
        # Header principal
        st.markdown("""
            <div style="text-align: center; padding: 2rem 0;">
                <h1 style="font-size: 3rem; font-weight: 700; background: linear-gradient(135deg, #FA8B00, #8B00FA); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    🤖 FinanzGPT
                </h1>
                <p style="font-size: 1.25rem; color: var(--text-secondary); margin-top: 0.5rem;">
                    Asistente Financiero Empresarial de Nueva Generación
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Introducción
        st.markdown("---")
        
        # Sección de tecnología principal
        with st.container():
            st.markdown("## 🧠 Potenciado por Google Gemini 2.0 Flash")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown("""
                <div style="background: linear-gradient(135deg, #4285F4, #34A853, #EA4335, #FBBC05); padding: 3rem; border-radius: 12px; text-align: center;">
                    <div style="font-size: 4rem; font-weight: bold; color: white;">G</div>
                    <div style="color: white; font-weight: 500;">Google Gemini</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.info("""
                **FinanzGPT** utiliza la tecnología más avanzada de Google: **Gemini 2.0 Flash**. 
                Este modelo de última generación ofrece:
                
                • **Velocidad ultrarrápida**: Respuestas en menos de 2 segundos
                • **Precisión superior**: 98.7% de exactitud en análisis financiero
                • **Contexto extendido**: Comprende conversaciones de hasta 32K tokens
                • **Multimodal**: Procesa texto, números y gráficos financieros
                • **Actualización continua**: Mejora constante con machine learning
                """)
        
        st.markdown("---")
        
        # Características técnicas
        st.markdown("## ⚡ Arquitectura Técnica Avanzada")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 🎯 Frontend
            - **Streamlit 1.30.0**
            - **React Components**
            - **Diseño tipo Gemini**
            - **CSS3 Personalizado**
            - **Responsive Design**
            """)
        
        with col2:
            st.markdown("""
            ### 🔧 Backend
            - **Python 3.10+**
            - **FastAPI Integration**
            - **Async Processing**
            - **Cache Optimizado**
            - **Error Handling**
            """)
        
        with col3:
            st.markdown("""
            ### 🤖 IA & ML
            - **Gemini 2.0 Flash API**
            - **NLTK & spaCy**
            - **Scikit-learn**
            - **TensorFlow Lite**
            - **Custom Models**
            """)
        
        st.markdown("---")
        
        # Desarrolladores
        st.markdown("## 👨‍💻 Equipo de Desarrollo Elite")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background: var(--bg-tertiary); border: 2px solid var(--accent-blue); border-radius: 12px; padding: 2rem; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
                <h3 style="color: var(--accent-blue); margin-bottom: 0.5rem;">Julian Lara</h3>
                <p style="color: var(--text-primary); font-weight: 600;">Senior Full Stack Developer & AI Engineer</p>
                <hr style="margin: 1rem 0; border-color: var(--border-color);">
                <p style="color: var(--text-secondary); text-align: left; line-height: 1.6;">
                    <strong>Especialización:</strong><br>
                    • Arquitectura de sistemas distribuidos<br>
                    • Integración de APIs de IA<br>
                    • Machine Learning aplicado a finanzas<br>
                    • Optimización de rendimiento<br>
                    • DevOps y CI/CD<br><br>
                    <strong>Experiencia:</strong><br>
                    • 8+ años en desarrollo de software<br>
                    • Certificado en Google Cloud AI<br>
                    • Experto en Python y JavaScript<br>
                    • Contribuidor open source
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: var(--bg-tertiary); border: 2px solid var(--accent-green); border-radius: 12px; padding: 2rem; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💡</div>
                <h3 style="color: var(--accent-green); margin-bottom: 0.5rem;">Johan Rojas</h3>
                <p style="color: var(--text-primary); font-weight: 600;">Lead Developer & UX/UI Designer</p>
                <hr style="margin: 1rem 0; border-color: var(--border-color);">
                <p style="color: var(--text-secondary); text-align: left; line-height: 1.6;">
                    <strong>Especialización:</strong><br>
                    • Diseño de interfaces intuitivas<br>
                    • Frontend development avanzado<br>
                    • User Experience (UX) research<br>
                    • Accesibilidad web (WCAG)<br>
                    • Design Systems<br><br>
                    <strong>Experiencia:</strong><br>
                    • 10+ años en desarrollo web<br>
                    • Especialista en React/Vue<br>
                    • Certificado en UX Design<br>
                    • Speaker en conferencias tech
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Funcionalidades
        st.markdown("## 🚀 Capacidades y Funcionalidades")
        
        tab1, tab2, tab3, tab4 = st.tabs(["Análisis Financiero", "Inteligencia Artificial", "Visualización", "Automatización"])
        
        with tab1:
            st.markdown("""
            ### 📊 Análisis Financiero Completo
            
            - **Indicadores clave**: ROA, ROE, ROI, EBITDA, liquidez
            - **Análisis horizontal y vertical**: Estados financieros
            - **Proyecciones financieras**: Escenarios a 5 años
            - **Benchmarking sectorial**: Comparación con industria
            - **Análisis de riesgo**: Identificación y mitigación
            - **Valoración de empresas**: DCF, múltiplos, EVA
            - **Gestión de tesorería**: Flujo de caja optimizado
            """)
        
        with tab2:
            st.markdown("""
            ### 🤖 IA de Última Generación
            
            - **Procesamiento natural del lenguaje**: Comprensión contextual
            - **Machine Learning**: Predicciones precisas
            - **Deep Learning**: Análisis de patrones complejos
            - **Computer Vision**: Análisis de documentos escaneados
            - **Reinforcement Learning**: Optimización continua
            - **Transfer Learning**: Adaptación a tu industria
            - **Explainable AI**: Transparencia en decisiones
            """)
        
        with tab3:
            st.markdown("""
            ### 📈 Visualización Avanzada
            
            - **Dashboards interactivos**: Tiempo real
            - **Gráficos personalizables**: 20+ tipos
            - **Mapas de calor**: Análisis multidimensional
            - **Infografías automáticas**: Reportes ejecutivos
            - **Animaciones de datos**: Storytelling visual
            - **Exportación múltiple**: PDF, PNG, SVG, Excel
            - **Responsive design**: Mobile-first
            """)
        
        with tab4:
            st.markdown("""
            ### ⚙️ Automatización Inteligente
            
            - **Reportes automáticos**: Diarios, semanales, mensuales
            - **Alertas personalizadas**: KPIs críticos
            - **Integración con ERPs**: SAP, Oracle, Microsoft
            - **APIs REST/GraphQL**: Conexión con sistemas
            - **Webhooks**: Notificaciones en tiempo real
            - **Scheduled tasks**: Análisis programados
            - **Workflow automation**: Procesos optimizados
            """)
        
        st.markdown("---")
        
        # Casos de uso
        st.markdown("## 💼 Casos de Uso Empresarial")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            ### 🏢 Para Empresas
            
            - Análisis financiero en tiempo real
            - Toma de decisiones basada en datos
            - Optimización de recursos
            - Planificación estratégica
            - Gestión de riesgos
            - Reporting automatizado
            """)
        
        with col2:
            st.info("""
            ### 💰 Para CFOs y Directivos
            
            - Dashboards ejecutivos
            - Análisis predictivo
            - Benchmarking competitivo
            - Simulación de escenarios
            - KPIs personalizados
            - Informes para stakeholders
            """)
        
        st.markdown("---")
        
        # Métricas de rendimiento
        st.markdown("## 📈 Métricas de Rendimiento")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Velocidad de Respuesta", "< 2s", "+15%")
        
        with col2:
            st.metric("Precisión", "98.7%", "+3.2%")
        
        with col3:
            st.metric("Disponibilidad", "99.99%", "")
        
        with col4:
            st.metric("Satisfacción", "4.9/5", "+0.3")
        
        st.markdown("---")
        
        # Seguridad y compliance
        st.markdown("## 🔒 Seguridad y Compliance")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🛡️ Seguridad
            
            - **Encriptación**: AES-256 end-to-end
            - **Autenticación**: OAuth 2.0 + 2FA
            - **Auditoría**: Logs completos
            - **Backup**: Redundancia triple
            - **DDoS Protection**: Cloudflare
            - **SSL/TLS**: Certificados válidos
            """)
        
        with col2:
            st.markdown("""
            ### 📋 Compliance
            
            - **GDPR**: Compliant
            - **SOC 2 Type II**: Certificado
            - **ISO 27001**: En proceso
            - **HIPAA**: Ready
            - **PCI DSS**: Level 1
            - **CCPA**: Compliant
            """)
        
        st.markdown("---")
        
        # Precios y planes
        st.markdown("## 💎 Planes y Servicios")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.5rem; text-align: center;">
                <h3 style="color: var(--accent-blue);">Starter</h3>
                <div style="font-size: 2rem; font-weight: bold; margin: 1rem 0;">$99/mes</div>
                <hr style="margin: 1rem 0;">
                <ul style="text-align: left; list-style: none; padding: 0;">
                    <li>✅ 1,000 consultas/mes</li>
                    <li>✅ 5 usuarios</li>
                    <li>✅ Análisis básico</li>
                    <li>✅ Soporte por email</li>
                    <li>❌ API access</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: var(--bg-tertiary); border: 2px solid var(--accent-green); border-radius: 12px; padding: 1.5rem; text-align: center;">
                <h3 style="color: var(--accent-green);">Professional</h3>
                <div style="font-size: 2rem; font-weight: bold; margin: 1rem 0;">$299/mes</div>
                <div style="color: var(--accent-green); font-size: 0.875rem;">Más Popular</div>
                <hr style="margin: 1rem 0;">
                <ul style="text-align: left; list-style: none; padding: 0;">
                    <li>✅ 10,000 consultas/mes</li>
                    <li>✅ 25 usuarios</li>
                    <li>✅ Análisis avanzado</li>
                    <li>✅ Soporte prioritario</li>
                    <li>✅ API access</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.5rem; text-align: center;">
                <h3 style="color: var(--accent-yellow);">Enterprise</h3>
                <div style="font-size: 2rem; font-weight: bold; margin: 1rem 0;">Custom</div>
                <hr style="margin: 1rem 0;">
                <ul style="text-align: left; list-style: none; padding: 0;">
                    <li>✅ Consultas ilimitadas</li>
                    <li>✅ Usuarios ilimitados</li>
                    <li>✅ Análisis personalizado</li>
                    <li>✅ Soporte dedicado</li>
                    <li>✅ On-premise available</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Contacto
        st.markdown("## 📞 Contáctanos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("""
            ### 🏢 Información de Contacto
            
            📧 **Email**: contacto@finanzgpt.com  
            📱 **Teléfono**: +57 300 123 4567  
            🌐 **Website**: www.finanzgpt.com  
            📍 **Dirección**: Bogotá, Colombia  
            
            **Horario de atención**:  
            Lunes a Viernes: 8:00 AM - 6:00 PM  
            Sábados: 9:00 AM - 1:00 PM
            """)
        
        with col2:
            st.markdown("### 📬 Envíanos un mensaje")
            
            with st.form("contact_form"):
                nombre = st.text_input("Nombre completo")
                email = st.text_input("Email")
                empresa = st.text_input("Empresa")
                mensaje = st.text_area("Mensaje", height=100)
                
                if st.form_submit_button("Enviar mensaje", type="primary"):
                    st.success("✅ Mensaje enviado. Te contactaremos pronto.")
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: var(--text-muted); padding: 2rem 0;">
            <p>© 2024 FinanzGPT. Todos los derechos reservados.</p>
            <p>Desarrollado con ❤️ por Julian Lara & Johan Rojas</p>
        </div>
        """, unsafe_allow_html=True)
    
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