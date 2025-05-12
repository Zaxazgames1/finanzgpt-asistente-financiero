import streamlit as st
import time
from models.empresa import Empresa

class FormUI:
    """
    Clase para manejar la interfaz del formulario de datos con diseño ultra moderno.
    """
    def __init__(self, analizador_financiero, validators):
        """
        Inicializa la interfaz del formulario.
        
        Args:
            analizador_financiero (AnalizadorFinanciero): Servicio de análisis financiero
            validators (Validators): Utilitarios de validación
        """
        self.analizador_financiero = analizador_financiero
        self.validators = validators
    
    def mostrar_procesamiento(self):
        """Muestra una animación de procesamiento estilo ChatGPT"""
        # Crear contenedor para la animación
        placeholder = st.empty()
        
        with placeholder.container():
            st.markdown("""
                <div class="processing-container">
                    <div class="processing-icon">🤖</div>
                    <div class="processing-text">Analizando datos financieros...</div>
                    <div class="processing-animation">
                        <div class="processing-dot"></div>
                        <div class="processing-dot"></div>
                        <div class="processing-dot"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # CSS para la animación
            st.markdown("""
                <style>
                    .processing-container {
                        text-align: center;
                        padding: 3rem;
                        max-width: 400px;
                        margin: 2rem auto;
                    }
                    
                    .processing-icon {
                        font-size: 3rem;
                        margin-bottom: 1rem;
                        animation: pulse 2s ease-in-out infinite;
                    }
                    
                    .processing-text {
                        font-size: 1.25rem;
                        color: var(--text-primary);
                        margin-bottom: 1.5rem;
                        font-weight: 500;
                    }
                    
                    .processing-animation {
                        display: flex;
                        justify-content: center;
                        gap: 0.5rem;
                    }
                    
                    .processing-dot {
                        width: 12px;
                        height: 12px;
                        background-color: var(--primary-color);
                        border-radius: 50%;
                        animation: bounce 1.4s ease-in-out infinite;
                    }
                    
                    .processing-dot:nth-child(1) {
                        animation-delay: 0s;
                    }
                    
                    .processing-dot:nth-child(2) {
                        animation-delay: 0.2s;
                    }
                    
                    .processing-dot:nth-child(3) {
                        animation-delay: 0.4s;
                    }
                    
                    @keyframes pulse {
                        0%, 100% { transform: scale(1); opacity: 1; }
                        50% { transform: scale(1.1); opacity: 0.8; }
                    }
                    
                    @keyframes bounce {
                        0%, 60%, 100% {
                            transform: translateY(0);
                            opacity: 0.5;
                        }
                        30% {
                            transform: translateY(-20px);
                            opacity: 1;
                        }
                    }
                    
                    .success-container {
                        text-align: center;
                        padding: 3rem;
                        max-width: 400px;
                        margin: 2rem auto;
                    }
                    
                    .success-icon {
                        font-size: 3rem;
                        color: var(--green);
                        margin-bottom: 1rem;
                        animation: checkmark 0.6s ease-in-out;
                    }
                    
                    .success-text {
                        font-size: 1.25rem;
                        color: var(--text-primary);
                        font-weight: 500;
                    }
                    
                    @keyframes checkmark {
                        0% { transform: scale(0) rotate(0deg); }
                        50% { transform: scale(1.2) rotate(360deg); }
                        100% { transform: scale(1) rotate(360deg); }
                    }
                </style>
            """, unsafe_allow_html=True)
            
            # Simulación de procesamiento
            time.sleep(2)
        
        # Limpiar y mostrar éxito
        placeholder.empty()
        with placeholder.container():
            st.markdown("""
                <div class="success-container">
                    <div class="success-icon">✅</div>
                    <div class="success-text">Análisis completado exitosamente</div>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
        
        # Limpiar completamente
        placeholder.empty()
    
    def renderizar_formulario(self):
        """
        Renderiza el formulario de entrada de datos con diseño ultra moderno.
        
        Returns:
            dict: Datos de empresa procesados, o None si no se envió o hay errores
        """
        # Título principal
        st.markdown('<h1 class="main-title">📝 Datos de la Empresa</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-title">Ingresa la información financiera para obtener un análisis personalizado</p>', unsafe_allow_html=True)
        
        # Obtener datos actuales si existen
        datos_empresa_actual = None
        if 'datos_empresa' in st.session_state and st.session_state.datos_empresa:
            datos_empresa_actual = st.session_state.datos_empresa.get('datos', {})
        
        # CSS adicional para el formulario
        st.markdown("""
            <style>
                .form-section {
                    background-color: var(--bg-card);
                    border: 1px solid var(--border-color);
                    border-radius: var(--radius-xl);
                    padding: 2rem;
                    margin-bottom: 1.5rem;
                    transition: var(--transition);
                }
                
                .form-section:hover {
                    border-color: var(--primary-color);
                    box-shadow: var(--shadow-md);
                }
                
                .form-title {
                    font-size: 1.25rem;
                    font-weight: 600;
                    color: var(--text-primary);
                    margin-bottom: 1.5rem;
                    display: flex;
                    align-items: center;
                    gap: 0.75rem;
                }
                
                .form-icon {
                    font-size: 1.5rem;
                    color: var(--primary-color);
                }
                
                .form-description {
                    font-size: 0.875rem;
                    color: var(--text-secondary);
                    margin-top: 0.25rem;
                    font-style: italic;
                }
                
                .form-actions {
                    display: flex;
                    gap: 1rem;
                    margin-top: 2rem;
                }
                
                .primary-button {
                    background-color: var(--primary-color);
                    color: white;
                    border: none;
                    padding: 0.875rem 2rem;
                    border-radius: var(--radius-lg);
                    font-size: 1rem;
                    font-weight: 500;
                    cursor: pointer;
                    transition: var(--transition);
                    flex: 1;
                }
                
                .primary-button:hover {
                    background-color: var(--primary-hover);
                    transform: translateY(-2px);
                    box-shadow: var(--shadow-lg);
                }
                
                .secondary-button {
                    background-color: transparent;
                    color: var(--primary-color);
                    border: 2px solid var(--primary-color);
                    padding: 0.875rem 2rem;
                    border-radius: var(--radius-lg);
                    font-size: 1rem;
                    font-weight: 500;
                    cursor: pointer;
                    transition: var(--transition);
                    flex: 1;
                }
                
                .secondary-button:hover {
                    background-color: var(--primary-color);
                    color: white;
                    transform: translateY(-2px);
                    box-shadow: var(--shadow-lg);
                }
                
                .input-group {
                    margin-bottom: 1.5rem;
                }
                
                .input-label {
                    font-size: 0.9375rem;
                    font-weight: 500;
                    color: var(--text-primary);
                    margin-bottom: 0.5rem;
                    display: block;
                }
                
                .input-help {
                    font-size: 0.8125rem;
                    color: var(--text-muted);
                    margin-top: 0.25rem;
                }
            </style>
        """, unsafe_allow_html=True)
        
        with st.form("formulario_empresa", clear_on_submit=False):
            # Sección de información general
            st.markdown("""
                <div class="form-section">
                    <h3 class="form-title">
                        <span class="form-icon">🏢</span>
                        Información General
                    </h3>
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
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Sección de información financiera
            st.markdown("""
                <div class="form-section">
                    <h3 class="form-title">
                        <span class="form-icon">💰</span>
                        Información Financiera
                    </h3>
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
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Sección de acciones
            st.markdown('<div class="form-actions">', unsafe_allow_html=True)
            
            col1_btn, col2_btn = st.columns(2)
            
            with col1_btn:
                submitted = st.form_submit_button("🚀 Analizar Empresa", use_container_width=True)
            
            with col2_btn:
                if 'datos_empresa' in st.session_state and st.session_state.datos_empresa:
                    cancel = st.form_submit_button("❌ Cancelar", use_container_width=True)
                    if cancel:
                        st.session_state.page_view = "welcome"
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