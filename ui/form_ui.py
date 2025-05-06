import streamlit as st
import time
from models.empresa import Empresa

class FormUI:
    """
    Clase para manejar la interfaz del formulario de datos.
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
    
    def renderizar_formulario(self):
        """
        Renderiza el formulario de entrada de datos.
        
        Returns:
            dict: Datos de empresa procesados, o None si no se envió o hay errores
        """
        st.markdown('<div class="main-title">📝 Datos de la Empresa</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">Ingresa la información financiera para obtener un análisis personalizado</div>', unsafe_allow_html=True)
        
        # Obtener datos actuales si existen
        datos_empresa_actual = None
        if 'datos_empresa' in st.session_state and st.session_state.datos_empresa:
            datos_empresa_actual = st.session_state.datos_empresa.get('datos', {})
        
        with st.form("formulario_empresa"):
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### Información General")
            
            nombre_empresa = st.text_input(
                "Nombre de la Empresa", 
                value="" if not datos_empresa_actual else datos_empresa_actual.get('nombre', "")
            )
            
            sector = st.selectbox(
                "Sector",
                ["Tecnología", "Comercio", "Manufactura", "Servicios", "Otro"],
                index=0 if not datos_empresa_actual else 
                      ["Tecnología", "Comercio", "Manufactura", "Servicios", "Otro"].index(
                          datos_empresa_actual.get('sector', "Tecnología")
                      )
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### Información Financiera")
            # Crear dos columnas para los inputs numéricos
            col1_form, col2_form = st.columns(2)
            
            with col1_form:
                ganancias = st.number_input(
                    "Ganancias Anuales (COP)", 
                    min_value=0.0, 
                    format="%f",
                    value=0.0 if not datos_empresa_actual else datos_empresa_actual.get('ganancias', 0.0)
                )
                st.markdown("""<div style="font-size: 12px; color: #666;">Ingresos totales menos gastos</div>""", unsafe_allow_html=True)
                
                num_empleados = st.number_input(
                    "Número de Empleados", 
                    min_value=1, 
                    step=1,
                    value=1 if not datos_empresa_actual else datos_empresa_actual.get('empleados', 1)
                )
                st.markdown("""<div style="font-size: 12px; color: #666;">Personal en nómina</div>""", unsafe_allow_html=True)
                
                valor_cartera = st.number_input(
                    "Valor en Cartera (COP)", 
                    min_value=0.0, 
                    format="%f",
                    value=0.0 if not datos_empresa_actual else datos_empresa_actual.get('cartera', 0.0)
                )
                st.markdown("""<div style="font-size: 12px; color: #666;">Total de cuentas por cobrar</div>""", unsafe_allow_html=True)
            
            with col2_form:
                valor_activos = st.number_input(
                    "Valor en Activos (COP)", 
                    min_value=0.0, 
                    format="%f",
                    value=0.0 if not datos_empresa_actual else datos_empresa_actual.get('activos', 0.0)
                )
                st.markdown("""<div style="font-size: 12px; color: #666;">Total de bienes y derechos</div>""", unsafe_allow_html=True)
                
                valor_deudas = st.number_input(
                    "Valor Deudas (COP)", 
                    min_value=0.0, 
                    format="%f",
                    value=0.0 if not datos_empresa_actual else datos_empresa_actual.get('deudas', 0.0)
                )
                st.markdown("""<div style="font-size: 12px; color: #666;">Total de obligaciones financieras</div>""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                submitted = st.form_submit_button("Analizar Empresa", use_container_width=True)
            with col2:
                if 'datos_empresa' in st.session_state and st.session_state.datos_empresa:
                    cancel = st.form_submit_button("Cancelar", use_container_width=True)
                    if cancel:
                        st.session_state.page_view = "welcome"
                        return None
            
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