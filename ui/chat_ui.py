import streamlit as st
import re
import time

class ChatUI:
    """
    Interfaz de chat estilo Gemini.
    """
    def __init__(self, nlp_service, formatters):
        """
        Inicializa la interfaz de chat.
        """
        self.nlp_service = nlp_service
        self.formatters = formatters
        
        # Inicializar historial de chat
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        if 'thinking' not in st.session_state:
            st.session_state.thinking = False
    
    def chatbot_response(self, mensaje, datos_empresa=None):
        """
        Genera respuestas usando el modelo Gemini.
        """
        respuesta = self.nlp_service.generar_respuesta_chat(mensaje, datos_empresa)
        
        if datos_empresa and len(respuesta) < 100:
            nombre = datos_empresa.get('resultados', {}).get('nombre', 'tu empresa')
            respuesta += f"\n\n¿Te gustaría que profundice en algún aspecto específico de {nombre}?"
        
        return respuesta
    
    def renderizar_chat(self, datos_empresa=None):
        """
        Renderiza la interfaz del chat estilo Gemini.
        """
        # CSS específico para el chat
        st.markdown("""
            <style>
                .chat-header {
                    position: sticky;
                    top: 0;
                    background-color: var(--bg-primary);
                    border-bottom: 1px solid var(--border-color);
                    padding: 1rem 2rem;
                    z-index: 100;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                }
                
                .chat-title {
                    font-size: 1.25rem;
                    font-weight: 500;
                    color: var(--text-primary);
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                }
                
                .chat-title span {
                    background: linear-gradient(135deg, #FA8B00, #8B00FA);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-size: 1.5rem;
                }
                
                .chat-actions {
                    display: flex;
                    gap: 0.5rem;
                }
                
                .welcome-message {
                    text-align: center;
                    padding: 3rem 2rem;
                    max-width: 600px;
                    margin: 2rem auto;
                }
                
                .welcome-message .icon {
                    font-size: 3rem;
                    margin-bottom: 1rem;
                    background: linear-gradient(135deg, #FA8B00, #8B00FA);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
                
                .welcome-message h2 {
                    font-size: 1.75rem;
                    font-weight: 500;
                    color: var(--text-primary);
                    margin-bottom: 0.5rem;
                }
                
                .welcome-message p {
                    color: var(--text-secondary);
                    font-size: 1rem;
                    line-height: 1.6;
                    margin-bottom: 2rem;
                }
                
                .bot-header {
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                    margin-bottom: 1rem;
                    color: var(--text-secondary);
                    font-size: 0.9rem;
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
                
                .action-button {
                    padding: 0.375rem 0.75rem;
                    border-radius: var(--radius-sm);
                    border: 1px solid var(--border-color);
                    background: transparent;
                    color: var(--text-secondary);
                    font-size: 0.8125rem;
                    cursor: pointer;
                    transition: var(--transition);
                    display: flex;
                    align-items: center;
                    gap: 0.375rem;
                }
                
                .action-button:hover {
                    background-color: var(--bg-tertiary);
                    color: var(--text-primary);
                    border-color: var(--text-muted);
                }
                
                .thinking-indicator {
                    display: flex;
                    align-items: center;
                    padding: 1rem 2rem;
                    margin-left: 3rem;
                }
                
                .thinking-bubble {
                    background-color: transparent;
                    padding: 0.5rem 0;
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
                
                .suggestions-container {
                    max-width: 800px;
                    margin: 2rem auto;
                    padding: 0 2rem;
                }
                
                .suggestions-title {
                    font-size: 0.875rem;
                    color: var(--text-secondary);
                    margin-bottom: 1rem;
                    font-weight: 500;
                }
                
                .suggestion-chips {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 0.75rem;
                }
                
                .suggestion-chip {
                    padding: 0.625rem 1.25rem;
                    background-color: var(--bg-tertiary);
                    border: 1px solid var(--border-color);
                    border-radius: var(--radius-full);
                    color: var(--text-primary);
                    font-size: 0.875rem;
                    cursor: pointer;
                    transition: var(--transition);
                    display: inline-block;
                }
                
                .suggestion-chip:hover {
                    background-color: var(--bg-input);
                    border-color: var(--text-muted);
                    transform: translateY(-1px);
                }
                
                .chat-container {
                    padding-bottom: 100px; /* Espacio para el input fijo */
                }
                
                .chat-input-container {
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    right: 0;
                    background-color: var(--bg-primary);
                    border-top: 1px solid var(--border-color);
                    padding: 1rem 0;
                    z-index: 1000;
                }
                
                .chat-input-inner {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 0 2rem;
                }
            </style>
        """, unsafe_allow_html=True)
        
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
                st.markdown("""
                    <div class="welcome-message">
                        <div class="icon">🤖</div>
                        <h2>Hola, soy FinanzGPT</h2>
                        <p>Tu asistente financiero impulsado por IA. Estoy aquí para ayudarte a analizar y mejorar las finanzas de tu empresa.</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Sugerencias de inicio
                st.markdown("""
                    <div class="suggestions-container">
                        <div class="suggestions-title">Prueba con estas preguntas:</div>
                        <div class="suggestion-chips">
                """, unsafe_allow_html=True)
                
                sugerencias = [
                    "¿Cómo está mi situación financiera?",
                    "¿Cómo puedo mejorar mi rentabilidad?",
                    "Analiza mi nivel de endeudamiento",
                    "Dame estrategias de crecimiento"
                ]
                
                for i, sugerencia in enumerate(sugerencias):
                    if st.button(sugerencia, key=f"sug_{i}", help="Haz clic para usar esta pregunta"):
                        st.session_state.chat_history.append(("user", sugerencia))
                        st.session_state.thinking = True
                        st.rerun()
                
                st.markdown("""
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Mostrar historial
            for sender, message in st.session_state.chat_history:
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
                    
                    # Acciones del mensaje con botones funcionales
                    st.markdown("""
                                </div>
                                <div class="message-actions">
                    """, unsafe_allow_html=True)
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        if st.button("👍", key=f"like_{st.session_state.chat_history.index((sender, message))}"):
                            st.toast("¡Gracias por tu feedback!", icon="👍")
                    with col2:
                        if st.button("👎", key=f"dislike_{st.session_state.chat_history.index((sender, message))}"):
                            st.toast("Gracias por tu feedback, mejoraremos", icon="👎")
                    with col3:
                        if st.button("📋 Copiar", key=f"copy_{st.session_state.chat_history.index((sender, message))}"):
                            st.toast("Copiado al portapapeles", icon="📋")
                    with col4:
                        if st.button("🔄 Regenerar", key=f"regen_{st.session_state.chat_history.index((sender, message))}"):
                            st.session_state.thinking = True
                            st.rerun()
                    
                    st.markdown("""
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
            
            # Animación de pensamiento
            if st.session_state.thinking:
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
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Input del chat (fuera del contenedor para evitar el error)
        mensaje_usuario = st.chat_input("Pregunta a FinanzGPT...")
        
        if mensaje_usuario:
            # Agregar mensaje al historial
            st.session_state.chat_history.append(("user", mensaje_usuario))
            
            # Activar animación
            st.session_state.thinking = True
            st.rerun()
        
        # Procesar respuesta cuando thinking es True
        if st.session_state.thinking and st.session_state.chat_history:
            # Simular tiempo de procesamiento
            time.sleep(1)
            
            # Desactivar animación
            st.session_state.thinking = False
            
            # Obtener último mensaje
            ultimo_mensaje = st.session_state.chat_history[-1][1]
            
            # Generar respuesta
            respuesta = self.chatbot_response(ultimo_mensaje, datos_empresa)
            
            # Agregar al historial
            st.session_state.chat_history.append(("bot", respuesta))
            
            # Actualizar
            st.rerun()
    
    def _escape_html(self, text):
        """Escapa HTML para evitar problemas de seguridad."""
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    def _format_message(self, message):
        """Formatea el mensaje para mejor presentación."""
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