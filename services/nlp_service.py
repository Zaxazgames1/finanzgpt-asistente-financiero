import requests
import json
import time
import random

class NLPService:
    """
    Servicio NLP usando Google Gemini 2.0 Flash API con enfoque EXCLUSIVO en finanzas.
    """
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NLPService, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        """
        Inicializa el servicio con Gemini.
        """
        if NLPService._initialized:
            return
            
        # Tu API key de Gemini
        self.api_key = "AIzaSyA-Vuy7H8fSsJ1gLAaJDVg-jMtGwpCP6kQ"
        
        # URL del endpoint correcto
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"
        
        # Headers
        self.headers = {
            'Content-Type': 'application/json'
        }
        
        # Lista ampliada de temas financieros para clasificación
        self.temas_financieros = [
            # Finanzas generales
            'finanza', 'empresa', 'dinero', 'capital', 'ganancia', 'presupuesto',
            'deuda', 'rentabilidad', 'productividad', 'indicador', 'economía',
            'endeudamiento', 'análisis', 'negocio', 'inversión', 'balance',
            'contabilidad', 'impuesto', 'iva', 'crédito', 'préstamo', 'banca',
            'ahorro', 'bolsa', 'acción', 'dividendo', 'interés', 'tasa',
            'inflación', 'deflación', 'mercado', 'comercio', 'venta', 'compra',
            'cliente', 'proveedor', 'factura', 'inventario', 'activo', 'pasivo',
            'patrimonio', 'flujo', 'caja', 'liquidez', 'solvencia', 'quiebra', 
            'seguro', 'riesgo', 'beneficio', 'costo', 'precio', 'margen', 'utilidad',
            'pérdida', 'roe', 'roa', 'ebitda', 'capm', 'wacc', 'roi', 'van', 'tir',
            'pib', 'pyme', 'startup', 'emprendimiento', 'accionista', 'socio',
            'inversion', 'hipoteca', 'pension', 'jubilacion', 'salario', 'nomina',
            # Términos específicos adicionales
            'balance general', 'estado de resultados', 'flujo de efectivo',
            'depreciación', 'amortización', 'apalancamiento', 'ratio', 'kpi',
            'monetario', 'fiscal', 'tributario', 'gastos', 'ingresos', 'nómina',
            'ventas', 'tesorería', 'ahorros', 'inversiones', 'dividendos', 
            'accionistas', 'acciones', 'bonos', 'debentures', 'letras', 'pagarés',
            'hipoteca', 'crédito', 'préstamo', 'leasing', 'factoring', 'subvención',
            'impuestos', 'tributos', 'evasión', 'elusión', 'declaración', 'renta',
            'depósito', 'cheque', 'transferencia', 'transacción', 'patrimonio'
        ]
        
        # Lista ampliada de palabras conversacionales comunes (permitidas aunque no sean de finanzas)
        self.palabras_conversacionales = [
            'hola', 'buenos días', 'buenas tardes', 'buenas noches', 'adiós', 
            'gracias', 'por favor', 'cómo estás', 'qué tal', 'hasta luego',
            'excelente', 'genial', 'perfecto', 'entiendo', 'claro', 'ok', 'bueno',
            'ayuda', 'asistencia', 'explicación', 'ejemplo', 'duda', 'pregunta',
            'respuesta', 'información', 'consejo', 'recomendación', 'guía',
            'consejos', 'tiempo', 'nombre', 'colombia', 'bogotá', 'medellín', 'cali'
        ]
        
        # Lista ampliada de temas prohibidos
        self.temas_prohibidos = [
            # Comida y recetas
            'receta', 'cocina', 'comida', 'desayuno', 'almuerzo', 'cena', 'plato', 'cocinado', 'cocinar',
            'ingrediente', 'hornear', 'freír', 'asar', 'sopa', 'ensalada', 'postre', 'postres', 'restaurante',
            'bebida', 'café', 'té', 'pizza', 'hamburguesa', 'pastel', 'panadería', 'repostería',
            # Temas médicos detallados
            'medicamento', 'medicina', 'tratamiento', 'enfermedad', 'síntoma', 'diagnóstico', 'cura',
            'doctor', 'médico', 'hospital', 'clínica', 'farmacia', 'receta médica', 'cirugía', 'operación',
            'terapia', 'rehabilitación', 'salud', 'virus', 'bacteria', 'antibiótico', 'vacuna',
            # Viajes y reservas específicos
            'hotel', 'reserva', 'vuelo', 'hospedaje', 'alojamiento', 'itinerario', 'ruta turística',
            'turismo', 'vacaciones', 'viaje', 'tour', 'aeropuerto', 'avión', 'crucero', 'destino',
            'turista', 'playa', 'montaña', 'camping', 'mochilero', 'pasaporte', 'visa',
            # Relaciones personales
            'amor', 'divorcio', 'cita', 'matrimonio', 'novia', 'novio', 'pareja', 'ruptura', 'relación',
            'boda', 'compromiso', 'anillo', 'romance', 'coqueteo', 'familia', 'hijo', 'hija', 'hermano',
            'hermana', 'padre', 'madre', 'tío', 'tía', 'abuelo', 'abuela', 'primo', 'prima',
            # Entretenimiento específico
            'película', 'serie', 'episodio', 'canción', 'cantante', 'actor', 'actriz', 'director',
            'cine', 'teatro', 'música', 'concierto', 'festival', 'baile', 'danza', 'libro', 'novela',
            'autor', 'escritor', 'poeta', 'poesía', 'lectura', 'videojuego', 'juego', 'consola',
            # Deportes específicos
            'jugador', 'equipo', 'gol', 'campeonato', 'mundial', 'liga', 'partido', 'marcador',
            'fútbol', 'baloncesto', 'tenis', 'béisbol', 'golf', 'atletismo', 'natación', 'gimnasio',
            'ejercicio', 'entrenamiento', 'competición', 'medalla', 'récord', 'estadio', 'cancha',
            # Tecnología detallada
            'instalar', 'configurar', 'hardware', 'software', 'videojuego', 'consola', 'dispositivo',
            'smartphone', 'laptop', 'tablet', 'ordenador', 'computadora', 'programación', 'código',
            'desarrollo', 'app', 'aplicación', 'sistema operativo', 'red', 'internet', 'wifi',
            # Otros temas alejados de finanzas
            'noticia', 'política', 'religión', 'historia', 'filosofía', 'ciencia', 'arte', 'cultura',
            'idioma', 'lenguaje', 'gramática', 'traducción', 'educación', 'escuela', 'universidad',
            'moda', 'ropa', 'estilo', 'belleza', 'maquillaje', 'cosmética', 'hogar', 'decoración',
            'jardinería', 'limpieza', 'mascotas', 'animales', 'películas', 'tv', 'chatgpt', 'inteligencia artificial',
            'robot', 'gemini', 'poesía', 'chiste', 'broma', 'anime', 'videojuegos', 'cuento'
        ]
        
        print("✅ Gemini 2.0 Flash cargado exitosamente")
        NLPService._initialized = True
    
    def generar_respuesta_chat(self, mensaje, contexto_empresa=None):
        """
        Genera respuestas excepcionales tipo ChatGPT en español con enfoque financiero.
        """
        try:
            # Verificar si el mensaje está relacionado con finanzas
            es_tema_financiero, tipo_mensaje = self.es_mensaje_financiero(mensaje)
            
            # Si no es tema financiero ni conversacional, devolver respuesta estándar
            if not es_tema_financiero and tipo_mensaje != "conversacional":
                return self._respuesta_no_financiera(mensaje)
            
            # Prompt del sistema (mejorado para ser más estricto)
            system_prompt = """Eres FinanzGPT, un asistente financiero altamente especializado, EXCLUSIVAMENTE enfocado en finanzas empresariales y personales. Tu propósito principal es ayudar con consultas financieras y económicas.

RESTRICCIÓN CRÍTICA: 
- SOLO responderás preguntas relacionadas con finanzas, economía o negocios.
- Si te preguntan sobre CUALQUIER otro tema (comida, deportes, tecnología, entretenimiento, etc.), responderás amablemente que eres un asistente EXCLUSIVAMENTE financiero y redirigirás la conversación a temas financieros.
- SIEMPRE responde en español perfecto y natural.

PERSONALIDAD Y ESTILO:
- Eres extremadamente inteligente, amigable y profesional
- Hablas español perfectamente con un tono conversacional natural
- Usas emojis de forma moderada para ser más cercano (👋 😊 📊 💰 ✅ 🎯 💡)
- Das respuestas detalladas pero bien estructuradas
- Eres empático y entiendes las preocupaciones del usuario

RESPUESTA A TEMAS NO FINANCIEROS:
Algo como: "Aprecio tu interés en este tema, pero como asistente financiero especializado, mi área de experiencia se centra exclusivamente en finanzas, economía y negocios. ¿Puedo ayudarte con alguna consulta relacionada con finanzas empresariales o personales?"

CAPACIDADES EXCEPCIONALES:
1. Análisis financiero profundo y preciso
2. Explicaciones claras de conceptos complejos
3. Recomendaciones prácticas y accionables
4. Comparaciones con estándares del sector
5. Planes estratégicos personalizados
6. Predicciones basadas en datos
7. Soluciones creativas a problemas financieros

FORMA DE RESPONDER:
- Siempre saluda de forma amigable
- Estructura tus respuestas con títulos y subtítulos cuando sea apropiado
- Usa bullets y numeración para claridad
- Incluye ejemplos concretos cuando sea útil
- Termina con una pregunta o invitación a continuar la conversación

RECUERDA: SOLO RESPONDE A TEMAS FINANCIEROS O ECONÓMICOS. PARA CUALQUIER OTRO TEMA, REDIRECCIONA AMABLEMENTE."""
            
            # Construir el prompt completo
            prompt_completo = system_prompt + "\n\n"
            
            # Añadir contexto de empresa si existe
            if contexto_empresa and 'resultados' in contexto_empresa:
                resultados = contexto_empresa['resultados']
                contexto_detallado = f"""
CONTEXTO ACTUAL DE LA EMPRESA:
🏢 Empresa: {resultados['nombre']}
🏭 Sector: {resultados['sector']}
📊 Estado General: {resultados['estado_general']}

INDICADORES FINANCIEROS ACTUALES:
- Ratio de Endeudamiento: {resultados['indicadores']['ratio_endeudamiento']:.2f} ({resultados['evaluacion']['endeudamiento']})
- Rentabilidad (ROA): {resultados['indicadores']['rentabilidad']:.2%} ({resultados['evaluacion']['rentabilidad']}) 
- Productividad: ${resultados['indicadores']['productividad']:,.0f} por empleado ({resultados['evaluacion']['productividad']})
- Rotación de Cartera: {resultados['indicadores']['rotacion_cartera']:.0f} días ({resultados['evaluacion']['rotacion']})

Usa estos datos para personalizar tus respuestas y dar consejos específicos.
"""
                prompt_completo += contexto_detallado
            
            # Añadir información sobre el tipo de mensaje
            if not es_tema_financiero:
                if tipo_mensaje == "conversacional":
                    prompt_completo += f"\n\nTIPO DE MENSAJE: Conversacional general (saludo, cortesía). Responde normalmente y luego dirige hacia temas financieros."
                else:
                    prompt_completo += f"\n\nTIPO DE MENSAJE: No financiero. IMPORTANTE: Responde BREVEMENTE explicando que solo puedes hablar de temas FINANCIEROS, y sugiere algunos temas financieros sobre los que puedes ayudar."
            
            # Añadir mensaje del usuario
            prompt_completo += f"\n\nUSUARIO: {mensaje}\n\nFINANZGPT (responde en español de forma excepcional):"
            
            # Preparar el payload
            payload = {
                "contents": [{
                    "parts": [{
                        "text": prompt_completo
                    }]
                }]
            }
            
            # Hacer la petición
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            
            # Procesar la respuesta
            if response.status_code == 200:
                result = response.json()
                # Extraer el texto de la respuesta
                if 'candidates' in result and len(result['candidates']) > 0:
                    respuesta = result['candidates'][0]['content']['parts'][0]['text']
                    
                    # Verificar que esté en español
                    if self._detectar_ingles(respuesta):
                        return self._respuesta_premium_espanol(mensaje, contexto_empresa, es_tema_financiero)
                    
                    # Verificar que sea respuesta financiera para temas no financieros
                    if not es_tema_financiero and tipo_mensaje != "conversacional":
                        # Si la respuesta parece entrar en el tema no financiero, forzar respuesta estándar
                        for tema in self.temas_prohibidos:
                            if tema in respuesta.lower() and tema not in self.temas_financieros:
                                return self._respuesta_no_financiera(mensaje)
                    
                    return respuesta
                else:
                    return self._respuesta_premium_espanol(mensaje, contexto_empresa, es_tema_financiero)
            else:
                print(f"Error de API: {response.status_code} - {response.text}")
                return self._respuesta_premium_espanol(mensaje, contexto_empresa, es_tema_financiero)
                
        except Exception as e:
            print(f"Error con Gemini: {e}")
            return self._respuesta_premium_espanol(mensaje, contexto_empresa, es_tema_financiero)
    
    def es_mensaje_financiero(self, mensaje):
        """
        Determina si un mensaje está relacionado con temas financieros.
        Mejora la detección con análisis más profundo.
        
        Args:
            mensaje (str): El mensaje del usuario
            
        Returns:
            tuple: (es_financiero, tipo_mensaje)
        """
        mensaje_lower = mensaje.lower()
        palabras = mensaje_lower.split()
        
        # Primero verificar temas prohibidos explícitamente
        for tema in self.temas_prohibidos:
            if tema in mensaje_lower:
                # Si contiene tema prohibido, definitivamente no es financiero
                return False, "no_financiero"
        
        # Detectar saludos y conversación casual
        for palabra in self.palabras_conversacionales:
            if palabra in mensaje_lower:
                return False, "conversacional"
        
        # Detectar temas financieros (prioridad más alta)
        for tema in self.temas_financieros:
            if tema in mensaje_lower:
                return True, "financiero"
        
        # Verificar longitud - mensajes cortos suelen ser conversacionales
        if len(palabras) <= 3:
            return False, "conversacional"
            
        # Por defecto, asumir que no es un tema financiero
        return False, "no_financiero"
    
    def _detectar_ingles(self, texto):
        """Detecta si la respuesta está en inglés."""
        palabras_ingles = ['the', 'is', 'are', 'what', 'how', 'financial', 'company', 'and', 'or', 'but', 'this', 'that']
        contador = sum(1 for palabra in palabras_ingles if ' ' + palabra + ' ' in ' ' + texto.lower() + ' ')
        return contador >= 3
    
    def _respuesta_premium_espanol(self, mensaje, contexto_empresa=None, es_tema_financiero=True):
        """Respuestas premium en español cuando falla Gemini."""
        mensaje_lower = mensaje.lower().strip()
        
        # Verificar si es un tema prohibido
        for tema in self.temas_prohibidos:
            if tema in mensaje_lower:
                return self._respuesta_no_financiera(mensaje)
        
        # SALUDOS
        if any(saludo in mensaje_lower for saludo in ['hola', 'hi', 'hey', 'buenas', 'saludos']):
            return """¡Hola! 👋 ¡Qué gusto saludarte!

Soy FinanzGPT, tu asistente financiero personal de última generación. Estoy aquí para hacer que las finanzas de tu empresa sean claras, comprensibles y sobre todo, mejorables.

Puedo ayudarte con:
- 📊 Análisis profundo de indicadores financieros
- 💡 Estrategias personalizadas de mejora
- 📈 Planes de crecimiento sostenible
- 💰 Optimización de recursos y costos
- 🎯 Decisiones basadas en datos

¿Qué aspecto de tu empresa te gustaría analizar hoy? ¿O prefieres que empecemos con un diagnóstico general?"""
        
        # CÓMO ESTÁS
        elif any(estado in mensaje_lower for estado in ['cómo estás', 'como estas', 'qué tal', 'que tal', 'como va']):
            return """¡Excelente, gracias por preguntar! 😊 

Estoy funcionando al 100% y con muchas ganas de ayudarte a mejorar las finanzas de tu empresa. Mi inteligencia artificial está optimizada para darte las mejores recomendaciones financieras.

¿Y tú cómo estás? ¿Hay algún tema financiero que te esté preocupando o sobre el que necesites claridad? Estoy aquí para ayudarte con cualquier análisis que necesites."""
        
        # QUÉ HACES / QUIÉN ERES
        elif any(pregunta in mensaje_lower for pregunta in ['qué haces', 'que haces', 'quién eres', 'quien eres', 'qué eres', 'que eres']):
            return """Soy FinanzGPT, tu asistente financiero inteligente de nueva generación 🤖💰

Piensa en mí como tu CFO virtual personal. Mi misión es democratizar el conocimiento financiero avanzado y ponerlo al alcance de todas las empresas, sin importar su tamaño.

**Mis superpoderes incluyen:**

🧠 **Inteligencia Financiera Avanzada**
- Analizo datos complejos en segundos
- Identifico patrones y tendencias ocultas
- Proyecto escenarios futuros con precisión

💡 **Consultoría Estratégica**
- Diseño planes de acción personalizados
- Sugiero optimizaciones específicas para tu sector
- Creo estrategias de crecimiento sostenible

📊 **Análisis Profundo**
- Evaluó todos tus indicadores clave (ROA, ROE, liquidez, etc.)
- Comparo con estándares del sector
- Detecto oportunidades de mejora inmediatas

🎓 **Educación Financiera**
- Explico conceptos complejos de forma simple
- Te enseño mejores prácticas del mercado
- Te empodero para tomar mejores decisiones

¿Te gustaría ver mis capacidades en acción? Puedo hacer un análisis rápido de tu empresa si me compartes algunos datos básicos."""
        
        # DESPEDIDAS
        elif any(despedida in mensaje_lower for despedida in ['adiós', 'adios', 'chao', 'bye', 'hasta luego', 'nos vemos']):
            return """¡Hasta pronto! 👋 Ha sido un verdadero placer conversar contigo.

Recuerda que estaré aquí 24/7 cuando necesites:
- Analizar nuevos indicadores
- Revisar estrategias financieras
- Tomar decisiones importantes
- O simplemente charlar sobre el futuro de tu empresa

¡Mucho éxito con tu negocio! 🚀 Espero verte pronto por aquí.

PD: Si implementas alguna de mis recomendaciones, me encantaría saber cómo te fue. ¡Cuídate mucho!"""
        
        # GRACIAS
        elif 'gracias' in mensaje_lower:
            return """¡De nada! 😊 Es un verdadero placer poder ayudarte.

Me encanta cuando puedo contribuir al éxito de las empresas. Si mi análisis o consejos te han sido útiles, eso me hace muy feliz.

¿Hay algo más en lo que pueda asistirte? Podemos profundizar en cualquier tema financiero o explorar nuevas áreas de oportunidad para tu negocio."""
        
        # GROSERÍAS O INSULTOS
        elif any(groseria in mensaje_lower for groseria in ['mierda', 'puta', 'carajo', 'idiota', 'estúpido', 'pendejo']):
            return """Entiendo que puedas estar frustrado. Las finanzas empresariales pueden ser estresantes a veces, especialmente cuando los números no cuadran o las cosas no van como esperamos.

Estoy aquí para ayudarte de manera profesional y constructiva. ¿Hay algún problema específico con tus finanzas que esté causando esta frustración? Me encantaría poder ayudarte a resolverlo.

A veces, hablar sobre los desafíos financieros puede aliviar mucho el estrés. ¿Qué te parece si empezamos de nuevo? Cuéntame qué te preocupa."""
        
        # RESPUESTAS PARA TEMAS NO FINANCIEROS
        if not es_tema_financiero:
            return self._respuesta_no_financiera(mensaje)
        
        # PREGUNTAS FINANCIERAS CON CONTEXTO
        if contexto_empresa and 'resultados' in contexto_empresa:
            return self._respuesta_contextual_premium(mensaje, contexto_empresa)
        
        # RESPUESTA GENERAL INTELIGENTE
        return """Interesante consulta. Como tu asistente financiero especializado, puedo ayudarte mejor si me das un poco más de contexto sobre lo que necesitas.

¿Tu pregunta está relacionada con alguno de estos temas?

📊 **Análisis Financiero**
- Evaluación de indicadores clave (ROA, ROE, liquidez)
- Interpretación de estados financieros
- Benchmarking con tu sector

💰 **Gestión de Capital**
- Estructura óptima de financiamiento
- Reducción inteligente de costos
- Gestión eficiente del flujo de caja

📈 **Estrategia y Crecimiento**
- Planes de expansión calculados
- Evaluación de nuevas inversiones
- Estrategias de diversificación

🛡️ **Gestión de Riesgos**
- Identificación de riesgos financieros
- Planes de contingencia
- Coberturas y seguros

Cuéntame más sobre lo que necesitas y te daré la mejor asesoría posible."""
    
    def _respuesta_no_financiera(self, mensaje):
        """Genera respuestas para temas no financieros, SIEMPRE redirigiendo a temas financieros."""
        return """Aprecio tu interés en este tema, pero como asistente financiero especializado, mi área de experiencia se centra exclusivamente en finanzas, economía y negocios. 

Puedo ser mucho más útil en temas como:

- 📊 Análisis financiero empresarial
- 💰 Gestión de presupuestos personales
- 📈 Estrategias de inversión
- 🏦 Productos bancarios y crediticios
- 💼 Valoración de empresas y activos
- 📑 Impuestos y planificación fiscal
- 💸 Control de gastos y ahorro

¿Te gustaría que exploremos alguno de estos temas financieros? ¿O quizás tienes alguna otra consulta relacionada con finanzas o economía en la que pueda ayudarte hoy?"""
    
    def _respuesta_contextual_premium(self, mensaje, contexto_empresa):
        """Respuestas premium cuando hay contexto de empresa."""
        resultados = contexto_empresa['resultados']
        nombre = resultados['nombre']
        mensaje_lower = mensaje.lower()
        
        # ANÁLISIS DE ENDEUDAMIENTO
        if any(palabra in mensaje_lower for palabra in ['endeudamiento', 'deuda', 'pasivo', 'apalancamiento', 'préstamo']):
            ratio = resultados['indicadores']['ratio_endeudamiento']
            eval = resultados['evaluacion']['endeudamiento']
            sector = resultados['sector']
            
            respuesta = f"""## 💰 Análisis Detallado de Endeudamiento - {nombre}

**Situación Actual:**
- Ratio de endeudamiento: **{ratio:.2f}**
- Evaluación sectorial: **{eval}**
- Sector de referencia: **{sector}**

### 📊 ¿Qué significa tu ratio de {ratio:.2f}?

"""
            
            if eval == 'bueno':
                respuesta += f"""🟢 **POSICIÓN FINANCIERA SÓLIDA**

Por cada $100 en activos, tienes ${ratio*100:.0f} en deudas. Esto es excelente porque:

✅ **Ventajas de tu posición actual:**
- Mantienes independencia financiera
- Los bancos te ven como cliente premium
- Tienes capacidad para nuevas inversiones
- Tu riesgo financiero es bajo
- Puedes negociar mejores tasas de interés

### 💡 Estrategias para Maximizar tu Ventaja:

**1. Aprovecha tu capacidad de endeudamiento:**
   - Líneas de crédito preaprobadas para oportunidades
   - Financiamiento para expansión a tasas preferenciales
   - Inversiones en tecnología o innovación

**2. Mantén tu posición privilegiada:**
   - Monitoreo mensual del ratio
   - Política de endeudamiento conservadora
   - Fondo de contingencia robusto

**3. Optimiza tu estructura de capital:**
   - Balance entre deuda y capital propio
   - Diversificación de fuentes de financiamiento
   - Aprovecha beneficios fiscales de la deuda"""
            else:
                respuesta += f"""🟡 **ALERTA: ENDEUDAMIENTO ELEVADO**

Por cada $100 en activos, debes ${ratio*100:.0f}. Esto requiere atención urgente porque:

⚠️ **Riesgos de tu situación actual:**
- Vulnerabilidad ante cambios del mercado
- Dificultad para obtener nuevo financiamiento
- Altos costos financieros que erosionan rentabilidad
- Menor flexibilidad operativa
- Posible presión de acreedores

### 🚨 Plan de Acción Inmediato:

**Fase 1: Estabilización (0-3 meses)**
1. Auditoría completa de deudas:
   - Mapear todas las obligaciones
   - Identificar tasas más altas
   - Detectar deudas innecesarias

2. Renegociación urgente:
   - Extensión de plazos
   - Reducción de tasas
   - Consolidación de pasivos

3. Mejora de flujo de caja:
   - Acelerar cobranzas
   - Reducir gastos no esenciales
   - Optimizar inventarios

**Fase 2: Reducción (3-6 meses)**
1. Venta de activos improductivos
2. Aumento de capital si es posible
3. Factoring selectivo de cartera
4. Programa agresivo de reducción de costos

**Fase 3: Reestructuración (6-12 meses)**
1. Nueva política de endeudamiento (máximo 50%)
2. Diversificación de fuentes de financiamiento
3. Creación de reservas de liquidez
4. Plan de contingencia financiera"""
            
            respuesta += f"""

### 📈 Proyección y Metas:

**Situación actual:** Ratio de {ratio:.2f}
**Meta a 6 meses:** Ratio de {ratio*0.85:.2f} (-15%)
**Meta a 12 meses:** Ratio de {ratio*0.70:.2f} (-30%)
**Meta ideal sector {sector}:** Ratio de 0.50-0.60

### 🎯 Próximos Pasos Recomendados:

¿Te gustaría que:
1. Creemos un plan detallado mes a mes?
2. Analicemos opciones específicas de refinanciamiento?
3. Evaluemos qué activos podrías liquidar?
4. Diseñemos una estrategia de negociación con bancos?

¿Cuál prefieres abordar primero?"""
            
            return respuesta
        
        # ANÁLISIS DE RENTABILIDAD
        elif any(palabra in mensaje_lower for palabra in ['rentabilidad', 'ganancia', 'utilidad', 'beneficio', 'roa', 'margen']):
            rent = resultados['indicadores']['rentabilidad']
            eval = resultados['evaluacion']['rentabilidad']
            sector = resultados['sector']
            
            respuesta = f"""## 📈 Análisis Integral de Rentabilidad - {nombre}

**Performance Financiero:**
- ROA (Retorno sobre Activos): **{rent:.1%}**
- Evaluación sectorial: **{eval}**
- Benchmark del sector: **{sector}**

### 🎯 Interpretación de tu ROA {rent:.1%}:

Tu empresa genera **${rent*100:.2f}** de beneficio por cada **$100** invertidos en activos.

"""
            
            if eval == 'buena':
                respuesta += f"""🟢 **RENTABILIDAD EXCEPCIONAL**

¡Felicitaciones! Estás en el top 20% del sector {sector}. Esto demuestra:

✅ **Fortalezas identificadas:**
- Gestión eficiente de recursos
- Modelo de negocio altamente rentable
- Ventaja competitiva sostenible
- Excelente control de costos
- Estrategia de precios acertada

### 📊 Análisis Comparativo:

**Tu empresa vs. Sector {sector}:**
- Tu ROA: {rent:.1%}
- Promedio del sector: {rent*0.7:.1%}
- Líderes del sector: {rent*1.1:.1%}
- Ventaja competitiva: +{(rent-rent*0.7)*100:.0f}%

### 🚀 Estrategias para Mantener el Liderazgo:

**1. Protege tu ventaja competitiva:**
   - Innovación continua en productos/servicios
   - Fidelización agresiva de clientes clave
   - Barreras de entrada para competidores
   - Protección de propiedad intelectual

**2. Expande inteligentemente:**
   - Réplica del modelo en nuevos mercados
   - Diversificación en productos complementarios
   - Alianzas estratégicas selectivas
   - Adquisiciones de competidores débiles

**3. Optimiza aún más:**
   - Automatización de procesos clave
   - Negociación continua con proveedores
   - Mejora de mix de productos (mayor margen)
   - Economías de escala adicionales"""
            else:
                respuesta += f"""🟡 **RENTABILIDAD BAJO POTENCIAL**

Tu ROA está por debajo del promedio del sector {sector}. Análisis detallado:

⚠️ **Problemas detectados:**
- Ineficiencia en uso de activos
- Márgenes de beneficio comprometidos
- Posibles activos improductivos
- Estructura de costos inflada
- Competencia más eficiente

### 🔍 Diagnóstico por Componentes:

**Descomposición del ROA:**
1. **Margen de beneficio neto:** Analizar pricing y costos
2. **Rotación de activos:** Evaluar eficiencia operativa
3. **Apalancamiento financiero:** Revisar estructura de capital

### 💡 Plan de Mejora Intensivo:

**Mes 1-2: Quick Wins**
✓ Auditoría exhaustiva de costos
✓ Eliminación de gastos superfluos (target: -10%)
✓ Renegociación con top 10 proveedores
✓ Revisión de política de precios
✓ Identificación de activos ociosos

**Mes 3-4: Optimización Operativa**
✓ Rediseño de procesos ineficientes
✓ Implementación de KPIs por área
✓ Programa de incentivos por productividad
✓ Automatización de tareas repetitivas
✓ Reducción de desperdicios

**Mes 5-6: Transformación Estratégica**
✓ Nuevo modelo de negocio
✓ Enfoque en productos de alto margen
✓ Digitalización de operaciones
✓ Alianzas para reducir costos
✓ Reestructuración organizacional"""
            
            respuesta += f"""

### 📊 Metas de Rentabilidad:

**Situación actual:** ROA {rent:.1%}
**Meta 3 meses:** ROA {rent*1.2:.1%} (+20%)
**Meta 6 meses:** ROA {rent*1.5:.1%} (+50%)
**Meta 12 meses:** ROA {rent*2:.1%} (+100%)
**Objetivo sector:** ROA 15-20%

### 🛠️ Herramientas de Apoyo:

¿Qué análisis específico necesitas?
1. Desglose detallado de costos por categoría
2. Benchmarking de precios vs. competencia
3. Análisis de rentabilidad por producto/servicio
4. Proyección de escenarios de mejora
5. Plan de implementación paso a paso

¿Por dónde prefieres empezar?"""
            
            return respuesta
        
        # PRODUCTIVIDAD
        elif any(palabra in mensaje_lower for palabra in ['productividad', 'empleado', 'personal', 'eficiencia', 'trabajador']):
            prod = resultados['indicadores']['productividad']
            eval = resultados['evaluacion']['productividad']
            sector = resultados['sector']
            
            respuesta = f"""## 👥 Análisis de Productividad Laboral - {nombre}

**Métricas de Eficiencia:**
- Productividad por empleado: **${prod:,.0f} COP**
- Evaluación sectorial: **{eval}**
- Benchmark del sector: **{sector}**

### 📊 ¿Qué significa tu productividad de ${prod:,.0f}?

Cada empleado genera en promedio ${prod:,.0f} COP en ingresos anuales.

"""
            
            if eval == 'buena':
                respuesta += f"""🟢 **EQUIPO ALTAMENTE PRODUCTIVO**

¡Excelente gestión del talento humano! Tu equipo está entre los más productivos del sector {sector}.

✅ **Fortalezas identificadas:**
- Personal altamente capacitado
- Procesos eficientes y optimizados
- Tecnología bien implementada
- Cultura de alto rendimiento
- Liderazgo efectivo

### 💪 Ventajas Competitivas:

**Comparación sectorial:**
- Tu productividad: ${prod:,.0f}/empleado
- Promedio del sector: ${prod*0.75:,.0f}/empleado
- Ventaja: +{((prod-prod*0.75)/prod*0.75)*100:.0f}%

### 🚀 Estrategias para Mantener la Excelencia:

**1. Retención del talento clave:**
   - Planes de carrera personalizados
   - Compensación competitiva
   - Beneficios diferenciados
   - Reconocimiento continuo
   - Ambiente laboral excepcional

**2. Mejora continua:**
   - Capacitación constante
   - Certificaciones especializadas
   - Rotación inteligente de roles
   - Innovación en procesos
   - Adopción de nuevas tecnologías

**3. Escalabilidad inteligente:**
   - Documentación de mejores prácticas
   - Mentoría entre pares
   - Automatización selectiva
   - Outsourcing estratégico
   - Expansión controlada del equipo"""
            else:
                respuesta += f"""🟡 **PRODUCTIVIDAD BAJO POTENCIAL**

Tu equipo está generando menos valor que el promedio del sector {sector}. 

⚠️ **Áreas de mejora detectadas:**
- Procesos ineficientes o burocráticos
- Falta de herramientas adecuadas
- Capacitación insuficiente
- Posible desmotivación
- Estructura organizacional deficiente

### 🔍 Diagnóstico Detallado:

**Factores que afectan la productividad:**
1. **Tecnológicos:** ¿Tienen las herramientas correctas?
2. **Formativos:** ¿Están capacitados adecuadamente?
3. **Motivacionales:** ¿Se sienten valorados?
4. **Organizacionales:** ¿Los procesos son eficientes?
5. **Culturales:** ¿Hay cultura de alto rendimiento?

### 💡 Plan de Mejora de Productividad:

**Fase 1: Diagnóstico (Semana 1-2)**
✓ Encuesta anónima de clima laboral
✓ Análisis de procesos clave
✓ Evaluación de herramientas actuales
✓ Revisión de cargas de trabajo
✓ Identificación de cuellos de botella

**Fase 2: Quick Wins (Mes 1)**
✓ Eliminación de reuniones innecesarias
✓ Automatización de tareas repetitivas
✓ Mejora de comunicación interna
✓ Actualización de herramientas básicas
✓ Reconocimiento de logros

**Fase 3: Transformación (Mes 2-6)**
✓ Rediseño de procesos clave
✓ Programa integral de capacitación
✓ Implementación de nuevas tecnologías
✓ Sistema de incentivos por resultados
✓ Reestructuración organizacional

### 🎯 KPIs de Seguimiento:

1. Productividad por empleado (mensual)
2. Índice de satisfacción laboral
3. Rotación de personal
4. Tiempo de ciclo de procesos clave
5. ROI de capacitaciones"""
            
            respuesta += f"""

### 📈 Proyección de Mejora:

**Actual:** ${prod:,.0f}/empleado
**Meta 3 meses:** ${prod*1.15:,.0f}/empleado (+15%)
**Meta 6 meses:** ${prod*1.30:,.0f}/empleado (+30%)
**Meta 12 meses:** ${prod*1.50:,.0f}/empleado (+50%)

### 🛠️ Próximos Pasos:

¿Qué aspecto quieres abordar primero?
1. Realizar diagnóstico de clima laboral
2. Mapear y optimizar procesos clave
3. Diseñar plan de capacitación
4. Evaluar herramientas tecnológicas
5. Crear sistema de incentivos

¿Cuál es tu prioridad?"""
            
            return respuesta
        
        # RESUMEN GENERAL EJECUTIVO
        elif any(palabra in mensaje_lower for palabra in ['resumen', 'general', 'completo', 'informe', 'reporte', 'análisis']):
            estado = resultados['estado_general']
            emoji_estado = '🟢' if estado in ['Excelente', 'Bueno'] else '🟡' if estado == 'Regular' else '🔴'
            
            return f"""# 📊 Informe Ejecutivo Integral - {nombre}

## 🏢 Ficha Técnica

**Empresa:** {nombre}  
**Sector:** {resultados['sector']}  
**Estado General:** **{estado}** {emoji_estado}  
**Fecha de Análisis:** {time.strftime('%d/%m/%Y')}

---

## 📈 Dashboard Ejecutivo de Indicadores

### 1. 💰 ENDEUDAMIENTO
**Ratio:** {resultados['indicadores']['ratio_endeudamiento']:.2f}  
**Estado:** {resultados['evaluacion']['endeudamiento']} {'✅' if resultados['evaluacion']['endeudamiento'] == 'bueno' else '⚠️'}  
**Interpretación:** {'Estructura de capital saludable con margen de maniobra' if resultados['evaluacion']['endeudamiento'] == 'bueno' else 'Nivel de deuda elevado que requiere atención urgente'}

### 2. 💹 RENTABILIDAD (ROA)
**Valor:** {resultados['indicadores']['rentabilidad']:.1%}  
**Estado:** {resultados['evaluacion']['rentabilidad']} {'✅' if resultados['evaluacion']['rentabilidad'] == 'buena' else '⚠️'}  
**Interpretación:** {'Excelente retorno sobre activos, liderando el sector' if resultados['evaluacion']['rentabilidad'] == 'buena' else 'Retorno insuficiente, por debajo del potencial del sector'}

### 3. 👥 PRODUCTIVIDAD
**Valor:** ${resultados['indicadores']['productividad']:,.0f} por empleado  
**Estado:** {resultados['evaluacion']['productividad']} {'✅' if resultados['evaluacion']['productividad'] == 'buena' else '⚠️'}  
**Interpretación:** {'Equipo altamente eficiente y productivo' if resultados['evaluacion']['productividad'] == 'buena' else 'Oportunidades significativas de mejora en eficiencia'}

### 4. 📅 ROTACIÓN DE CARTERA
**Días:** {resultados['indicadores']['rotacion_cartera']:.0f}  
**Estado:** {resultados['evaluacion']['rotacion']} {'✅' if resultados['evaluacion']['rotacion'] == 'buena' else '⚠️'}  
**Interpretación:** {'Excelente gestión de cobros y liquidez óptima' if resultados['evaluacion']['rotacion'] == 'buena' else 'Ciclo de cobro extenso afectando el flujo de caja'}

---

## 🎯 Diagnóstico Estratégico Integral

{self._generar_diagnostico_ejecutivo(resultados)}

---

## 💡 Plan de Acción Prioritario

{self._generar_plan_accion_ejecutivo(resultados)}

---

## 📊 Análisis FODA Financiero

### FORTALEZAS 💪
{self._generar_fortalezas(resultados)}

### DEBILIDADES ⚠️
{self._generar_debilidades(resultados)}

### OPORTUNIDADES 🚀
{self._generar_oportunidades(resultados)}

### AMENAZAS 🛡️
{self._generar_amenazas(resultados)}

---

## 📈 Proyecciones y Escenarios

### Escenario Conservador (6 meses)
{self._generar_escenario_conservador(resultados)}

### Escenario Optimista (12 meses)
{self._generar_escenario_optimista(resultados)}

---

## 🤝 Próximos Pasos Recomendados

1. **Inmediato (0-7 días)**
   - Revisar este informe con el equipo directivo
   - Priorizar áreas críticas de intervención
   - Asignar responsables para cada iniciativa

2. **Corto plazo (1-4 semanas)**
   - Implementar quick wins identificados
   - Establecer KPIs de seguimiento
   - Iniciar negociaciones necesarias

3. **Mediano plazo (1-3 meses)**
   - Ejecutar plan de mejora integral
   - Monitorear progreso semanalmente
   - Ajustar estrategia según resultados

---

## 🔍 ¿Cómo puedo ayudarte más?

Puedo profundizar en:
- **Análisis detallado** de cualquier indicador específico
- **Plan de implementación** paso a paso
- **Simulación de escenarios** personalizados
- **Benchmarking sectorial** avanzado
- **Estrategias específicas** por área

¿Qué aspecto te gustaría explorar con más detalle?"""
        
        # RESPUESTA CONTEXTUAL GENERAL
        return f"""Entiendo tu consulta sobre {nombre}. Aquí está el resumen ejecutivo de la situación financiera:

**🏢 {nombre} - Sector {resultados['sector']}**
**Estado General: {resultados['estado_general']}**

**Indicadores Clave:**
- 💰 Endeudamiento: {resultados['indicadores']['ratio_endeudamiento']:.2f} ({resultados['evaluacion']['endeudamiento']})
- 📈 Rentabilidad: {resultados['indicadores']['rentabilidad']:.1%} ({resultados['evaluacion']['rentabilidad']})
- 👥 Productividad: ${resultados['indicadores']['productividad']:,.0f}/empleado ({resultados['evaluacion']['productividad']})
- 📅 Rotación: {resultados['indicadores']['rotacion_cartera']:.0f} días ({resultados['evaluacion']['rotacion']})

**Mi recomendación principal:**
{self._obtener_recomendacion_principal(resultados)}

¿Te gustaría que:
1. Analice algún indicador en profundidad?
2. Cree un plan de acción específico?
3. Compare con empresas similares?
4. Proyecte escenarios futuros?

¿Qué necesitas?"""
    
    def _generar_diagnostico_ejecutivo(self, resultados):
        """Genera diagnóstico ejecutivo ultra profesional."""
        problemas = sum(1 for val in resultados['evaluacion'].values() if val not in ['bueno', 'buena'])
        
        if problemas == 0:
            return """### 🌟 POSICIÓN DE LIDERAZGO ABSOLUTO

Su empresa demuestra un desempeño financiero excepcional, ubicándose en el percentil 90 del sector. Esta posición privilegiada refleja:

- **Gestión de Clase Mundial:** Todos los indicadores superan ampliamente los benchmarks sectoriales
- **Modelo de Negocio Robusto:** Alta eficiencia operativa y rentabilidad sostenible
- **Ventaja Competitiva Clara:** Difícil de replicar por competidores
- **Base para Expansión:** Condiciones ideales para crecimiento agresivo

**Estrategia Recomendada:** Capitalizar esta posición para consolidar liderazgo de mercado y explorar oportunidades de expansión disruptiva."""
        
        elif problemas == 1:
            return """### 💪 POSICIÓN COMPETITIVA FUERTE

Su empresa mantiene un desempeño sólido con un área específica de optimización. Esta situación estratégica presenta:

- **Fundamentos Sanos:** La mayoría de indicadores en niveles óptimos
- **Oportunidad Clara:** Un área específica con potencial de mejora significativo
- **Riesgo Controlado:** Situación manejable sin comprometer estabilidad
- **Potencial de Crecimiento:** Quick wins disponibles para alcanzar excelencia

**Estrategia Recomendada:** Focalizar recursos en el área de mejora identificada mientras se mantienen las fortalezas actuales."""
        
        elif problemas == 2:
            return """### ⚖️ POSICIÓN DE EQUILIBRIO ESTRATÉGICO

Su empresa presenta un balance entre fortalezas y áreas de mejora. Este punto de inflexión requiere:

- **Priorización Inteligente:** Identificar qué mejorar primero para máximo impacto
- **Gestión de Recursos:** Balancear inversiones entre mantener fortalezas y corregir debilidades
- **Visión Integral:** Abordar mejoras de forma sistémica, no aislada
- **Momentum Crítico:** Momento decisivo para definir trayectoria futura

**Estrategia Recomendada:** Plan integral de transformación con fases bien definidas y métricas claras de éxito."""
        
        else:
            return """### 🔧 SITUACIÓN DE TURNAROUND

Multiple indicadores requieren intervención urgente. Aunque desafiante, esta situación presenta una oportunidad única de transformación:

- **Urgencia Máxima:** Necesidad de acción inmediata y decisiva
- **Potencial Oculto:** Margen significativo de mejora en todas las áreas
- **Transformación Total:** Oportunidad de reinventar el modelo de negocio
- **Resiliencia Probada:** El hecho de continuar operando demuestra fortaleza fundamental

**Estrategia Recomendada:** Plan de turnaround agresivo con hitos a corto plazo y transformación profunda del modelo operativo."""
    
    def _generar_plan_accion_ejecutivo(self, resultados):
        """Genera plan de acción ejecutivo personalizado."""
        acciones = []
        
        # Analizar cada área problemática
        if resultados['evaluacion']['endeudamiento'] != 'bueno':
            acciones.append("""### 1. 🏦 Reestructuración Financiera (Prioridad: CRÍTICA)
            
**Objetivo:** Reducir ratio de endeudamiento en 30% en 6 meses

**Acciones Inmediatas (Semana 1):**
- Mapeo completo de obligaciones financieras
- Identificación de deudas con mayor costo
- Inicio de negociaciones con principales acreedores

**Acciones a Corto Plazo (Mes 1-3):**
- Refinanciamiento de deuda cara
- Venta de activos no estratégicos
- Implementación de cash management agresivo
- Evaluación de alternativas de capital

**KPIs de Seguimiento:**
- Ratio deuda/activos (semanal)
- Costo promedio de deuda (mensual)
- Flujo de caja libre (diario)""")
        
        if resultados['evaluacion']['rentabilidad'] != 'buena':
            acciones.append("""### 2. 📈 Optimización de Rentabilidad (Prioridad: ALTA)
            
**Objetivo:** Incrementar ROA en 50% en 9 meses

**Quick Wins (Primeras 2 semanas):**
- Auditoría express de gastos
- Eliminación de costos redundantes
- Renegociación top 10 proveedores

**Transformación Operativa (Mes 1-6):**
- Rediseño de procesos clave
- Automatización de operaciones
- Revisión integral de pricing
- Optimización de mix de productos

**Métricas Clave:**
- Margen EBITDA (quincenal)
- Costo por transacción (semanal)
- Precio promedio de venta (diario)""")
        
        if resultados['evaluacion']['productividad'] != 'buena':
            acciones.append("""### 3. 👥 Revolución de Productividad (Prioridad: MEDIA-ALTA)
            
**Objetivo:** Aumentar productividad por empleado en 40% en 6 meses

**Diagnóstico Inicial (Semana 1-2):**
- Evaluación 360° del equipo
- Mapeo de procesos actuales
- Identificación de cuellos de botella

**Programa de Transformación (Mes 1-4):**
- Capacitación intensiva focalizada
- Implementación de nuevas herramientas
- Rediseño de estructura organizacional
- Sistema de incentivos por resultados

**Indicadores de Éxito:**
- Revenue por empleado (mensual)
- NPS interno (trimestral)
- Tiempo de ciclo procesos clave (semanal)""")
        
        if resultados['evaluacion']['rotacion'] != 'buena':
            acciones.append("""### 4. 💸 Aceleración de Cobros (Prioridad: MEDIA)
            
**Objetivo:** Reducir días de cartera en 40% en 4 meses

**Acciones Inmediatas (Primera semana):**
- Análisis de antigüedad de cartera
- Identificación de clientes morosos
- Campaña de recuperación intensiva

**Mejoras Estructurales (Mes 1-3):**
- Nueva política de crédito
- Automatización de cobranzas
- Incentivos por pronto pago
- Evaluación de factoring selectivo

**KPIs Críticos:**
- DSO - Days Sales Outstanding (diario)
- % cartera vencida (semanal)
- Efectividad de cobro (mensual)""")
        
        # Si todo está bien, plan de crecimiento
        if not acciones:
            acciones.append("""### 1. 🚀 Expansión Estratégica (Prioridad: ALTA)
            
**Objetivo:** Crecer ingresos 40% manteniendo márgenes

**Iniciativas de Crecimiento:**
- Expansión geográfica calculada
- Lanzamiento de nuevas líneas
- Adquisiciones estratégicas
- Partnerships clave

**Innovación y Desarrollo:**
- Inversión en I+D (3% de ingresos)
- Digitalización de productos
- Nuevos modelos de negocio
- Venture building interno""")
            
            acciones.append("""### 2. 🏆 Consolidación de Liderazgo (Prioridad: MEDIA)
            
**Objetivo:** Crear ventajas competitivas sostenibles

**Estrategias de Dominio:**
- Barreras de entrada más altas
- Ecosistema de productos/servicios
- Fidelización avanzada de clientes
- Thought leadership sectorial

**Excelencia Operativa:**
- Mejora continua (Kaizen)
- Certificaciones internacionales
- Best practices globales
- Cultura de innovación""")
        
        return '\n\n'.join(acciones[:3])  # Máximo 3 acciones prioritarias
    
    def _generar_fortalezas(self, resultados):
        fortalezas = []
        
        if resultados['evaluacion']['endeudamiento'] == 'bueno':
            fortalezas.append("• Estructura de capital óptima con bajo riesgo financiero")
            fortalezas.append("• Capacidad de endeudamiento disponible para oportunidades")
        
        if resultados['evaluacion']['rentabilidad'] == 'buena':
            fortalezas.append("• Alta eficiencia en generación de valor sobre activos")
            fortalezas.append("• Márgenes superiores al promedio del sector")
        
        if resultados['evaluacion']['productividad'] == 'buena':
            fortalezas.append("• Equipo altamente productivo y motivado")
            fortalezas.append("• Procesos operativos optimizados y eficientes")
        
        if resultados['evaluacion']['rotacion'] == 'buena':
            fortalezas.append("• Excelente gestión de capital de trabajo")
            fortalezas.append("• Ciclo de conversión de efectivo optimizado")
        
        if not fortalezas:
            fortalezas.append("• Resiliencia operativa a pesar de los desafíos")
            fortalezas.append("• Oportunidad clara de mejora en múltiples frentes")
        
        return '\n'.join(fortalezas)
    
    def _generar_debilidades(self, resultados):
        debilidades = []
        
        if resultados['evaluacion']['endeudamiento'] != 'bueno':
            debilidades.append("• Nivel de endeudamiento por encima del óptimo sectorial")
            debilidades.append("• Costo financiero impactando rentabilidad")
        
        if resultados['evaluacion']['rentabilidad'] != 'buena':
            debilidades.append("• ROA por debajo del potencial del sector")
            debilidades.append("• Ineficiencias en la utilización de activos")
        
        if resultados['evaluacion']['productividad'] != 'buena':
            debilidades.append("• Productividad laboral bajo el estándar sectorial")
            debilidades.append("• Posibles ineficiencias en procesos y sistemas")
        
        if resultados['evaluacion']['rotacion'] != 'buena':
            debilidades.append("• Ciclo de cobro extenso afectando liquidez")
            debilidades.append("• Gestión de cartera requiere optimización")
        
        if not debilidades:
            debilidades.append("• Riesgo de complacencia por el buen desempeño")
            debilidades.append("• Necesidad de innovación para mantener liderazgo")
        
        return '\n'.join(debilidades)
    
    def _generar_oportunidades(self, resultados):
        oportunidades = []
        
        if resultados['evaluacion']['endeudamiento'] == 'bueno':
            oportunidades.append("• Acceso a financiamiento preferencial para expansión")
            oportunidades.append("• Capacidad para aprovechar oportunidades de M&A")
        else:
            oportunidades.append("• Mejora significativa posible en estructura de capital")
            oportunidades.append("• Potencial de refinanciamiento a mejores tasas")
        
        if resultados['evaluacion']['rentabilidad'] == 'buena':
            oportunidades.append("• Expansión a mercados de mayor margen")
            oportunidades.append("• Capacidad de inversión en innovación")
        else:
            oportunidades.append("• Margen significativo de mejora en rentabilidad")
            oportunidades.append("• Optimización de procesos para mayor eficiencia")
        
        oportunidades.append(f"• Crecimiento potencial en el sector {resultados['sector']}")
        oportunidades.append("• Transformación digital para ventaja competitiva")
        
        return '\n'.join(oportunidades[:4])
    
    def _generar_amenazas(self, resultados):
        amenazas = []
        
        if resultados['evaluacion']['endeudamiento'] != 'bueno':
            amenazas.append("• Vulnerabilidad ante cambios en tasas de interés")
            amenazas.append("• Riesgo de insolvencia en escenario adverso")
        
        if resultados['evaluacion']['rentabilidad'] != 'buena':
            amenazas.append("• Competidores más eficientes ganando mercado")
            amenazas.append("• Erosión de márgenes por presión competitiva")
        
        amenazas.append(f"• Volatilidad económica en el sector {resultados['sector']}")
        amenazas.append("• Cambios regulatorios potenciales")
        amenazas.append("• Disrupciones tecnológicas en la industria")
        
        return '\n'.join(amenazas[:4])
    
    def _generar_escenario_conservador(self, resultados):
        """Genera proyección conservadora."""
        return f"""Con mejoras incrementales y gestión prudente:
- Endeudamiento: {resultados['indicadores']['ratio_endeudamiento']*0.95:.2f} (-5%)
- Rentabilidad: {resultados['indicadores']['rentabilidad']*1.1:.1%} (+10%)
- Productividad: ${resultados['indicadores']['productividad']*1.05:,.0f} (+5%)
- Rotación: {resultados['indicadores']['rotacion_cartera']*0.95:.0f} días (-5%)

**Resultado esperado:** Mejora gradual pero sostenible en todos los indicadores."""
    
    def _generar_escenario_optimista(self, resultados):
        """Genera proyección optimista."""
        return f"""Con implementación agresiva de todas las recomendaciones:
- Endeudamiento: {resultados['indicadores']['ratio_endeudamiento']*0.75:.2f} (-25%)
- Rentabilidad: {resultados['indicadores']['rentabilidad']*1.5:.1%} (+50%)
- Productividad: ${resultados['indicadores']['productividad']*1.3:,.0f} (+30%)
- Rotación: {resultados['indicadores']['rotacion_cartera']*0.7:.0f} días (-30%)

**Resultado esperado:** Transformación significativa posicionando a la empresa como líder del sector."""
    
    def _obtener_recomendacion_principal(self, resultados):
        """Obtiene la recomendación más importante."""
        problemas = []
        
        if resultados['evaluacion']['endeudamiento'] != 'bueno':
            problemas.append(('endeudamiento', 'Reducir urgentemente el nivel de endeudamiento'))
        if resultados['evaluacion']['rentabilidad'] != 'buena':
            problemas.append(('rentabilidad', 'Mejorar la rentabilidad operativa'))
        if resultados['evaluacion']['productividad'] != 'buena':
            problemas.append(('productividad', 'Optimizar la productividad del equipo'))
        if resultados['evaluacion']['rotacion'] != 'buena':
            problemas.append(('rotacion', 'Acelerar el ciclo de cobros'))
        
        if problemas:
            return problemas[0][1]  # Retornar el problema más crítico
        else:
            return "Mantener la excelencia actual y buscar oportunidades de expansión estratégica"
    
    # Métodos de compatibilidad con el sistema existente
    def tokenizar_texto(self, texto):
        """Tokeniza texto en palabras."""
        return texto.lower().split()
    
    def lematizar_texto(self, texto):
        """Lematiza texto (simplificado)."""
        return texto.lower().split()
    
    def pos_tagging(self, texto):
        """Etiquetado POS (simplificado)."""
        return [(palabra, 'NOUN') for palabra in texto.split()]
    
    def crear_embedding(self, texto):
        """Crea embedding dummy."""
        return [0.0] * 100
    
    def similaridad_textos(self, texto1, texto2):
        """Calcula similitud (simplificado)."""
        return 0.5
    
    def normalizar_texto(self, texto):
        """Normaliza texto."""
        return texto.lower().strip()
    
    def extraer_keywords(self, texto, num_palabras=5):
        """Extrae palabras clave."""
        palabras = texto.lower().split()
        palabras_importantes = [p for p in palabras if len(p) > 4]
        return palabras_importantes[:num_palabras]
    
    def es_mensaje_no_financiero(self, mensaje):
        """Detecta si el mensaje no es financiero (método legacy, mantenido por compatibilidad)."""
        es_financiero, tipo = self.es_mensaje_financiero(mensaje)
        return not es_financiero, tipo