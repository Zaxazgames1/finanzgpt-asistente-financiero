import streamlit as st
from models.empresa import Empresa
from models.analisis import ResultadoAnalisis

class ConversationalAnalyzer:
    """
    Maneja la recopilación de datos de manera conversacional
    y asegura que las respuestas estén enfocadas EXCLUSIVAMENTE en temas financieros
    """
    def __init__(self, analizador_financiero, nlp_service):
        self.analizador_financiero = analizador_financiero
        self.nlp_service = nlp_service
        
        # Estados de la conversación
        self.ESTADOS = {
            'INICIO': 'inicio',
            'NOMBRE': 'nombre',
            'SECTOR': 'sector',
            'GANANCIAS': 'ganancias',
            'EMPLEADOS': 'empleados',
            'ACTIVOS': 'activos',
            'CARTERA': 'cartera',
            'DEUDAS': 'deudas',
            'CONFIRMACION': 'confirmacion',
            'ANALISIS': 'analisis',
            'COMPLETADO': 'completado'
        }
        
        # Inicializar estado de conversación
        if 'estado_conversacion' not in st.session_state:
            st.session_state.estado_conversacion = self.ESTADOS['INICIO']
        
        if 'datos_recopilados' not in st.session_state:
            st.session_state.datos_recopilados = {}
        
        # Lista ampliada de temas prohibidos (tomar de nlp_service para mantener consistencia)
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
    
    def detectar_intencion_analisis(self, mensaje):
        """Detecta si el usuario quiere iniciar un análisis"""
        mensaje_lower = mensaje.lower()
        palabras_clave_analisis = [
            'analizar', 'análisis', 'analisis', 'empresa', 'finanzas', 
            'ayuda', 'evaluar', 'revisar', 'estudiar', 'examinar',
            'diagnóstico', 'diagnostico', 'estado financiero',
            'situación financiera', 'indicadores', 'métricas',
            'iniciar análisis', 'comenzar análisis', 'empezar análisis',
            'quiero analizar', 'necesito analizar', 'deseo analizar',
            'evalúa', 'diagnostica', 'chequea', 'revisa finanzas'
        ]
        
        return any(palabra in mensaje_lower for palabra in palabras_clave_analisis)
    
    def detectar_intencion_tema_no_financiero(self, mensaje):
        """
        Detecta si el usuario está preguntando sobre un tema no financiero
        Versión mejorada para ser más estricta
        """
        # Verificar si hay temas prohibidos explícitamente
        mensaje_lower = mensaje.lower()
        for tema in self.temas_prohibidos:
            if tema in mensaje_lower:
                return True, "prohibido"
                
        # Usar el método del servicio NLP para determinar si es un tema financiero
        es_financiero, tipo = self.nlp_service.es_mensaje_financiero(mensaje)
        return not es_financiero, tipo
    
    def procesar_respuesta(self, mensaje):
        """
        Procesa la respuesta del usuario según el estado actual
        """
        estado_actual = st.session_state.estado_conversacion
        
        # Detectar temas prohibidos directamente y responder con redirección
        mensaje_lower = mensaje.lower()
        if any(tema in mensaje_lower for tema in self.temas_prohibidos):
            return """Aprecio tu interés en este tema, pero como asistente financiero especializado, mi área de experiencia se centra exclusivamente en finanzas, economía y negocios. 

Aunque me encantaría ayudarte con esta consulta específica, te puedo ser mucho más útil en temas como:

- 📊 Análisis financiero empresarial
- 💰 Gestión de presupuestos personales
- 📈 Estrategias de inversión
- 🏦 Productos bancarios y crediticios
- 💼 Valoración de empresas y activos
- 📑 Impuestos y planificación fiscal
- 💸 Control de gastos y ahorro

¿Te gustaría que exploremos alguno de estos temas financieros? ¿O quizás tienes alguna otra consulta relacionada con finanzas o economía en la que pueda ayudarte hoy?"""
        
        # Si es un tema no financiero y estamos en estado COMPLETADO o INICIO,
        # generar una respuesta para temas no financieros pero mantener el estado
        if estado_actual in [self.ESTADOS['COMPLETADO'], self.ESTADOS['INICIO']]:
            es_no_financiero, tipo = self.detectar_intencion_tema_no_financiero(mensaje)
            if es_no_financiero and tipo != "conversacional":
                return self.nlp_service._respuesta_no_financiera(mensaje)
        
        # Continuar con el flujo de conversación normal
        if estado_actual == self.ESTADOS['INICIO']:
            return self._manejar_inicio(mensaje)
        elif estado_actual == self.ESTADOS['NOMBRE']:
            return self._manejar_nombre(mensaje)
        elif estado_actual == self.ESTADOS['SECTOR']:
            return self._manejar_sector(mensaje)
        elif estado_actual == self.ESTADOS['GANANCIAS']:
            return self._manejar_ganancias(mensaje)
        elif estado_actual == self.ESTADOS['EMPLEADOS']:
            return self._manejar_empleados(mensaje)
        elif estado_actual == self.ESTADOS['ACTIVOS']:
            return self._manejar_activos(mensaje)
        elif estado_actual == self.ESTADOS['CARTERA']:
            return self._manejar_cartera(mensaje)
        elif estado_actual == self.ESTADOS['DEUDAS']:
            return self._manejar_deudas(mensaje)
        elif estado_actual == self.ESTADOS['CONFIRMACION']:
            return self._manejar_confirmacion(mensaje)
        elif estado_actual == self.ESTADOS['COMPLETADO']:
            return self._manejar_completado(mensaje)
        else:
            return "Lo siento, algo salió mal. ¿Podemos empezar de nuevo?"
    
    def _manejar_inicio(self, mensaje):
        """Maneja el estado inicial"""
        if self.detectar_intencion_analisis(mensaje):
            st.session_state.estado_conversacion = self.ESTADOS['NOMBRE']
            return """¡Excelente decisión! 🎯 Voy a ayudarte a realizar un análisis financiero completo de tu empresa.

Te haré 7 preguntas sencillas sobre tu empresa para poder generar:
- 📊 Indicadores financieros clave
- 📈 Gráficas visuales de tu situación
- 💡 Recomendaciones personalizadas
- 🎯 Plan de acción específico

Todo el proceso tomará menos de 5 minutos.

📝 **Comencemos con la información básica**

**Pregunta 1 de 7:** ¿Cuál es el nombre de tu empresa?"""
        else:
            return self.nlp_service.generar_respuesta_chat(mensaje)
    
    def _manejar_nombre(self, mensaje):
        """Maneja el nombre de la empresa"""
        nombre = mensaje.strip()
        
        if len(nombre) < 2:
            return "Por favor, ingresa un nombre válido para tu empresa. Puede ser el nombre comercial o razón social."
        
        st.session_state.datos_recopilados['nombre'] = nombre
        st.session_state.estado_conversacion = self.ESTADOS['SECTOR']
        
        return f"""¡Perfecto! **{nombre}** - me gusta ese nombre. 🏢

📊 **Pregunta 2 de 7: Sector Económico**

¿En qué sector opera {nombre}? Por favor selecciona una opción o escribe el nombre:

1️⃣ **Tecnología** (Software, IT, desarrollo)
2️⃣ **Comercio** (Retail, ventas, distribución)
3️⃣ **Manufactura** (Producción, fábricas)
4️⃣ **Servicios** (Consultoría, salud, educación)
5️⃣ **Otro** (Especificar)

Solo escribe el número o el nombre del sector."""
    
    def _manejar_sector(self, mensaje):
        """Maneja el sector de la empresa"""
        mensaje_lower = mensaje.lower().strip()
        
        sectores = {
            '1': 'Tecnología',
            'tecnología': 'Tecnología',
            'tecnologia': 'Tecnología',
            'tech': 'Tecnología',
            'it': 'Tecnología',
            'software': 'Tecnología',
            '2': 'Comercio',
            'comercio': 'Comercio',
            'retail': 'Comercio',
            'ventas': 'Comercio',
            '3': 'Manufactura',
            'manufactura': 'Manufactura',
            'producción': 'Manufactura',
            'produccion': 'Manufactura',
            'fábrica': 'Manufactura',
            'fabrica': 'Manufactura',
            '4': 'Servicios',
            'servicios': 'Servicios',
            'consultoría': 'Servicios',
            'consultoria': 'Servicios',
            '5': 'Otro',
            'otro': 'Otro'
        }
        
        sector = None
        for key, value in sectores.items():
            if key in mensaje_lower:
                sector = value
                break
        
        if not sector:
            if len(mensaje) > 2:  # Si escribió algo específico
                sector = 'Otro'
            else:
                return """Por favor, selecciona un sector válido:
                
1️⃣ Tecnología
2️⃣ Comercio  
3️⃣ Manufactura
4️⃣ Servicios
5️⃣ Otro

Puedes escribir el número o el nombre del sector."""
        
        st.session_state.datos_recopilados['sector'] = sector
        st.session_state.estado_conversacion = self.ESTADOS['GANANCIAS']
        
        nombre = st.session_state.datos_recopilados['nombre']
        emoji_sector = {
            'Tecnología': '💻',
            'Comercio': '🛍️',
            'Manufactura': '🏭',
            'Servicios': '🏢',
            'Otro': '🌐'
        }
        
        return f"""¡Genial! {nombre} opera en el sector **{sector}** {emoji_sector.get(sector, '🏢')}

💰 **Pregunta 3 de 7: Ganancias Anuales**

¿Cuáles fueron las ganancias netas de {nombre} en el último año fiscal?
(Utilidad después de impuestos)

Ingresa el valor en pesos colombianos, solo números:
Ejemplo: 500000000 (para 500 millones)"""
    
    def _manejar_ganancias(self, mensaje):
        """Maneja las ganancias anuales"""
        try:
            # Limpiar el mensaje
            mensaje_limpio = mensaje.strip().replace(',', '').replace('$', '').replace('.', '').replace(' ', '')
            ganancias = float(mensaje_limpio)
            
            if ganancias < 0:
                return "Las ganancias no pueden ser negativas. Si tuviste pérdidas, ingresa 0. Por favor intenta de nuevo."
            
            st.session_state.datos_recopilados['ganancias'] = ganancias
            st.session_state.estado_conversacion = self.ESTADOS['EMPLEADOS']
            
            nombre = st.session_state.datos_recopilados['nombre']
            ganancias_formato = f"${ganancias:,.0f}"
            
            return f"""Excelente, {nombre} tuvo ganancias de **{ganancias_formato} COP** 💵

👥 **Pregunta 4 de 7: Número de Empleados**

¿Cuántos empleados tiene actualmente {nombre}?
(Incluye empleados directos en nómina)

Solo escribe el número:
Ejemplo: 50"""
            
        except ValueError:
            return """Por favor ingresa solo números para las ganancias.

Ejemplo correcto: 500000000
Ejemplo incorrecto: $500.000.000 o quinientos millones

Intenta de nuevo:"""
    
    def _manejar_empleados(self, mensaje):
        """Maneja el número de empleados"""
        try:
            empleados = int(mensaje.strip())
            
            if empleados < 1:
                return "El número de empleados debe ser al menos 1. ¿Cuántos empleados tienes?"
            
            st.session_state.datos_recopilados['empleados'] = empleados
            st.session_state.estado_conversacion = self.ESTADOS['ACTIVOS']
            
            nombre = st.session_state.datos_recopilados['nombre']
            
            emoji_empleados = "👤" if empleados == 1 else "👥" if empleados < 10 else "👫" if empleados < 50 else "🏢"
            
            return f"""Perfecto, {nombre} cuenta con **{empleados} empleados** {emoji_empleados}

🏦 **Pregunta 5 de 7: Activos Totales**

¿Cuál es el valor total de los activos de {nombre}?
(Suma de todos los bienes, propiedades, equipos, inversiones, etc.)

Ingresa el valor en pesos colombianos:
Ejemplo: 1500000000 (para 1,500 millones)"""
            
        except ValueError:
            return """Por favor ingresa solo el número de empleados.

Ejemplo correcto: 50
Ejemplo incorrecto: cincuenta o 50 empleados

Intenta de nuevo:"""
    
    def _manejar_activos(self, mensaje):
        """Maneja el valor de activos"""
        try:
            activos_limpio = mensaje.strip().replace(',', '').replace('$', '').replace('.', '').replace(' ', '')
            activos = float(activos_limpio)
            
            if activos < 0:
                return "El valor de los activos no puede ser negativo. Por favor ingresa un valor válido."
            
            st.session_state.datos_recopilados['activos'] = activos
            st.session_state.estado_conversacion = self.ESTADOS['CARTERA']
            
            nombre = st.session_state.datos_recopilados['nombre']
            activos_formato = f"${activos:,.0f}"
            
            return f"""Bien, {nombre} tiene activos por **{activos_formato} COP** 📊

💳 **Pregunta 6 de 7: Cartera por Cobrar**

¿Cuál es el valor de la cartera por cobrar de {nombre}?
(Dinero que te deben los clientes)

Ingresa el valor en pesos colombianos:
Ejemplo: 200000000 (para 200 millones)"""
            
        except ValueError:
            return """Por favor ingresa solo números para el valor de los activos.

Ejemplo correcto: 1500000000
Ejemplo incorrecto: $1.500.000.000

Intenta de nuevo:"""
    
    def _manejar_cartera(self, mensaje):
        """Maneja el valor de cartera"""
        try:
            cartera_limpio = mensaje.strip().replace(',', '').replace('$', '').replace('.', '').replace(' ', '')
            cartera = float(cartera_limpio)
            
            if cartera < 0:
                return "El valor de la cartera no puede ser negativo. Por favor ingresa un valor válido."
            
            st.session_state.datos_recopilados['cartera'] = cartera
            st.session_state.estado_conversacion = self.ESTADOS['DEUDAS']
            
            nombre = st.session_state.datos_recopilados['nombre']
            cartera_formato = f"${cartera:,.0f}"
            
            return f"""Anotado, {nombre} tiene **{cartera_formato} COP** en cartera por cobrar 📋

🏦 **Pregunta 7 de 7: Deudas Totales** (¡Última pregunta!)

¿Cuál es el valor total de las deudas de {nombre}?
(Préstamos bancarios, obligaciones financieras, proveedores, etc.)

Ingresa el valor en pesos colombianos:
Ejemplo: 800000000 (para 800 millones)"""
            
        except ValueError:
            return """Por favor ingresa solo números para el valor de la cartera.

Ejemplo correcto: 200000000
Ejemplo incorrecto: $200.000.000

Intenta de nuevo:"""
    
    def _manejar_deudas(self, mensaje):
        """Maneja el valor de deudas"""
        try:
            deudas_limpio = mensaje.strip().replace(',', '').replace('$', '').replace('.', '').replace(' ', '')
            deudas = float(deudas_limpio)
            
            if deudas < 0:
                return "El valor de las deudas no puede ser negativo. Si no tienes deudas, ingresa 0."
            
            st.session_state.datos_recopilados['deudas'] = deudas
            st.session_state.estado_conversacion = self.ESTADOS['CONFIRMACION']
            
            # Mostrar resumen para confirmación
            datos = st.session_state.datos_recopilados
            
            resumen = f"""¡Excelente! 🎉 He recopilado toda la información necesaria.

📊 **RESUMEN DE DATOS - {datos['nombre']}**

- **Sector:** {datos['sector']}
- **Ganancias anuales:** ${datos['ganancias']:,.0f} COP
- **Empleados:** {datos['empleados']}
- **Activos totales:** ${datos['activos']:,.0f} COP
- **Cartera por cobrar:** ${datos['cartera']:,.0f} COP
- **Deudas totales:** ${datos['deudas']:,.0f} COP

¿La información es correcta? Responde:
✅ **SI** para generar tu análisis financiero completo
❌ **NO** si necesitas corregir algún dato"""
            
            return resumen
            
        except ValueError:
            return """Por favor ingresa solo números para el valor de las deudas.

Ejemplo correcto: 800000000
Ejemplo incorrecto: $800.000.000

Intenta de nuevo:"""
    
    def _manejar_confirmacion(self, mensaje):
        """Maneja la confirmación de datos"""
        mensaje_lower = mensaje.lower().strip()
        
        if mensaje_lower in ['si', 'sí', 'yes', 's', 'correcto', 'ok', 'confirmar', 'confirmo']:
            st.session_state.estado_conversacion = self.ESTADOS['ANALISIS']
            
            # Realizar análisis
            datos = st.session_state.datos_recopilados
            empresa = Empresa(
                nombre=datos['nombre'],
                sector=datos['sector'],
                ganancias=datos['ganancias'],
                empleados=datos['empleados'],
                activos=datos['activos'],
                cartera=datos['cartera'],
                deudas=datos['deudas']
            )
            
            # Realizar análisis
            resultados = self.analizador_financiero.analizar_empresa(empresa)
            
            # Guardar resultados
            st.session_state.datos_empresa = {
                'datos': empresa.data_dict,
                'resultados': resultados.data_dict,
                'mensaje': resultados.generar_mensaje()
            }
            
            # Marcar que el análisis está completo y debe mostrarse
            st.session_state.estado_conversacion = self.ESTADOS['COMPLETADO']
            st.session_state.mostrar_analisis = True
            
            return """🔍 **Análisis completado con éxito!**

    ⚡ He calculado todos tus indicadores financieros
    📊 He generado las visualizaciones
    💡 He preparado recomendaciones personalizadas

    Aquí están los resultados de tu análisis:"""
            
        elif mensaje_lower in ['no', 'corregir', 'cambiar', 'modificar', 'editar']:
            st.session_state.estado_conversacion = self.ESTADOS['NOMBRE']
            st.session_state.datos_recopilados = {}
            return """Sin problema, empecemos de nuevo. 

📝 **Pregunta 1 de 7:** ¿Cuál es el nombre de tu empresa?"""
        else:
            return """Por favor responde:
            
✅ **SI** para confirmar los datos y generar el análisis
❌ **NO** para corregir algún dato"""
    
    def _manejar_completado(self, mensaje):
        """Maneja consultas después del análisis"""
        # Detectar temas prohibidos directamente y responder con redirección
        mensaje_lower = mensaje.lower()
        if any(tema in mensaje_lower for tema in self.temas_prohibidos):
            return """Aprecio tu interés en este tema, pero como asistente financiero especializado, mi área de experiencia se centra exclusivamente en finanzas, economía y negocios. 

Aunque me encantaría ayudarte con esta consulta específica, te puedo ser mucho más útil en temas como:

- 📊 Análisis financiero empresarial
- 💰 Gestión de presupuestos personales
- 📈 Estrategias de inversión
- 🏦 Productos bancarios y crediticios
- 💼 Valoración de empresas y activos
- 📑 Impuestos y planificación fiscal
- 💸 Control de gastos y ahorro

¿Te gustaría que exploremos alguno de estos temas financieros? ¿O quizás tienes alguna otra consulta relacionada con finanzas o economía en la que pueda ayudarte hoy?"""
            
        # Para temas no financieros enviamos una respuesta especial pero mantenemos
        # el estado de conversación en COMPLETADO
        es_no_financiero, tipo = self.detectar_intencion_tema_no_financiero(mensaje)
        if es_no_financiero and tipo != "conversacional":
            return self.nlp_service._respuesta_no_financiera(mensaje)
            
        # Para temas financieros o conversacionales, procesamos normalmente
        if 'datos_empresa' in st.session_state:
            return self.nlp_service.generar_respuesta_chat(mensaje, st.session_state.datos_empresa)
        else:
            return "Parece que hubo un error. ¿Te gustaría empezar un nuevo análisis?"
    
    def resetear_conversacion(self):
        """Resetea el estado de la conversación"""
        st.session_state.estado_conversacion = self.ESTADOS['INICIO']
        st.session_state.datos_recopilados = {}
        if 'datos_empresa' in st.session_state:
            del st.session_state.datos_empresa