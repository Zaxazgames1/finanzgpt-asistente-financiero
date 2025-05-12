import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils.formatters import Formatters

class ResultsUI:
    """
    Clase para manejar la interfaz de resultados del análisis estilo Gemini.
    """
    def __init__(self, formatters):
        """
        Inicializa la interfaz de resultados.
        """
        self.formatters = formatters
    
    def renderizar_resultados(self, datos_empresa):
        """
        Renderiza la vista de resultados del análisis estilo Gemini.
        """
        if not datos_empresa:
            st.warning("No hay datos de empresa para mostrar. Por favor, completa el formulario primero.")
            st.session_state.page_view = "form"
            return
        
        resultados = datos_empresa['resultados']
        
        # Header de resultados
        st.markdown(f"""
            <div style="padding: 2rem 0 1rem 0; text-align: center;">
                <h1 style="font-size: 1.75rem; font-weight: 500; color: var(--text-primary);">
                    📊 Análisis Financiero
                </h1>
                <p style="color: var(--text-secondary); margin-top: 0.5rem;">
                    {resultados['nombre']} • Sector {resultados['sector']}
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Estado general con estilo Gemini
        estado = resultados['estado_general'].lower()
        st.markdown(f"""
        <div class="card">
            <div class="estado-{estado}">
                <h2 style="font-size: 1.25rem; font-weight: 500;">Estado Financiero: {resultados['estado_general']}</h2>
            </div>
            <div style="text-align: center; margin-top: 1rem; font-size: 0.9rem; color: var(--text-secondary);">
                <p>El análisis se basa en la comparación de tus indicadores con estándares del sector {resultados['sector']}.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Contenedor para los indicadores principales
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📈 Indicadores Clave")
        
        # Crear 2 columnas para mostrar los indicadores principales
        col1_ind, col2_ind = st.columns(2)
        
        with col1_ind:
            ratio = resultados['indicadores']['ratio_endeudamiento']
            eval_ind = resultados['evaluacion']['endeudamiento']
            
            st.markdown(f"""
            <div class="highlight-metric">
                <strong>⚖️ Endeudamiento</strong><br>
                <span style="font-size: 1.25rem; color: {('#00D084' if eval_ind == 'bueno' else '#F85640')}">{ratio:.2f}</span><br>
                <span style="font-size: 0.875rem; color: var(--text-secondary);">Evaluación: {eval_ind.capitalize()}</span>
            </div>
            """, unsafe_allow_html=True)
            
            rent = resultados['indicadores']['rentabilidad']
            eval_ind = resultados['evaluacion']['rentabilidad']
            
            st.markdown(f"""
            <div class="highlight-metric">
                <strong>💰 Rentabilidad</strong><br>
                <span style="font-size: 1.25rem; color: {('#00D084' if eval_ind == 'buena' else '#F85640')}">{rent:.2%}</span><br>
                <span style="font-size: 0.875rem; color: var(--text-secondary);">Evaluación: {eval_ind.capitalize()}</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col2_ind:
            prod = resultados['indicadores']['productividad']
            eval_ind = resultados['evaluacion']['productividad']
            
            st.markdown(f"""
            <div class="highlight-metric">
                <strong>👥 Productividad</strong><br>
                <span style="font-size: 1.25rem; color: {('#00D084' if eval_ind == 'buena' else '#F85640')}">${self.formatters.formato_numero(prod)}</span><br>
                <span style="font-size: 0.875rem; color: var(--text-secondary);">Evaluación: {eval_ind.capitalize()}</span>
            </div>
            """, unsafe_allow_html=True)
            
            rot = resultados['indicadores']['rotacion_cartera']
            eval_ind = resultados['evaluacion']['rotacion']
            
            st.markdown(f"""
            <div class="highlight-metric">
                <strong>📅 Rotación Cartera</strong><br>
                <span style="font-size: 1.25rem; color: {('#00D084' if eval_ind == 'buena' else '#F85640')}">{rot:.1f} días</span><br>
                <span style="font-size: 0.875rem; color: var(--text-secondary);">Evaluación: {eval_ind.capitalize()}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Recomendaciones
        if resultados['recomendaciones']:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 💡 Recomendaciones")
            
            for i, rec in enumerate(resultados['recomendaciones'], 1):
                st.markdown(f"""
                <div class="recomendacion">
                    <strong>Recomendación {i}:</strong> {rec}
                </div>
                """, unsafe_allow_html=True)
                
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Gráfico de indicadores estilo Gemini
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📊 Visualización de Indicadores")
        
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
        
        # Mostramos el gráfico
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Análisis NLP estilo Gemini
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🧠 Análisis de Procesamiento de Lenguaje Natural")
        
        with st.expander("Ver detalles del análisis NLP"):
            tab1, tab2, tab3, tab4 = st.tabs(["Tokenización", "Lematización", "POS Tagging", "Embedding"])
            
            with tab1:
                st.markdown("#### 🔍 Tokenización")
                st.markdown("La tokenización divide el texto en unidades individuales (tokens):")
                st.code(str(resultados['nlp_ejemplo']['tokens']))
                st.markdown("""
                <div class="info-section">
                    <div class="info-icon">💡</div>
                    <div class="info-text">
                        <strong>¿Para qué sirve?</strong> Permite analizar el texto palabra por palabra, lo que es fundamental para el procesamiento del lenguaje natural.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with tab2:
                st.markdown("#### 📝 Lematización")
                st.markdown("La lematización reduce las palabras a su forma base o lema:")
                st.code(str(resultados['nlp_ejemplo']['lemas']))
                st.markdown("""
                <div class="info-section">
                    <div class="info-icon">💡</div>
                    <div class="info-text">
                        <strong>¿Para qué sirve?</strong> Permite considerar diferentes formas de una palabra como la misma, mejorando el análisis semántico del texto.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with tab3:
                st.markdown("#### 🏷️ POS Tagging")
                st.markdown("El etiquetado gramatical (Part-of-Speech) identifica la función gramatical de cada palabra:")
                st.code(str(resultados['nlp_ejemplo']['pos_tags']))
                st.markdown("""
                <div class="info-section">
                    <div class="info-icon">💡</div>
                    <div class="info-text">
                        <strong>¿Para qué sirve?</strong> Ayuda a entender la estructura gramatical del texto, identificando verbos, sustantivos, adjetivos, etc.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with tab4:
                st.markdown("#### 🧮 Embedding")
                st.markdown("El embedding transforma el texto en vectores numéricos que capturan significado semántico:")
                st.code(f"Dimensión del embedding: {resultados['nlp_ejemplo']['embedding_dim']}")
                st.markdown("""
                <div class="info-section">
                    <div class="info-icon">💡</div>
                    <div class="info-text">
                        <strong>¿Para qué sirve?</strong> Permite representar palabras y frases como vectores, facilitando cálculos de similitud semántica y otros análisis avanzados.
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Botones de acción estilo Gemini
        st.markdown("""
            <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💬 Consultar al Chatbot", use_container_width=True):
                st.session_state.page_view = "chat"
                st.rerun()
        
        with col2:
            if st.button("📝 Modificar datos", use_container_width=True):
                st.session_state.page_view = "form"
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Footer con acciones adicionales estilo Gemini
        st.markdown("""
            <div style="margin-top: 3rem; text-align: center;">
                <div style="display: inline-flex; gap: 1rem;">
                    <button class="deep-research-button">
                        🔍 Deep Research
                    </button>
                    <button class="canvas-button">
                        📊 Canvas
                    </button>
                    <button class="action-button">
                        📤 Exportar reporte
                    </button>
                </div>
            </div>
        """, unsafe_allow_html=True)