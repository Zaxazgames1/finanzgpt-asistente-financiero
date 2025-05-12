import streamlit as st
import time
from models.empresa import Empresa

class FormUI:
    """
    Clase para manejar la interfaz del formulario de datos con diseño tipo Gemini.
    """
    def __init__(self, analizador_financiero, validators):
        """
        Inicializa la interfaz del formulario.
        """
        self.analizador_financiero = analizador_financiero
        self.validators = validators
    
    def mostrar_procesamiento(self):
        """Muestra una animación de procesamiento estilo Gemini"""
        placeholder = st.empty()
        
        with placeholder.container():
            st.markdown("""
                <div style="text-align: center; padding: 3rem; max-width: 400px; margin: 2rem auto;">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem; animation: pulse 2s ease-in-out infinite;">
                        <span style="background: linear-gradient(135deg, #FA8B00, #8B00FA); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🤖</span>
                    </div>
                    <div style="font-size: 1.125rem; color: var(--text-primary); margin-bottom: 1.5rem; font-weight: 500;">
                        Analizando datos financieros...
                    </div>
                    <div style="display: flex; justify-content: center; gap: 0.5rem;">
                        <div style="width: 8px; height: 8px; background-color: var(--text-muted); border-radius: 50%; animation: bounce 1.4s ease-in-out infinite;"></div>
                        <div style="width: 8px; height: 8px; background-color: var(--text-muted); border-radius: 50%; animation: bounce 1.4s ease-in-out 0.2s infinite;"></div>
                        <div style="width: 8px; height: 8px; background-color: var(--text-muted); border-radius: 50%; animation: bounce 1.4s ease-in-out 0.4s infinite;"></div>
                    </div>
                </div>
                
                <style>
                    @keyframes pulse {
                        0%, 100% { transform: scale(1); opacity: 1; }
                        50% { transform: scale(1.05); opacity: 0.8; }
                    }
                    
                    @keyframes bounce {
                        0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
                        30% { transform: translateY(-10px); opacity: 1; }
                    }
                </style>
            """, unsafe_allow_html=True)
            
            time.sleep(2)
        
        # Mostrar éxito
        placeholder.empty()
        with placeholder.container():
            st.markdown("""
                <div style="text-align: center; padding: 3rem; max-width: 400px; margin: 2rem auto;">
                    <div style="font-size: 2.5rem; color: var(--accent-green); margin-bottom: 1rem; animation: checkmark 0.6s ease-in-out;">
                        ✅
                    </div>
                    <div style="font-size: 1.125rem; color: var(--text-primary); font-weight: 500;">
                        Análisis completado exitosamente
                    </div>
                </div>
                
                <style>
                    @keyframes checkmark {
                        0% { transform: scale(0) rotate(0deg); }
                        50% { transform: scale(1.2) rotate(360deg); }
                        100% { transform: scale(1) rotate(360deg); }
                    }
                </style>
            """, unsafe_allow_html=True)
            time.sleep(1)
        
        placeholder.empty()
    
    def renderizar_formulario(self):
        """
        Renderiza el formulario de entrada de datos estilo Gemini.
        """
        # Título
        st.markdown("""
            <div style="padding: 2rem 0 1rem 0; text-align: center;">
                <h1 style="font-size: 1.75rem; font-weight: 500; color: var(--text-primary);">
                    📝 Datos de la Empresa
                </h1>
                <p style="color: var(--text-secondary); margin-top: 0.5rem;">
                    Ingresa la información financiera para obtener un análisis personalizado
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Obtener datos actuales si existen
        datos_empresa_actual = None
        if 'datos_empresa' in st.session_state and st.session_state.datos_empresa:
            datos_empresa_actual = st.session_state.datos_empresa.get('datos', {})
        
        with st.form("formulario_empresa", clear_on_submit=False):
            # Sección de información general
            st.markdown("""
                <div class="form-section">
                    <h3 class="form-title">
                        <span class="form-icon">🏢</span>
                        Información General
                    </h3>
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                nombre_empresa = st.text_input(
                    "Nombre de la Empresa",
                    value="" if not datos_empresa_actual else datos_empresa_actual.get('nombre', ""),
                    placeholder="Ej: Mi Empresa S.A.",
                    help="Ingresa el nombre legal de tu empresa"
                )
            
            with col2:
                sector = st.selectbox(
                    "Sector",
                    ["Tecnología", "Comercio", "Manufactura", "Servicios", "Otro"],
                    index=0 if not datos_empresa_actual else 
                          ["Tecnología", "Comercio", "Manufactura", "Servicios", "Otro"].index(
                              datos_empresa_actual.get('sector', "Tecnología")
                          ),
                    help="Selecciona el sector económico principal"
                )
            
            # Sección de información financiera
            st.markdown("""
                <div class="form-section" style="margin-top: 2rem;">
                    <h3 class="form-title">
                        <span class="form-icon">💰</span>
                        Información Financiera
                    </h3>
                </div>
            """, unsafe_allow_html=True)
            
            col1_form, col2_form = st.columns(2)
            
            with col1_form:
                ganancias = st.number_input(
                    "Ganancias Anuales (COP)",
                    min_value=0.0,
                    format="%f",
                    value=0.0 if not datos_empresa_actual else datos_empresa_actual.get('ganancias', 0.0),
                    help="Ingresos totales menos gastos operativos"
                )
                st.markdown('<div class="form-description">Utilidad neta del último año fiscal</div>', unsafe_allow_html=True)
                
                num_empleados = st.number_input(
                    "Número de Empleados",
                    min_value=1,
                    step=1,
                    value=1 if not datos_empresa_actual else datos_empresa_actual.get('empleados', 1),
                    help="Total de empleados en nómina"
                )
                st.markdown('<div class="form-description">Personal activo en la empresa</div>', unsafe_allow_html=True)
                
                valor_cartera = st.number_input(
                    "Valor en Cartera (COP)",
                    min_value=0.0,
                    format="%f",
                    value=0.0 if not datos_empresa_actual else datos_empresa_actual.get('cartera', 0.0),
                    help="Total de cuentas por cobrar"
                )
                st.markdown('<div class="form-description">Dinero pendiente de cobro a clientes</div>', unsafe_allow_html=True)
            
            with col2_form:
                valor_activos = st.number_input(
                    "Valor en Activos (COP)",
                    min_value=0.0,
                    format="%f",
                    value=0.0 if not datos_empresa_actual else datos_empresa_actual.get('activos', 0.0),
                    help="Total de bienes y derechos"
                )
                st.markdown('<div class="form-description">Suma de todos los activos de la empresa</div>', unsafe_allow_html=True)
                
                valor_deudas = st.number_input(
                    "Valor Deudas (COP)",
                    min_value=0.0,
                    format="%f",
                    value=0.0 if not datos_empresa_actual else datos_empresa_actual.get('deudas', 0.0),
                    help="Total de obligaciones financieras"
                )
                st.markdown('<div class="form-description">Pasivos totales de la empresa</div>', unsafe_allow_html=True)
            
            # Sección de acciones
            st.markdown('<div style="margin-top: 2rem; display: flex; gap: 1rem;">', unsafe_allow_html=True)
            
            col1_btn, col2_btn = st.columns(2)
            
            with col1_btn:
                submitted = st.form_submit_button("🚀 Analizar Empresa", use_container_width=True)
            
            with col2_btn:
                if 'datos_empresa' in st.session_state and st.session_state.datos_empresa:
                    cancel = st.form_submit_button("❌ Cancelar", use_container_width=True)
                    if cancel:
                        st.session_state.page_view = "chat"
                        return None
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            if submitted:
                # Validar entradas
                errores = []
                
                if not nombre_empresa.strip():
                    errores.append("El nombre de la empresa es obligatorio.")
                
                valid_ganancias, msg = self.validators.validar_numeros(ganancias, 0.0, "valor de ganancias")
                if not valid_ganancias:
                    errores.append(msg)
                
                valid_activos, msg = self.validators.validar_numeros(valor_activos, 0.0, "valor de activos")
                if not valid_activos:
                    errores.append(msg)
                    
                valid_empleados, msg = self.validators.validar_numeros(num_empleados, 1, "número de empleados")
                if not valid_empleados:
                    errores.append(msg)
                    
                valid_cartera, msg = self.validators.validar_numeros(valor_cartera, 0.0, "valor en cartera")
                if not valid_cartera:
                    errores.append(msg)
                    
                valid_deudas, msg = self.validators.validar_numeros(valor_deudas, 0.0, "valor en deudas")
                if not valid_deudas:
                    errores.append(msg)
                
                # Si hay errores, mostrarlos
                if errores:
                    error_text = "\n".join([f"• {error}" for error in errores])
                    st.error(f"Por favor, corrige los siguientes errores:\n\n{error_text}")
                    return None
                else:
                    # Crear objeto Empresa
                    empresa = Empresa(
                        nombre=nombre_empresa,
                        sector=sector,
                        ganancias=ganancias,
                        empleados=num_empleados,
                        activos=valor_activos,
                        cartera=valor_cartera,
                        deudas=valor_deudas
                    )
                    
                    # Mostrar animación de procesamiento
                    self.mostrar_procesamiento()
                    
                    # Realizar análisis
                    resultados = self.analizador_financiero.analizar_empresa(empresa)
                    mensaje = resultados.generar_mensaje()
                    
                    # Preparar datos procesados
                    datos_procesados = {
                        'datos': empresa.data_dict,
                        'resultados': resultados.data_dict,
                        'mensaje': mensaje
                    }
                    
                    # Agregar mensaje de bienvenida al chat si es el primer análisis
                    if 'chat_history' not in st.session_state or not st.session_state.chat_history:
                        bienvenida = f"¡Hola! He analizado los datos de **{nombre_empresa}**. El estado financiero general de tu empresa es **{resultados.estado_general}**.\n\n¿Qué te gustaría saber específicamente sobre tus indicadores financieros?"
                        if 'chat_history' not in st.session_state:
                            st.session_state.chat_history = []
                        st.session_state.chat_history.append(("bot", bienvenida))
                    
                    return datos_procesados
        
        return None