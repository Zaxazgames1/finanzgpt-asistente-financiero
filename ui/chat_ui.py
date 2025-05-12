import streamlit as st
import re
import time

class ChatUI:
    """
    Interfaz de chat tipo ChatGPT usando Flan-T5.
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
        Genera respuestas usando el modelo T5.
        
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
        Renderiza la interfaz del chat.
        """
        st.markdown('<div class="main-title">💬 Chat con FinanzGPT</div>', unsafe_allow_html=True)
        
        # Mensaje informativo si no hay datos
        if not datos_empresa:
            st.info("👋 Para análisis personalizados, ingresa primero los datos de tu empresa en la sección 'Datos'. Mientras tanto, ¡pregúntame lo que quieras sobre finanzas!")
        
        # Contenedor del chat
        chat_container = st.container()
        
        with chat_container:
            # Mensaje de bienvenida si el chat está vacío
            if not st.session_state.chat_history:
                st.markdown("""
                <div style="text-align: center; margin: 50px 0; color: #888;">
                    <h3>¡Bienvenido a FinanzGPT! 🤖💰</h3>
                    <p>Soy tu asistente financiero inteligente. Puedo ayudarte con:</p>
                    <ul style="text-align: left; display: inline-block; list-style: none;">
                        <li>✅ Análisis de indicadores financieros</li>
                        <li>✅ Evaluación de salud económica</li>
                        <li>✅ Recomendaciones personalizadas</li>
                        <li>✅ Estrategias de mejora</li>
                    </ul>
                    <p><strong>Escribe "hola" para comenzar 👇</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            # Mostrar historial
            for sender, message in st.session_state.chat_history:
                if sender == "user":
                    st.markdown(f"""
                    <div class="chat-message-user">
                        <div class="avatar avatar-user">👤</div>
                        <div class="message-content">{message}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # Formatear mensaje del bot
                    formatted_message = self._format_message(message)
                    st.markdown(f"""
                    <div class="chat-message-bot">
                        <div class="avatar avatar-bot">🤖</div>
                        <div class="message-content">{formatted_message}</div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Animación de pensamiento
        if st.session_state.thinking:
            st.markdown("""
            <div class="thinking-animation">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
            </div>
            <p style="text-align: center; color: #888;">Analizando...</p>
            """, unsafe_allow_html=True)
        
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
    
    def _format_message(self, message):
        """
        Formatea el mensaje para mejor presentación.
        """
        # Convertir markdown básico a HTML
        message = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', message)
        message = re.sub(r'\*(.*?)\*', r'<em>\1</em>', message)
        
        # Convertir saltos de línea
        message = message.replace('\n\n', '</p><p>')
        message = message.replace('\n', '<br>')
        
        # Añadir párrafos
        if not message.startswith('<p>'):
            message = f'<p>{message}</p>'
        
        return message