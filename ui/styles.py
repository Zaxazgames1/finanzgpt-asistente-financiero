class StylesUI:
    """
    Clase con estilos CSS inspirados en Gemini.
    """
    @staticmethod
    def get_css():
        """
        Retorna estilos CSS inspirados en Gemini.
        """
        return """
        <style>
            /* Variables de color tipo Gemini */
            :root {
                --bg-primary: #1E1F20;
                --bg-secondary: #131415;
                --bg-tertiary: #2A2B2D;
                --bg-input: #1E1F20;
                --text-primary: #E5E5E5;
                --text-secondary: #B8BCC8;
                --text-muted: #9AA0A6;
                --primary-color: #00A1F1;
                --primary-hover: #0080BF;
                --border-color: #3C3F41;
                --border-subtle: #2A2B2D;
                --accent-blue: #00A1F1;
                --accent-green: #00D084;
                --accent-red: #F85640;
                --accent-yellow: #FFB800;
                --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
                --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.4);
                --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.5);
                --radius-xs: 3px;
                --radius-sm: 6px;
                --radius-md: 8px;
                --radius-lg: 12px;
                --radius-xl: 16px;
                --radius-full: 9999px;
                --transition: all 0.2s ease;
            }
            
            /* Reset global y base */
            * {
                box-sizing: border-box;
            }
            
            .stApp {
                background-color: var(--bg-primary);
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', Arial, sans-serif;
                color: var(--text-primary);
            }
            
            /* Ocultar elementos de Streamlit */
            #MainMenu, footer, header {
                display: none !important;
            }
            
            [data-testid="stToolbar"] {
                display: none !important;
            }
            
            [data-testid="stHeader"] {
                display: none !important;
            }
            
            /* Container principal */
            .main .block-container {
                padding: 0;
                max-width: 100%;
            }
            
            /* Sidebar estilo Gemini */
            section[data-testid="stSidebar"] {
                background-color: var(--bg-secondary);
                border-right: 1px solid var(--border-color);
                min-width: 280px;
                padding: 0;
                transition: var(--transition);
            }
            
            section[data-testid="stSidebar"] > div {
                padding: 1rem 0;
                background-color: var(--bg-secondary);
            }
            
            /* Botones estilo Gemini */
            .stButton > button {
                background-color: transparent;
                border: none;
                color: var(--text-secondary);
                padding: 0.75rem 1.5rem;
                border-radius: 0;
                font-size: 0.9rem;
                font-weight: 400;
                transition: var(--transition);
                width: 100%;
                text-align: left;
                display: flex;
                align-items: center;
                gap: 0.75rem;
                position: relative;
            }
            
            .stButton > button:hover {
                background-color: rgba(255, 255, 255, 0.1);
                color: var(--text-primary);
            }
            
            .stButton > button:active,
            .stButton > button:focus {
                background-color: rgba(255, 255, 255, 0.15);
                outline: none;
            }
            
            /* Botón activo */
            .stButton > button:disabled {
                background-color: transparent !important;
                color: var(--accent-blue) !important;
                cursor: default !important;
                opacity: 1 !important;
                position: relative;
            }
            
            .stButton > button:disabled::before {
                content: '';
                position: absolute;
                left: 0;
                top: 0;
                bottom: 0;
                width: 3px;
                background-color: var(--accent-blue);
            }
            
            /* Ajustes para los botones del chat */
            .stButton > button[kind="primary"] {
                background: linear-gradient(135deg, #FA8B00, #8B00FA) !important;
                color: white !important;
                font-weight: 500 !important;
                padding: 0.875rem 1.5rem !important;
                font-size: 1rem !important;
                border: none !important;
                border-radius: var(--radius-md) !important;
                box-shadow: 0 4px 12px rgba(250, 139, 0, 0.3) !important;
                text-align: center !important;
            }
            
            .stButton > button[kind="primary"]:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 16px rgba(250, 139, 0, 0.4) !important;
            }
            
            /* Estilo para botones secundarios */
            .stButton > button[kind="secondary"] {
                background-color: var(--bg-tertiary) !important;
                border: 1px solid var(--border-color) !important;
                color: var(--text-primary) !important;
                border-radius: var(--radius-md) !important;
                padding: 0.75rem 1.25rem !important;
                font-size: 0.875rem !important;
                text-align: center !important;
            }
            
            .stButton > button[kind="secondary"]:hover {
                background-color: var(--bg-input) !important;
                border-color: var(--accent-blue) !important;
                color: var(--accent-blue) !important;
            }
            
            /* Forms estilo Gemini */
            .stTextInput > div > div > input,
            .stNumberInput > div > div > input,
            .stTextArea > div > div > textarea {
                background-color: var(--bg-input) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-md) !important;
                color: var(--text-primary) !important;
                padding: 0.75rem 1rem !important;
                font-size: 0.95rem !important;
                transition: var(--transition) !important;
            }
            
            .stTextInput > div > div > input:hover,
            .stNumberInput > div > div > input:hover,
            .stTextArea > div > div > textarea:hover {
                border-color: var(--text-muted) !important;
            }
            
            .stTextInput > div > div > input:focus,
            .stNumberInput > div > div > input:focus,
            .stTextArea > div > div > textarea:focus {
                border-color: var(--accent-blue) !important;
                outline: none !important;
                box-shadow: 0 0 0 1px var(--accent-blue) !important;
            }
            
            /* Chat input estilo Gemini - CORREGIDO */
            .stChatInput {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background-color: var(--bg-primary);
                border-top: 1px solid var(--border-color);
                padding: 1rem 0;
                z-index: 1000;
            }
            
            .stChatInput > div {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 2rem;
            }
            
            div[data-testid="stChatInput"] {
                background-color: var(--bg-primary) !important;
                padding: 1rem !important;
            }
            
            div[data-testid="stChatInput"] > div {
                background-color: var(--bg-input) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-lg) !important;
            }
            
            div[data-testid="stChatInput"] textarea {
                background-color: transparent !important;
                border: none !important;
                color: var(--text-primary) !important;
                font-size: 0.95rem !important;
                padding: 0.75rem 1rem !important;
            }
            
            div[data-testid="stChatInput"] textarea::placeholder {
                color: var(--text-muted) !important;
            }
            
            /* Labels */
            .stTextInput > label,
            .stNumberInput > label,
            .stSelectbox > label,
            .stTextArea > label {
                color: var(--text-secondary) !important;
                font-weight: 500 !important;
                font-size: 0.875rem !important;
                margin-bottom: 0.5rem !important;
            }
            
            /* Headers */
            h1, h2, h3, h4, h5, h6 {
                color: var(--text-primary);
                font-weight: 500;
                line-height: 1.4;
            }
            
            h1 { font-size: 1.75rem; margin: 1.5rem 0 1rem 0; }
            h2 { font-size: 1.5rem; margin: 1.25rem 0 0.875rem 0; }
            h3 { font-size: 1.25rem; margin: 1rem 0 0.75rem 0; }
            h4 { font-size: 1.125rem; margin: 0.875rem 0 0.5rem 0; }
            
            /* Cards estilo Gemini */
            .card {
                background-color: var(--bg-input);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-lg);
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                transition: var(--transition);
            }
            
            .card:hover {
                border-color: var(--text-muted);
            }
            
            /* Code blocks */
            .stCodeBlock {
                background-color: var(--bg-tertiary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-md) !important;
                padding: 1rem !important;
            }
            
            code {
                color: var(--accent-blue) !important;
                background-color: var(--bg-tertiary) !important;
                padding: 0.125rem 0.375rem !important;
                border-radius: var(--radius-xs) !important;
                font-size: 0.875rem !important;
                font-family: 'Consolas', 'Monaco', monospace !important;
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 12px;
                height: 12px;
            }
            
            ::-webkit-scrollbar-track {
                background-color: var(--bg-secondary);
            }
            
            ::-webkit-scrollbar-thumb {
                background-color: var(--border-color);
                border-radius: var(--radius-full);
                border: 3px solid var(--bg-secondary);
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background-color: var(--text-muted);
            }
            
            /* Estados de análisis */
            .estado-excelente,
            .estado-bueno,
            .estado-regular,
            .estado-critico {
                background-color: var(--bg-tertiary);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-lg);
                padding: 1.25rem;
                text-align: center;
                font-weight: 500;
                color: var(--text-primary);
                position: relative;
                overflow: hidden;
            }
            
            .estado-excelente::before {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 3px;
                background-color: var(--accent-green);
            }
            
            .estado-bueno::before {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 3px;
                background-color: var(--accent-blue);
            }
            
            .estado-regular::before {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 3px;
                background-color: var(--accent-yellow);
            }
            
            .estado-critico::before {
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                right: 0;
                height: 3px;
                background-color: var(--accent-red);
            }
            
            /* Metrics */
            .highlight-metric {
                background-color: var(--bg-tertiary);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-md);
                padding: 1rem 1.25rem;
                margin-bottom: 1rem;
                transition: var(--transition);
            }
            
            .highlight-metric:hover {
                border-color: var(--text-muted);
            }
            
            /* Form sections */
            .form-section {
                background-color: var(--bg-input);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-lg);
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                transition: var(--transition);
            }
            
            .form-section:hover {
                border-color: var(--text-muted);
            }
            
            /* Canvas button */
            .canvas-button {
                background-color: var(--bg-tertiary);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-md);
                padding: 0.5rem 1rem;
                color: var(--text-secondary);
                font-size: 0.875rem;
                cursor: pointer;
                transition: var(--transition);
            }
            
            .canvas-button:hover {
                background-color: var(--bg-input);
                color: var(--text-primary);
                border-color: var(--text-muted);
            }
            
            /* Ajuste para mensajes del bot */
            div[class*="message-"] pre {
                background-color: var(--bg-tertiary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-md) !important;
                padding: 1rem !important;
                overflow-x: auto !important;
            }
            
            /* Responsive */
            @media (max-width: 768px) {
                .chat-container {
                    padding: 1rem;
                    padding-bottom: 100px;
                }
                
                .capabilities {
                    grid-template-columns: 1fr;
                }
                
                .main-cta {
                    flex-direction: column;
                    text-align: center;
                }
                
                .message-content {
                    max-width: 90%;
                }
            }
        </style>
        """