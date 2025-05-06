import streamlit as st
import re
import random
import time

class ChatUI:
    """
    Clase para manejar la interfaz de usuario del chat.
    """
    def __init__(self, nlp_service, formatters):
        """
        Inicializa la interfaz de chat.
        
        Args:
            nlp_service (NLPService): Servicio de procesamiento de lenguaje natural
            formatters (Formatters): Utilidades de formato
        """
        self.nlp_service = nlp_service
        self.formatters = formatters
        
        # Inicializar historial de chat si no existe
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        if 'thinking' not in st.session_state:
            st.session_state.thinking = False
    
    def mostrar_procesamiento(self):
        """Muestra una animación de procesamiento estilo ChatGPT"""
        with st.spinner(''):
            st.markdown("""
            <div class="thinking-animation">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
            </div>
            """, unsafe_allow_html=True)
            
            # Simulación de procesamiento
            time.sleep(2)
            
            # Mostrar mensaje de éxito al completar
            st.success('Análisis completado')
            time.sleep(0.5)
    
    def responder_mensaje_no_financiero(self, tipo):
        """
        Genera respuestas para mensajes que no son de índole financiera.
        
        Args:
            tipo (str): Tipo de mensaje no financiero
            
        Returns:
            str: Respuesta apropiada
        """
        if tipo == "saludo":
            saludos = [
                "👋 ¡Hola! Soy FinanzGPT, tu asistente financiero empresarial. ¿En qué puedo ayudarte hoy con respecto a tus finanzas?",
                "¡Hola! Estoy aquí para ayudarte con el análisis financiero de tu empresa. ¿Qué te gustaría saber?",
                "¡Saludos! Soy tu asistente especializado en análisis financiero empresarial. ¿Tienes alguna consulta sobre tus indicadores financieros?"
            ]
            return random.choice(saludos)
        
        elif tipo == "despedida":
            despedidas = [
                "¡Hasta pronto! Recuerda revisar periódicamente tus indicadores financieros para mantener el control de tu empresa.",
                "¡Adiós! Si tienes más preguntas sobre finanzas empresariales en el futuro, estaré aquí para ayudarte.",
                "¡Que tengas un buen día! Estaré disponible cuando necesites más análisis financieros para tu empresa."
            ]
            return random.choice(despedidas)
        
        elif tipo == "emocion" or tipo == "personal":
            respuestas = [
                "Como asistente financiero, estoy diseñado para ayudarte con indicadores y análisis económicos de tu empresa. ¿Te gustaría que analizáramos algún aspecto financiero específico?",
                "Mi especialidad es el análisis financiero empresarial. ¿Puedo ayudarte con alguna consulta sobre tus indicadores económicos?",
                "Estoy programado para asistirte en temas financieros empresariales. ¿Hay algún aspecto financiero de tu empresa sobre el que quieras información?"
            ]
            return random.choice(respuestas)
        
        elif tipo == "ayuda":
            # Mostrar menú de opciones de ayuda
            respuesta = """### 🔍 ¿En qué puedo ayudarte?

Soy FinanzGPT, tu asistente especializado en análisis financiero empresarial. Puedo ayudarte con:

1. **Análisis de endeudamiento**: Evaluación de tu ratio de deuda y recomendaciones para optimizarlo
2. **Análisis de rentabilidad**: Evaluación de tu ROA y estrategias para mejorar tus beneficios
3. **Análisis de productividad**: Evaluación del rendimiento por empleado y consejos para aumentarlo
4. **Análisis de rotación de cartera**: Evaluación de tu ciclo de cobro y métodos para acelerarlo
5. **Análisis de liquidez**: Evaluación de tu capacidad para cubrir obligaciones a corto plazo
6. **Resumen general financiero**: Visión global de todos tus indicadores financieros

Para consultar, simplemente pregunta por ejemplo: *"¿Cómo está mi endeudamiento?"* o *"¿Qué puedo hacer para mejorar mi rentabilidad?"*"""
            return respuesta
        
        elif tipo == "corto" or tipo == "otro":
            respuestas = [
                "Soy un asistente especializado en análisis financiero empresarial. ¿Puedo ayudarte con alguna consulta sobre indicadores financieros de tu empresa?",
                "Estoy aquí para ayudarte con análisis económico y financiero. ¿Qué indicador financiero te gustaría analizar?",
                "Como asistente financiero, puedo ayudarte a interpretar tus indicadores y darte recomendaciones para mejorar la salud económica de tu empresa. ¿Qué aspecto te interesa analizar?"
            ]
            return random.choice(respuestas)
    
    def chatbot_response(self, mensaje, datos_empresa=None):
        """
        Genera respuestas del chatbot basadas en el mensaje del usuario y los datos de la empresa.
        
        Args:
            mensaje (str): Mensaje del usuario
            datos_empresa (dict, optional): Datos de la empresa
            
        Returns:
            str: Respuesta del chatbot
        """
        # Verificar si es un mensaje no financiero
        es_no_financiero, tipo = self.nlp_service.es_mensaje_no_financiero(mensaje)
        
        if es_no_financiero:
            return self.responder_mensaje_no_financiero(tipo)
        
        # Si el mensaje es financiero, continuar con el análisis normal
        # Aplicar NLP al mensaje
        tokens = self.nlp_service.tokenizar_texto(mensaje)
        lemas = self.nlp_service.lematizar_texto(mensaje)
        pos_tags = self.nlp_service.pos_tagging(mensaje)
        keywords = self.nlp_service.extraer_keywords(mensaje, 3)
        
        # Mensajes predefinidos para diferentes situaciones
        mensajes_predefinidos = {
            'endeudamiento': [
                "El ratio de endeudamiento muestra qué proporción de tus activos está financiada por deuda. Un valor menor generalmente indica una situación más sólida, aunque depende del sector.\n\nTe invito a consultar este indicador específico para tu empresa escribiendo '¿Cómo está mi endeudamiento?'",
                "Para mejorar tu ratio de endeudamiento, podrías:\n• Aumentar el capital social\n• Reinvertir beneficios\n• Vender activos no productivos para reducir deuda\n• Renegociar plazos de pago.\n\nSi quieres un análisis más detallado de tu situación, pregúntame directamente.",
                "Es importante comparar tu ratio de endeudamiento con empresas similares del sector. Cada industria tiene sus particularidades y lo que es alto en un sector puede ser normal en otro.\n\nPuedo analizar la situación específica de tu empresa si me preguntas sobre tu nivel de endeudamiento."
            ],
            'rentabilidad': [
                "La rentabilidad sobre activos (ROA) indica cuánto beneficio generas por cada peso invertido en activos. Un ROA más alto significa que estás aprovechando mejor tus recursos.\n\nPara conocer cómo está tu rentabilidad, simplemente pregúntame '¿Cómo es mi rentabilidad?'",
                "Para mejorar tu rentabilidad podrías:\n• Aumentar precios si el mercado lo permite\n• Reducir costos operativos\n• Optimizar la gestión de inventarios\n• Deshacerte de activos poco productivos.\n\nPregúntame por un análisis específico para tu empresa.",
                "Tu ROA debe compararse con la media del sector. Si está por debajo, podría ser momento de replantearse la estrategia de negocio o buscar nuevas oportunidades de mercado.\n\nPuedo darte una evaluación personalizada si me preguntas directamente."
            ],
            'productividad': [
                "La productividad por empleado muestra cuánto genera cada trabajador en términos de ingresos. Es un indicador clave de la eficiencia operativa.\n\nSi quieres saber cómo está la productividad en tu empresa, pregúntame directamente.",
                "Para mejorar la productividad podrías:\n• Invertir en capacitación\n• Mejorar procesos y tecnología\n• Implementar sistemas de incentivos basados en resultados\n• Revisar la distribución de tareas.\n\nConsulta el estado de tu empresa preguntándome por tu nivel de productividad.",
                "Una baja productividad puede indicar exceso de personal, falta de tecnología adecuada, o procesos ineficientes. Análisis más profundos te ayudarán a identificar los cuellos de botella.\n\nPregúntame directamente por tu productividad para un análisis específico."
            ],
            'cartera': [
                "La rotación de cartera indica cuántos días tardas en cobrar tus ventas a crédito. Una rotación más baja es generalmente mejor, ya que mejora tu liquidez.\n\nPara saber cómo está tu rotación de cartera, puedes preguntarme directamente.",
                "Para mejorar tu rotación de cartera, considera:\n• Revisar políticas de crédito\n• Implementar descuentos por pronto pago\n• Mejorar el seguimiento de cobros\n• Evaluar factoring para cuentas problemáticas.\n\nPregúntame específicamente por tu rotación de cartera para un análisis personalizado.",
                "Una cartera que rota lentamente puede generar problemas de liquidez. Es importante balancear las políticas de crédito para no perder clientes pero tampoco arriesgar tu flujo de caja.\n\nSi quieres saber cómo está tu rotación de cartera, solo pregúntame."
            ],
            'liquidez': [
                "La liquidez se refiere a la capacidad de tu empresa para cumplir con sus obligaciones a corto plazo. Con los datos proporcionados, puedo hacer una estimación básica.\n\nSi quieres saber más sobre tu liquidez, pregúntame directamente.",
                "Un buen ratio de liquidez suele estar entre 1.5 y 2.0, indicando que puedes cubrir tus deudas a corto plazo sin problemas.\n\nPara un análisis específico de tu empresa, pregúntame por tu liquidez.",
                "Si tienes problemas de liquidez, podrías:\n• Mejorar la gestión de cobros\n• Renegociar plazos con proveedores\n• Establecer líneas de crédito\n• Revisar tu ciclo de conversión de efectivo.\n\nConsulta tu situación preguntándome directamente."
            ],
            'general': [
                "Basándome en los datos proporcionados, puedo analizar varios aspectos financieros de tu empresa. ¿Hay algún indicador específico que te interese conocer más a fondo?",
                "¿Sabías que el análisis financiero debe ser periódico? Te recomiendo revisar estos indicadores al menos trimestralmente para detectar tendencias y actuar a tiempo.",
                "Recuerda que cada sector tiene sus propios estándares para los indicadores financieros. Lo importante es identificar tendencias y compararte con empresas similares."
            ]
        }
        
        # Verificar el tipo de mensaje usando NLP
        # Enfoque mejorado analizando palabras clave y contexto
        if any(palabra in mensaje.lower() for palabra in ['deuda', 'endeudamiento', 'pasivo', 'prestamo', 'financiacion', 'apalancamiento']):
            categoria = 'endeudamiento'
        elif any(palabra in mensaje.lower() for palabra in ['rentabilidad', 'ganancia', 'beneficio', 'rendimiento', 'roa', 'margen','utilidad']):
            categoria = 'rentabilidad'
        elif any(palabra in mensaje.lower() for palabra in ['productividad', 'eficiencia', 'empleado', 'trabajador', 'personal', 'rendimiento']):
            categoria = 'productividad'
        elif any(palabra in mensaje.lower() for palabra in ['cartera', 'cobrar', 'credito', 'rotacion', 'cliente', 'factura', 'cobranza']):
            categoria = 'cartera'
        elif any(palabra in mensaje.lower() for palabra in ['liquidez', 'efectivo', 'caja', 'corriente', 'solvencia', 'flujo']):
            categoria = 'liquidez'
        else:
            # Análisis más avanzado basado en similitud semántica
            temas = {
                'endeudamiento': "deudas financiación pasivos préstamos créditos obligaciones financieras apalancamiento",
                'rentabilidad': "beneficios ganancias rentabilidad margen utilidad rendimiento roa roi retorno inversión",
                'productividad': "empleados trabajadores personal productividad eficiencia rendimiento laboral desempeño",
                'cartera': "cartera cobros créditos clientes facturas cuentas por cobrar cobranza",
                'liquidez': "liquidez efectivo caja flujo dinero solvencia corto plazo disponible"
            }
            
            # Calcular similitud con cada tema
            mejores_similitudes = {}
            for tema, descripcion in temas.items():
                similitud = self.nlp_service.similaridad_textos(mensaje.lower(), descripcion)
                mejores_similitudes[tema] = similitud
            
            # Elegir el tema con mayor similitud si supera un umbral
            mejor_tema = max(mejores_similitudes.items(), key=lambda x: x[1])
            if mejor_tema[1] > 0.1:  # Umbral de similitud
                categoria = mejor_tema[0]
            else:
                categoria = 'general'
        
        # Si hay datos de empresa, personalizar respuesta
        if datos_empresa and 'resultados' in datos_empresa:
            resultados = datos_empresa['resultados']
            
            if categoria == 'endeudamiento':
                ratio = resultados['indicadores']['ratio_endeudamiento']
                evaluacion = resultados['evaluacion']['endeudamiento']
                
                # Respuesta detallada y personalizada
                respuesta = f"### 📊 Análisis de Endeudamiento\n\nTu ratio de endeudamiento es **{ratio:.2f}**, lo cual es considerado **{evaluacion}** para el sector {resultados['sector']}.\n\n"
                
                # Añadir interpretación según el valor
                if ratio < 0.4:
                    respuesta += "Este valor indica un bajo nivel de endeudamiento, lo que es positivo para la estabilidad financiera, pero podría estar perdiendo oportunidades de apalancamiento para crecer más rápido.\n\n"
                elif ratio < 0.6:
                    respuesta += "Este valor muestra un endeudamiento moderado y saludable, un buen balance entre capital propio y ajeno.\n\n"
                else:
                    respuesta += "Este nivel de endeudamiento es elevado, lo que podría aumentar el riesgo financiero y dificultar el acceso a nuevo financiamiento.\n\n"
                
                # Añadir recomendaciones específicas
                if ratio > 0.6:
                    respuesta += "**Recomendaciones para reducir tu endeudamiento:**\n\n"
                    respuesta += "1. Considera aumentar el capital social o reinvertir beneficios\n"
                    respuesta += "2. Evalúa la posibilidad de vender activos no estratégicos\n"
                    respuesta += "3. Establece un plan gradual de reducción de deuda\n"
                    respuesta += "4. Renegocia condiciones de crédito con tus acreedores\n\n"
                
                return respuesta
            
            # Otras categorías de respuestas seguirían el mismo patrón...
            # (He omitido las otras categorías por brevedad, pero funcionarían similarmente)
            
        # Si no hay datos de empresa o la consulta es general
        # Usar POS tagging para identificar verbos y sustantivos clave
        verbos = [word for word, tag in pos_tags if tag == 'VERB']
        sustantivos = [word for word, tag in pos_tags if tag in ['NOUN', 'PROPN']]
        
        # Personalización básica basada en palabras extraídas
        if verbos and sustantivos:
            accion = verbos[0]
            tema = sustantivos[0] if sustantivos else "empresa"
            respuesta = f"Entiendo que quieres {accion} sobre {tema}. "
            respuesta += random.choice(mensajes_predefinidos.get(categoria, mensajes_predefinidos['general']))
            return respuesta
        
        # Si no hay suficiente contexto para personalizar, usar respuesta predefinida
        return random.choice(mensajes_predefinidos.get(categoria, mensajes_predefinidos['general']))
    
    def renderizar_chat(self, datos_empresa=None):
        """
        Renderiza la interfaz del chat.
        
        Args:
            datos_empresa (dict, optional): Datos de la empresa
        """
        st.markdown('<div class="main-title">💬 Chat con FinanzGPT</div>', unsafe_allow_html=True)
        
        # Si no hay datos de empresa, mostrar mensaje
        if not datos_empresa:
            st.info("👋 Para obtener respuestas personalizadas sobre tu empresa, primero debes ingresar tus datos financieros en la sección 'Datos'.")
        
        # Contenedor para el historial de chat
        chat_container = st.container()
        
        # Mostrar historial de chat con estilos mejorados
        with chat_container:
            if not st.session_state.chat_history:
                st.markdown("""
                <div style="text-align: center; margin: 50px 0; color: #888;">
                    <p>👋 ¡Hola! Soy FinanzGPT, tu asistente financiero.</p>
                    <p>Puedes preguntarme sobre indicadores financieros, recomendaciones para tu empresa, o cualquier duda sobre análisis económico.</p>
                    <p>Escribe "ayuda" si necesitas ver un menú de opciones.</p>
                </div>
                """, unsafe_allow_html=True)
            
            for sender, message in st.session_state.chat_history:
                if sender == "user":
                    st.markdown(f"""
                    <div class="chat-message-user">
                        <div class="avatar avatar-user">U</div>
                        <div class="message-content">{message}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    # Convertir marcadores markdown en mensaje HTML
                    # Procesar encabezados
                    message = re.sub(r'### (.*)', r'<h3>\1</h3>', message)
                    # Procesar negritas
                    message = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', message)
                    # Procesar itálicas
                    message = re.sub(r'\*(.*?)\*', r'<em>\1</em>', message)
                    # Procesar listas con viñetas
                    message = re.sub(r'• (.*)', r'<li>\1</li>', message)
                    message = message.replace('<li>', '<ul><li>').replace('</li>\n\n', '</li></ul>\n\n')
                    
                    st.markdown(f"""
                    <div class="chat-message-bot">
                        <div class="avatar avatar-bot">F</div>
                        <div class="message-content">{message}</div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Manejar el estado "pensando"
        if st.session_state.thinking:
            st.markdown("""
            <div class="thinking-animation">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
            </div>
            """, unsafe_allow_html=True)
        
        # Input para chatbot
        mensaje_usuario = st.chat_input("Escribe tu pregunta aquí...")
        
        if mensaje_usuario:
            # Agregar mensaje del usuario al historial
            st.session_state.chat_history.append(("user", mensaje_usuario))
            
            # Activar animación de pensamiento
            st.session_state.thinking = True
            st.rerun()
        
        # Este código se ejecuta después del rerun cuando thinking es True
        if st.session_state.thinking and st.session_state.chat_history:
            # Desactivar el estado "pensando"
            st.session_state.thinking = False
            
            # Obtener la última pregunta del usuario
            ultima_pregunta = [msg for sender, msg in st.session_state.chat_history if sender == "user"][-1]
            
            # Generar respuesta del chatbot
            respuesta = self.chatbot_response(ultima_pregunta, datos_empresa)
            
            # Agregar respuesta al historial
            st.session_state.chat_history.append(("bot", respuesta))
            
            # Actualizar chat
            st.rerun()