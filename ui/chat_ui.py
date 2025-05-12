import streamlit as st
import re
import time

class ChatUI:
    """
    Interfaz de chat tipo ChatGPT usando Gemini.
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
        
        Args:
            mensaje (str): Mensaje del usuario
            datos_empresa (dict): Datos de la empresa si existen
            
        Returns:
            str: Respuesta del chatbot
        """
        # Usar el nuevo método del servicio NLP
        respuesta = self.nlp_service.generar_respuesta_chat(mensaje, datos_empresa)
        
        # Si la respuesta es muy técnica, añadir algo de contexto
        if datos_empresa and len(respuesta) < 100:
            nombre = datos_empresa.get('resultados', {}).get('nombre', 'tu empresa')
            respuesta += f"\n\n¿Te gustaría que profundice en algún aspecto específico de {nombre}?"
        
        return respuesta
    
    def renderizar_chat(self, datos_empresa=None):
        """
        Renderiza la interfaz del chat con diseño ultra moderno.
        """
        # CSS específico para el chat
        st.markdown("""
            <style>
                .chat-container {
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 2rem;
                    height: calc(100vh - 200px);
                    overflow-y: auto;
                }
                
                .chat-message-user, .chat-message-bot {
                    display: flex;
                    gap: 1rem;
                    margin-bottom: 1.5rem;
                    animation: fadeInUp 0.4s ease;
                }
                
                @keyframes fadeInUp {
                    from {
                        opacity: 0;
                        transform: translateY(20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                
                .chat-message-user {
                    justify-content: flex-end;
                }
                
                .chat-message-bot {
                    justify-content: flex-start;
                }
                
                .message-content {
                    max-width: 70%;
                    padding: 1rem 1.25rem;
                    border-radius: 12px;
                    line-height: 1.6;
                    font-size: 0.9375rem;
                }
                
                .chat-message-user .message-content {
                    background-color: #10a37f;
                    color: white;
                    border-bottom-right-radius: 4px;
                }
                
                .chat-message-bot .message-content {
                    background-color: #2a2a2a;
                    color: #ececec;
                    border: 1px solid #444444;
                    border-bottom-left-radius: 4px;
                }
                
                .avatar {
                    width: 40px;
                    height: 40px;
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1.25rem;
                    flex-shrink: 0;
                }
                
                .avatar-user {
                    background-color: #262626;
                    color: #ececec;
                }
                
                .avatar-bot {
                    background: linear-gradient(135deg, #10a37f, #2dd4bf);
                    color: white;
                    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                }
                
                .welcome-chat {
                    text-align: center;
                    padding: 3rem 2rem;
                    max-width: 600px;
                    margin: 0 auto;
                }
                
                .welcome-chat-icon {
                    font-size: 4rem;
                    margin-bottom: 1rem;
                    animation: float 3s ease-in-out infinite;
                }
                
                @keyframes float {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-10px); }
                }
                
                .welcome-chat-title {
                    font-size: 1.75rem;
                    font-weight: 600;
                    color: #ececec;
                    margin-bottom: 0.5rem;
                }
                
                .welcome-chat-text {
                    font-size: 1.125rem;
                    color: #a8a8a8;
                    margin-bottom: 2rem;
                }
                
                .welcome-features {
                    display: grid;
                    gap: 1rem;
                    margin-bottom: 2rem;
                    text-align: left;
                    max-width: 400px;
                    margin-left: auto;
                    margin-right: auto;
                }
                
                .welcome-feature {
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                    font-size: 1rem;
                    color: #ececec;
                }
                
                .feature-check {
                    color: #22c55e;
                    font-size: 1.25rem;
                }
                
                .welcome-cta {
                    font-size: 1.125rem;
                    color: #a8a8a8;
                }
                
                .info-banner {
                    background-color: rgba(16, 163, 127, 0.1);
                    border: 1px solid #10a37f;
                    border-radius: 12px;
                    padding: 1rem 1.5rem;
                    margin-bottom: 2rem;
                    display: flex;
                    align-items: center;
                    gap: 1rem;
                    max-width: 900px;
                    margin-left: auto;
                    margin-right: auto;
                }
                
                .info-icon {
                    font-size: 1.5rem;
                    color: #10a37f;
                }
                
                .info-text {
                    color: #ececec;
                    font-size: 0.9375rem;
                    line-height: 1.5;
                }
                
                .typing-indicator {
                    display: flex;
                    align-items: center;
                    padding: 1rem;
                }
                
                .typing-bubble {
                    background-color: #1a1a1a;
                    border: 1px solid #444444;
                    border-radius: 12px;
                    padding: 0.75rem 1.25rem;
                    display: flex;
                    gap: 0.4rem;
                    align-items: center;
                    border-bottom-left-radius: 4px;
                }
                
                .typing-dot {
                    width: 8px;
                    height: 8px;
                    background-color: #a8a8a8;
                    border-radius: 50%;
                    animation: typing 1.4s ease-in-out infinite;
                }
                
                .typing-dot:nth-child(1) {
                    animation-delay: 0s;
                }
                
                .typing-dot:nth-child(2) {
                    animation-delay: 0.2s;
                }
                
                .typing-dot:nth-child(3) {
                    animation-delay: 0.4s;
                }
                
                @keyframes typing {
                    0%, 60%, 100% {
                        transform: translateY(0);
                        opacity: 0.5;
                    }
                    30% {
                        transform: translateY(-10px);
                        opacity: 1;
                    }
                }
                
                /* Estilos para el contenido formateado del bot */
                .bot-content p {
                    margin-bottom: 0.75rem;
                    line-height: 1.6;
                }
                
                .bot-content ul, .bot-content ol {
                    margin-left: 1.5rem;
                    margin-bottom: 1rem;
                    line-height: 1.6;
                }
                
                .bot-content strong {
                    color: #2dd4bf;
                    font-weight: 600;
                }
                
                .bot-content em {
                    color: #a8a8a8;
                    font-style: italic;
                }
                
                .bot-content h2, .bot-content h3, .bot-content h4 {
                    color: #10a37f;
                    font-weight: 600;
                    margin-top: 1rem;
                    margin-bottom: 0.5rem;
                }
                
                .bot-content h2 {
                    font-size: 1.3rem;
                }
                
                .bot-content h3 {
                    font-size: 1.15rem;
                }
                
                .bot-content h4 {
                    font-size: 1.05rem;
                }
                
                .main-title {
                    font-size: 2rem;
                    font-weight: 700;
                    background: linear-gradient(90deg, #10a37f, #2dd4bf);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    text-align: center;
                    margin: 2rem 0 1rem 0;
                    letter-spacing: -0.02em;
                }
            </style>
        """, unsafe_allow_html=True)
        
        # Título del chat
        st.markdown('<h1 class="main-title">💬 Chat con FinanzGPT</h1>', unsafe_allow_html=True)
        
        # Mensaje informativo si no hay datos
        if not datos_empresa:
            st.markdown("""
                <div class="info-banner">
                    <div class="info-icon">💡</div>
                    <div class="info-text">
                        Para análisis personalizados, ingresa primero los datos de tu empresa en la sección 
                        <strong>📝 Datos</strong>. Mientras tanto, ¡pregúntame lo que quieras sobre finanzas!
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        # Contenedor del chat
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        # Mensaje de bienvenida si el chat está vacío
        if not st.session_state.chat_history:
            st.markdown("""
                <div class="welcome-chat">
                    <div class="welcome-chat-icon">🤖</div>
                    <h2 class="welcome-chat-title">¡Hola! Soy FinanzGPT</h2>
                    <p class="welcome-chat-text">
                        Tu asistente financiero inteligente está listo para ayudarte.
                    </p>
                    <div class="welcome-features">
                        <div class="welcome-feature">
                            <span class="feature-check">✅</span>
                            Análisis de indicadores financieros
                        </div>
                        <div class="welcome-feature">
                            <span class="feature-check">✅</span>
                            Evaluación de salud económica
                        </div>
                        <div class="welcome-feature">
                            <span class="feature-check">✅</span>
                            Recomendaciones personalizadas
                        </div>
                        <div class="welcome-feature">
                            <span class="feature-check">✅</span>
                            Estrategias de mejora
                        </div>
                    </div>
                    <p class="welcome-cta">Escribe <strong>"hola"</strong> para comenzar 👋</p>
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
                # Formatear mensaje del bot
                formatted_message = self._format_message(message)
                st.markdown(f"""
                    <div class="chat-message-bot">
                        <div class="avatar avatar-bot">🤖</div>
                        <div class="message-content bot-content">
                            {formatted_message}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        
        # Animación de pensamiento
        if st.session_state.thinking:
            st.markdown("""
                <div class="typing-indicator">
                    <div class="typing-bubble">
                        <div class="typing-dot"></div>
                        <div class="typing-dot"></div>
                        <div class="typing-dot"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Input del chat
        mensaje_usuario = st.chat_input("Escribe tu mensaje aquí...")
        
        if mensaje_usuario:
            # Agregar mensaje al historial
            st.session_state.chat_history.append(("user", mensaje_usuario))
            
            # Activar animación
            st.session_state.thinking = True
            st.rerun()
        
        # Procesar respuesta cuando thinking es True
        if st.session_state.thinking and st.session_state.chat_history:
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
        """
        Escapa HTML para evitar problemas de seguridad.
        """
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    def _format_message(self, message):
        """
        Formatea el mensaje para mejor presentación.
        """
        # Escapar HTML primero
        message = self._escape_html(message)
        
        # Formatear headers
        message = re.sub(r'^#{4}\s+(.+)$', r'<h4>\1</h4>', message, flags=re.MULTILINE)
        message = re.sub(r'^#{3}\s+(.+)$', r'<h3>\1</h3>', message, flags=re.MULTILINE)
        message = re.sub(r'^#{2}\s+(.+)$', r'<h2>\1</h2>', message, flags=re.MULTILINE)
        message = re.sub(r'^#{1}\s+(.+)$', r'<h2>\1</h2>', message, flags=re.MULTILINE)
        
        # Formatear negritas y cursivas
        message = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', message)
        message = re.sub(r'\*(.+?)\*', r'<em>\1</em>', message)
        
        # Formatear listas no ordenadas
        message = re.sub(r'^[\*\-•]\s+(.+)$', r'<li>\1</li>', message, flags=re.MULTILINE)
        
        # Agrupar elementos li consecutivos en ul
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
        
        # Formatear listas numeradas
        message = re.sub(r'^(\d+)\.\s+(.+)$', r'<li>\2</li>', message, flags=re.MULTILINE)
        
        # Convertir saltos de línea dobles en párrafos
        paragraphs = message.split('\n\n')
        formatted_paragraphs = []
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if paragraph:
                if not paragraph.startswith('<'):
                    paragraph = f'<p>{paragraph}</p>'
                # Convertir saltos de línea simples en <br>
                paragraph = paragraph.replace('\n', '<br>')
                formatted_paragraphs.append(paragraph)
        
        return '\n'.join(formatted_paragraphs)