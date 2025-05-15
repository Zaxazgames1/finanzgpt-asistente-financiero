import streamlit as st
import re
import time
import matplotlib.pyplot as plt
import numpy as np

class ChatUI:
    """
    Interfaz de chat estilo Gemini con capacidad de mostrar gráficas.
    """
    def __init__(self, nlp_service, formatters, conversational_analyzer):
        """
        Inicializa la interfaz de chat.
        """
        self.nlp_service = nlp_service
        self.formatters = formatters
        self.conversational_analyzer = conversational_analyzer
        
        # Inicializar historial de chat
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        if 'thinking' not in st.session_state:
            st.session_state.thinking = False
        
        if 'mostrar_analisis' not in st.session_state:
            st.session_state.mostrar_analisis = False
            
        if 'mensaje_enviado' not in st.session_state:
            st.session_state.mensaje_enviado = False
    
    def renderizar_grafica_radar(self, resultados):
        """Renderiza la gráfica radar de indicadores"""
        # Configurar el estilo del gráfico para que coincida con Gemini
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), facecolor='#1E1F20')
        ax.set_facecolor('#1E1F20')
        
        # Normalizar valores para el gráfico
        endeudamiento_norm = 1 - min(1, resultados['indicadores']['ratio_endeudamiento'] / 1.0)
        rentabilidad_norm = min(1, resultados['indicadores']['rentabilidad'] / 0.3)
        
        # Para productividad, normalizar según sector
        sector_limites = {
            'Tecnología': 100000000,
            'Comercio': 50000000,
            'Manufactura': 70000000,
            'Servicios': 60000000,
            'Otro': 60000000
        }
        
        limite_prod = sector_limites.get(resultados['sector'], 60000000)
        productividad_norm = min(1, resultados['indicadores']['productividad'] / limite_prod)
        
        # Para rotación, menor es mejor (normalizar de forma inversa)
        rotacion_norm = 1 - min(1, resultados['indicadores']['rotacion_cartera'] / 90)
        
        # Datos para el gráfico
        categorias = ['Endeudamiento', 'Rentabilidad', 'Productividad', 'Rot. Cartera']
        valores = [endeudamiento_norm, rentabilidad_norm, productividad_norm, rotacion_norm]
        
        # Completar el círculo repitiendo el primer valor
        valores += [valores[0]]
        categorias += [categorias[0]]
        
        # Configuración estética
        N = len(categorias) - 1
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += [angles[0]]  # Cerrar el círculo
        
        # Dibujar los ejes y el gráfico con colores estilo Gemini
        ax.plot(angles, valores, linewidth=2.5, linestyle='solid', color='#00A1F1')
        ax.fill(angles, valores, alpha=0.3, color='#00A1F1')
        
        # Agregar etiquetas con mejor formato
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categorias[:-1], size=12, color='#E5E5E5')
        
        # Mejorar las líneas de la cuadrícula
        ax.set_rlabel_position(0)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], color="#B8BCC8", size=10)
        ax.set_ylim(0, 1)
        ax.grid(True, color='#3C3F41', linewidth=0.5, alpha=0.7)
        
        # Agregar título
        plt.title('Perfil Económico de la Empresa', size=16, color='#E5E5E5', pad=20, fontweight='500')
        
        return fig
    
    def renderizar_resultados_en_chat(self, resultados):
        """Renderiza los resultados del análisis directamente en el chat"""
        # Estado general
        estado = resultados['estado_general'].lower()
        estado_emoji = '🟢' if estado in ['excelente', 'bueno'] else '🟡' if estado == 'regular' else '🔴'
        
        mensaje_resultado = f"""# 📊 Análisis Financiero Completo - {resultados['nombre']}

## Estado General: {resultados['estado_general']} {estado_emoji}

Tu empresa del sector **{resultados['sector']}** presenta el siguiente perfil financiero:

### 📈 Indicadores Clave

**⚖️ Ratio de Endeudamiento:** {resultados['indicadores']['ratio_endeudamiento']:.2f}
- Evaluación: {resultados['evaluacion']['endeudamiento']}
- {'✅ Saludable' if resultados['evaluacion']['endeudamiento'] == 'bueno' else '⚠️ Requiere atención'}

**💰 Rentabilidad (ROA):** {resultados['indicadores']['rentabilidad']:.2%}
- Evaluación: {resultados['evaluacion']['rentabilidad']}
- {'✅ Excelente' if resultados['evaluacion']['rentabilidad'] == 'buena' else '⚠️ Bajo potencial'}

**👥 Productividad:** ${resultados['indicadores']['productividad']:,.0f} por empleado
- Evaluación: {resultados['evaluacion']['productividad']}
- {'✅ Alta eficiencia' if resultados['evaluacion']['productividad'] == 'buena' else '⚠️ Puede mejorar'}

**📅 Rotación de Cartera:** {resultados['indicadores']['rotacion_cartera']:.1f} días
- Evaluación: {resultados['evaluacion']['rotacion']}
- {'✅ Buen flujo' if resultados['evaluacion']['rotacion'] == 'buena' else '⚠️ Ciclo largo'}

### 💡 Recomendaciones Principales

"""
        
        # Agregar recomendaciones
        for i, rec in enumerate(resultados['recomendaciones'], 1):
            mensaje_resultado += f"{i}. {rec}\n"
        
        # Agregar el mensaje al historial
        st.session_state.chat_history.append(("bot", mensaje_resultado))
        
        # Agregar la gráfica como un mensaje especial
        st.session_state.chat_history.append(("bot", "GRAFICA_RADAR"))
        
        # Mensaje final
        mensaje_final = """
¿Te gustaría que profundice en algún indicador específico? Puedo explicarte:
- Estrategias detalladas para mejorar cada indicador
- Comparación con empresas del sector
- Proyecciones a futuro
- Plan de acción paso a paso

¿Qué aspecto te interesa más?"""
        
        st.session_state.chat_history.append(("bot", mensaje_final))
    
    def chatbot_response(self, mensaje, datos_empresa=None):
        """
        Genera respuestas usando el modelo Gemini o el analizador conversacional.
        """
        # Si hay un análisis en curso, usar el analizador conversacional
        estado_conversacion = st.session_state.get('estado_conversacion', 'inicio')
        
        # Procesar respuesta
        respuesta = None
        
        if estado_conversacion == 'completado' and st.session_state.get('mostrar_analisis', False):
            # Si hay que mostrar análisis, hacerlo inmediatamente
            st.session_state.mostrar_analisis = False
            self.renderizar_resultados_en_chat(st.session_state.datos_empresa['resultados'])
            return None
        elif estado_conversacion != 'completado' and estado_conversacion != 'inicio':
            respuesta = self.conversational_analyzer.procesar_respuesta(mensaje)
        else:
            # Verificar si el usuario quiere iniciar un análisis
            if self.conversational_analyzer.detectar_intencion_analisis(mensaje):
                respuesta = self.conversational_analyzer.procesar_respuesta(mensaje)
            else:
                # Usar el servicio NLP normal
                respuesta = self.nlp_service.generar_respuesta_chat(mensaje, datos_empresa)
        
        return respuesta
    
    def renderizar_chat(self, datos_empresa=None):
        """
        Renderiza la interfaz del chat estilo Gemini.
        """
        # CSS específico para el chat
        st.markdown(self.get_chat_css(), unsafe_allow_html=True)
        
        # Header del chat
        st.markdown("""
            <div class="chat-header">
                <div class="chat-title">
                    <span>🤖</span>
                    FinanzGPT - Asistente Financiero
                </div>
                <div class="chat-actions">
                    <button class="canvas-button">📊 Canvas</button>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Contenedor del chat
        chat_container = st.container()
        
        with chat_container:
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            
            # Mensaje de bienvenida si el chat está vacío
            if not st.session_state.chat_history:
                # Mensaje de bienvenida
                st.markdown("""
                    <div class="welcome-message">
                        <div class="icon">🤖</div>
                        <h2>Hola, soy FinanzGPT</h2>
                        <p>Tu asistente financiero inteligente impulsado por Gemini 2.0</p>
                    </div>
                    
                    <div class="capabilities-grid">
                        <div class="capability-card">
                            <span class="capability-icon">📊</span>
                            <div class="capability-text">
                                <strong>Análisis Financiero</strong>
                                <p>Evalúa la salud financiera de tu empresa con indicadores clave</p>
                            </div>
                        </div>
                        <div class="capability-card">
                            <span class="capability-icon">📈</span>
                            <div class="capability-text">
                                <strong>Visualizaciones</strong>
                                <p>Gráficas claras y fáciles de entender</p>
                            </div>
                        </div>
                        <div class="capability-card">
                            <span class="capability-icon">💡</span>
                            <div class="capability-text">
                                <strong>Recomendaciones</strong>
                                <p>Consejos personalizados para tu sector</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="main-cta">
                        <div class="cta-icon">🎯</div>
                        <div class="cta-text">
                            <h3>¿Listo para analizar tu empresa?</h3>
                            <p>Solo necesito 7 datos básicos para generar un análisis completo</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botones de sugerencias - Fuera del HTML para que funcionen
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    if st.button("🏢 Iniciar análisis de mi empresa", key="btn1", use_container_width=True):
                        st.session_state.chat_history.append(("user", "Quiero analizar mi empresa"))
                        st.session_state.mensaje_enviado = True
                        st.rerun()
                
                with col2:
                    if st.button("📊 Analizar situación financiera", key="btn2", use_container_width=True):
                        st.session_state.chat_history.append(("user", "Necesito analizar mi situación financiera"))
                        st.session_state.mensaje_enviado = True
                        st.rerun()
                
                with col3:
                    if st.button("💰 Evaluar indicadores clave", key="btn3", use_container_width=True):
                        st.session_state.chat_history.append(("user", "Quiero evaluar mis indicadores financieros"))
                        st.session_state.mensaje_enviado = True
                        st.rerun()
                
                with col4:
                    if st.button("🤔 ¿Cómo funciona?", key="btn4", use_container_width=True):
                        st.session_state.chat_history.append(("user", "¿Cómo funciona el análisis?"))
                        st.session_state.mensaje_enviado = True
                        st.rerun()
            
            # Mostrar historial
            for i, (sender, message) in enumerate(st.session_state.chat_history):
                if sender == "user":
                    st.markdown(f"""
                        <div class="chat-message-user">
                            <div class="message-content">
                                {self._escape_html(message)}
                            </div>
                            <div class="avatar avatar-user">👤</div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    if message == "GRAFICA_RADAR" and 'datos_empresa' in st.session_state:
                        # Mostrar gráfica radar
                        st.markdown("""
                            <div class="chat-message-bot">
                                <div class="avatar avatar-bot">🤖</div>
                                <div style="flex: 1;">
                        """, unsafe_allow_html=True)
                        
                        fig = self.renderizar_grafica_radar(st.session_state.datos_empresa['resultados'])
                        st.pyplot(fig)
                        
                        st.markdown("""
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        # Header del bot
                        st.markdown("""
                            <div class="chat-message-bot">
                                <div class="avatar avatar-bot">🤖</div>
                                <div style="flex: 1;">
                                    <div class="bot-header">
                                        <span class="bot-name">FinanzGPT</span>
                                        <span>•</span>
                                        <span>2.0 Flash</span>
                                    </div>
                                    <div class="message-content">
                        """, unsafe_allow_html=True)
                        
                        # Contenido formateado
                        formatted_message = self._format_message(message)
                        st.markdown(formatted_message, unsafe_allow_html=True)
                        
                        # Acciones del mensaje
                        st.markdown("""
                                    </div>
                                    <div class="message-actions">
                        """, unsafe_allow_html=True)
                        
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            if st.button("👍", key=f"like_{i}"):
                                st.toast("¡Gracias por tu feedback!", icon="👍")
                        with col2:
                            if st.button("👎", key=f"dislike_{i}"):
                                st.toast("Gracias por tu feedback, mejoraremos", icon="👎")
                        with col3:
                            if st.button("📋", key=f"copy_{i}_btn"):
                                st.toast("Copiado al portapapeles", icon="📋")
                        with col4:
                            if st.button("🔄", key=f"regen_{i}_btn"):
                                st.session_state.thinking = True
                                st.rerun()
                        
                        st.markdown("""
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
            
            # Botón de emergencia para forzar el análisis
            if st.session_state.get('estado_conversacion') == 'completado' and 'datos_empresa' in st.session_state:
                if st.button("📊 Ver resultados del análisis", key="force_results", type="primary", use_container_width=True):
                    self.renderizar_resultados_en_chat(st.session_state.datos_empresa['resultados'])
                    st.rerun()
            
            # Animación de pensamiento
            if st.session_state.thinking:
                # Timeout de seguridad
                if 'thinking_start' not in st.session_state:
                    st.session_state.thinking_start = time.time()
                
                # Si lleva más de 5 segundos pensando, forzar resultado
                if time.time() - st.session_state.thinking_start > 5:
                    st.session_state.thinking = False
                    st.session_state.thinking_start = None
                    if st.session_state.get('mostrar_analisis', False):
                        st.session_state.mostrar_analisis = False
                        self.renderizar_resultados_en_chat(st.session_state.datos_empresa['resultados'])
                    st.rerun()
                
                st.markdown("""
                    <div class="thinking-indicator">
                        <div class="avatar avatar-bot">🤖</div>
                        <div class="thinking-bubble">
                            <div class="thinking-dot"></div>
                            <div class="thinking-dot"></div>
                            <div class="thinking-dot"></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Si el estado es análisis, mostrar mensaje especial
                if st.session_state.get('estado_conversacion') == 'analisis':
                    time.sleep(2)  # Simular análisis
                    st.session_state.thinking = False
                    st.session_state.mostrar_analisis = True
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Espacio antes del input
        st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True)
        
        # Input del chat - AHORA FUERA DE CUALQUIER CONTENEDOR
        mensaje_usuario = st.chat_input("Pregunta a FinanzGPT...")
        
        if mensaje_usuario:
            # Agregar mensaje al historial
            st.session_state.chat_history.append(("user", mensaje_usuario))
            st.session_state.mensaje_enviado = True
            st.rerun()
        
        # Procesar mensaje cuando se envió
        if st.session_state.mensaje_enviado and st.session_state.chat_history:
            # Activar animación de pensamiento
            st.session_state.thinking = True
            st.session_state.mensaje_enviado = False
            
            # Obtener último mensaje
            ultimo_mensaje = st.session_state.chat_history[-1][1]
            
            # Generar respuesta
            respuesta = self.chatbot_response(ultimo_mensaje, datos_empresa)
            
            # Solo agregar respuesta si existe
            if respuesta:
                st.session_state.chat_history.append(("bot", respuesta))
            
            # Si se debe mostrar análisis, hacerlo ahora
            if st.session_state.get('mostrar_analisis', False):
                st.session_state.mostrar_analisis = False
                self.renderizar_resultados_en_chat(st.session_state.datos_empresa['resultados'])
            
            # Desactivar animación
            st.session_state.thinking = False
            
            # Actualizar
            st.rerun()
    
    def _escape_html(self, text):
        """Escapa HTML para evitar problemas de seguridad."""
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    def _format_message(self, message):
        """Formatea el mensaje para mejor presentación."""
        # Si el mensaje ya contiene HTML no procesarlo
        if '<' in message and '>' in message:
            return message
            
        # Escapar HTML primero
        message = self._escape_html(message)
        
        # Formatear headers
        message = re.sub(r'^#{4}\s+(.+)$', r'<h4>\1</h4>', message, flags=re.MULTILINE)
        message = re.sub(r'^#{3}\s+(.+)$', r'<h3>\1</h3>', message, flags=re.MULTILINE)
        message = re.sub(r'^#{2}\s+(.+)$', r'<h2>\1</h2>', message, flags=re.MULTILINE)
        message = re.sub(r'^#{1}\s+(.+)$', r'<h1>\1</h1>', message, flags=re.MULTILINE)
        
        # Formatear negritas y cursivas
        message = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', message)
        message = re.sub(r'\*(.+?)\*', r'<em>\1</em>', message)
        
        # Formatear listas
        message = re.sub(r'^[\*\-•]\s+(.+)$', r'<li>\1</li>', message, flags=re.MULTILINE)
        
        # Agrupar elementos li en ul
        lines = message.split('\n')
        new_lines = []
        in_list = False
        
        for line in lines:
            if '<li>' in line:
                if not in_list:
                    new_lines.append('<ul>')
                    in_list = True
                new_lines.append(line)
            else:
                if in_list:
                    new_lines.append('</ul>')
                    in_list = False
                new_lines.append(line)
        
        if in_list:
            new_lines.append('</ul>')
        
        message = '\n'.join(new_lines)
        
        # Formatear párrafos
        paragraphs = message.split('\n\n')
        formatted_paragraphs = []
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if paragraph:
                if not paragraph.startswith('<'):
                    paragraph = f'<p>{paragraph}</p>'
                paragraph = paragraph.replace('\n', '<br>')
                formatted_paragraphs.append(paragraph)
        
        return '\n'.join(formatted_paragraphs)
    
    def get_chat_css(self):
        """Retorna el CSS específico para el chat"""
        return """
            <style>
                /* Estilos para el chat */
                .stApp > header {
                    display: none !important;
                }
                
                section[data-testid="stMain"] > div:first-child {
                    overflow: visible !important;
                }
                
                .chat-header {
                    background-color: var(--bg-primary);
                    border-bottom: 1px solid var(--border-color);
                    padding: 1rem 2rem;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    position: sticky;
                    top: 0;
                    z-index: 100;
                }
                
                .chat-title {
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                    font-size: 1.25rem;
                    font-weight: 500;
                    color: var(--text-primary);
                }
                
                .chat-container {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 2rem;
                    padding-bottom: 20px; /* Menos padding abajo */
                }
                
                .welcome-message {
                    text-align: center;
                    padding: 3rem 0 2rem 0;
                    max-width: 700px;
                    margin: 0 auto;
                }
                
                .welcome-message .icon {
                    font-size: 4rem;
                    margin-bottom: 1.5rem;
                    background: linear-gradient(135deg, #FA8B00, #8B00FA);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
                
                .welcome-message h2 {
                    font-size: 2.5rem;
                    font-weight: 500;
                    color: var(--text-primary);
                    margin-bottom: 0.5rem;
                }
                
                .welcome-message p {
                    font-size: 1.25rem;
                    color: var(--text-secondary);
                    margin-bottom: 3rem;
                }
                
                .capabilities-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 2rem;
                    margin: 3rem auto;
                    max-width: 1000px;
                }
                
                .capability-card {
                    background: var(--bg-tertiary);
                    border: 1px solid var(--border-color);
                    border-radius: var(--radius-lg);
                    padding: 2rem;
                    display: flex;
                    gap: 1.5rem;
                    transition: var(--transition);
                    cursor: pointer;
                }
                
                .capability-card:hover {
                    border-color: var(--accent-blue);
                    transform: translateY(-4px);
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                }
                
                .capability-icon {
                    font-size: 2.5rem;
                    flex-shrink: 0;
                }
                
                .capability-text strong {
                    display: block;
                    color: var(--text-primary);
                    font-size: 1.125rem;
                    margin-bottom: 0.5rem;
                    font-weight: 500;
                }
                
                .capability-text p {
                    color: var(--text-secondary);
                    font-size: 0.875rem;
                    line-height: 1.5;
                    margin: 0;
                }
                
                .main-cta {
                    background: linear-gradient(135deg, rgba(250, 139, 0, 0.1), rgba(139, 0, 250, 0.1));
                    border: 2px solid rgba(250, 139, 0, 0.3);
                    border-radius: var(--radius-xl);
                    padding: 2.5rem;
                    margin: 3rem auto;
                    max-width: 700px;
                    display: flex;
                    align-items: center;
                    gap: 2rem;
                    transition: var(--transition);
                }
                
                .main-cta:hover {
                    border-color: rgba(250, 139, 0, 0.6);
                    background: linear-gradient(135deg, rgba(250, 139, 0, 0.15), rgba(139, 0, 250, 0.15));
                }
                
                .cta-icon {
                    font-size: 3.5rem;
                    background: linear-gradient(135deg, #FA8B00, #8B00FA);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
                
                .cta-text h3 {
                    margin: 0 0 0.5rem 0;
                    color: var(--text-primary);
                    font-size: 1.75rem;
                    font-weight: 500;
                }
                
                .cta-text p {
                    margin: 0;
                    color: var(--text-secondary);
                    font-size: 1.125rem;
                }
                
                /* Botones de sugerencias */
                .stButton > button {
                    background-color: var(--bg-tertiary);
                    border: 1px solid var(--border-color);
                    color: var(--text-primary);
                    padding: 0.875rem 1.5rem;
                    border-radius: var(--radius-md);
                    font-size: 0.875rem;
                    font-weight: 400;
                    transition: var(--transition);
                    width: 100%;
                    text-align: center;
                    cursor: pointer;
                }
                
                .stButton > button:hover {
                    background-color: var(--bg-input);
                    border-color: var(--accent-blue);
                    color: var(--accent-blue);
                    transform: translateY(-2px);
                }
                
                /* Mensajes del chat */
                .chat-message-user,
                .chat-message-bot {
                    display: flex;
                    gap: 1rem;
                    margin-bottom: 2rem;
                    max-width: 100%;
                }
                
                .chat-message-user {
                    flex-direction: row-reverse;
                }
                
                .message-content {
                    max-width: 70%;
                    word-wrap: break-word;
                }
                
                .chat-message-user .message-content {
                    background-color: var(--bg-tertiary);
                    color: var(--text-primary);
                    padding: 1rem 1.5rem;
                    border-radius: var(--radius-lg);
                    border: 1px solid var(--border-color);
                }
                
                .chat-message-bot .message-content {
                    background-color: transparent;
                    color: var(--text-primary);
                }
                
                /* Avatars */
                .avatar {
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1rem;
                    flex-shrink: 0;
                }
                
                .avatar-user {
                    background-color: var(--bg-tertiary);
                    border: 1px solid var(--border-color);
                }
                
                .avatar-bot {
                    background: linear-gradient(135deg, #FA8B00, #8B00FA);
                    color: white;
                    .avatar-bot {
                    background: linear-gradient(135deg, #FA8B00, #8B00FA);
                    color: white;
                }
                
                .bot-header {
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                    margin-bottom: 0.5rem;
                    color: var(--text-secondary);
                    font-size: 0.875rem;
                }
                
                .bot-header .bot-name {
                    font-weight: 500;
                    color: var(--text-primary);
                }
                
                .message-actions {
                    display: flex;
                    gap: 0.5rem;
                    margin-top: 0.75rem;
                    padding-top: 0.75rem;
                    border-top: 1px solid var(--border-color);
                }
                
                /* Thinking animation */
                .thinking-indicator {
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    margin-bottom: 1.5rem;
                }
                
                .thinking-bubble {
                    display: flex;
                    gap: 0.3rem;
                    align-items: center;
                }
                
                .thinking-dot {
                    width: 8px;
                    height: 8px;
                    background-color: var(--text-muted);
                    border-radius: 50%;
                    animation: thinking 1.4s ease-in-out infinite;
                }
                
                .thinking-dot:nth-child(1) { animation-delay: 0s; }
                .thinking-dot:nth-child(2) { animation-delay: 0.2s; }
                .thinking-dot:nth-child(3) { animation-delay: 0.4s; }
                
                @keyframes thinking {
                    0%, 60%, 100% {
                        transform: translateY(0);
                        opacity: 0.4;
                    }
                    30% {
                        transform: translateY(-10px);
                        opacity: 1;
                    }
                }
                
                /* Canvas button */
                .canvas-button {
                    background-color: var(--bg-tertiary);
                    border: 1px solid var(--border-color);
                    border-radius: var(--radius-md);
                    padding: 0.5rem 1rem;
                    color: var(--text-secondary);
                    font-size: 0.875rem;
                    cursor: pointer;
                    transition: var(--transition);
                }
                
                .canvas-button:hover {
                    background-color: var(--bg-input);
                    color: var(--text-primary);
                    border-color: var(--text-muted);
                }
                
                /* AJUSTE ESPECIAL PARA EL CHAT INPUT */
                div[data-testid="stChatInputContainer"] {
                    position: fixed !important;
                    bottom: 0 !important;
                    left: 0 !important;
                    right: 0 !important;
                    background-color: var(--bg-primary) !important;
                    padding: 1rem 2rem 1.5rem 2rem !important;
                    border-top: 1px solid var(--border-color) !important;
                    z-index: 1000 !important;
                }
                
                div[data-testid="stChatInputContainer"] > div {
                    max-width: 1200px !important;
                    margin: 0 auto !important;
                }
                
                div[data-testid="stChatInput"] {
                    border: 1px solid var(--border-color) !important;
                    border-radius: 28px !important;
                    background-color: var(--bg-input) !important;
                    overflow: hidden !important;
                }
                
                div[data-testid="stChatInput"] > textarea {
                    background-color: transparent !important;
                    border: none !important;
                    color: var(--text-primary) !important;
                    font-size: 1rem !important;
                    padding: 0.75rem 1.25rem !important;
                    line-height: 1.5 !important;
                    min-height: 44px !important;
                    max-height: 200px !important;
                }
                
                div[data-testid="stChatInput"] > textarea:focus {
                    outline: none !important;
                    box-shadow: none !important;
                }
                
                div[data-testid="stChatInput"] > textarea::placeholder {
                    color: var(--text-muted) !important;
                }
                
                /* Botón de enviar del chat */
                div[data-testid="stChatInput"] button {
                    background-color: transparent !important;
                    border: none !important;
                    color: var(--text-secondary) !important;
                    padding: 0.5rem !important;
                    cursor: pointer !important;
                }
                
                div[data-testid="stChatInput"] button:hover {
                    color: var(--accent-blue) !important;
                }
                
                /* Ajuste del contenedor principal para evitar que el contenido quede detrás del input */
                .main > div {
                    padding-bottom: 80px !important;
                }
                
                /* Estilos para el botón de emergencia */
                button[data-testid="baseButton-primary"] {
                    background: linear-gradient(135deg, #FA8B00, #8B00FA) !important;
                    border: none !important;
                    color: white !important;
                    font-weight: 500 !important;
                    padding: 0.75rem 1.5rem !important;
                    border-radius: var(--radius-md) !important;
                    transition: var(--transition) !important;
                    transform: scale(1) !important;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
                }
                
                button[data-testid="baseButton-primary"]:hover {
                    transform: translateY(-2px) scale(1.02) !important;
                    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3) !important;
                }
                
                /* Animación de entrada */
                @keyframes fadeIn {
                    from {
                        opacity: 0;
                        transform: translateY(10px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                
                .chat-message-user,
                .chat-message-bot {
                    animation: fadeIn 0.3s ease-out;
                }
                
                /* Responsive */
                @media (max-width: 768px) {
                    .capabilities-grid {
                        grid-template-columns: 1fr;
                        gap: 1rem;
                    }
                    
                    .main-cta {
                        flex-direction: column;
                        text-align: center;
                        padding: 2rem;
                        gap: 1.5rem;
                    }
                    
                    .message-content {
                        max-width: 85%;
                    }
                    
                    .chat-container {
                        padding: 1rem;
                        padding-bottom: 10px;
                    }
                    
                    .chat-header {
                        padding: 1rem;
                    }
                    
                    .welcome-message h2 {
                        font-size: 2rem;
                    }
                    
                    .cta-text h3 {
                        font-size: 1.5rem;
                    }
                    
                    div[data-testid="stChatInputContainer"] {
                        padding: 0.75rem 1rem 1rem 1rem !important;
                    }
                }
                
                @media (max-width: 480px) {
                    .stButton > button {
                        padding: 0.75rem 1rem;
                        font-size: 0.8rem;
                    }
                    
                    .capability-card {
                        padding: 1.5rem;
                    }
                    
                    .cta-icon {
                        font-size: 2.5rem;
                    }
                    
                    .welcome-message .icon {
                        font-size: 3rem;
                    }
                }
            </style>
        """