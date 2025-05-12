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
            
            /* Select boxes */
            .stSelectbox > div > div {
                background-color: var(--bg-input) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-md) !important;
                color: var(--text-primary) !important;
                min-height: 38px !important;
            }
            
            .stSelectbox > div > div > div {
                color: var(--text-primary) !important;
            }
            
            .stSelectbox > div > div:hover {
                border-color: var(--text-muted) !important;
            }
            
            .stSelectbox > div > div:focus-within {
                border-color: var(--accent-blue) !important;
                box-shadow: 0 0 0 1px var(--accent-blue) !important;
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
            
            /* Chat input estilo Gemini */
            .stChatInput {
                background-color: var(--bg-primary) !important;
                border-top: 1px solid var(--border-color);
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                z-index: 1000;
                padding: 1rem 0;
            }
            
            .stChatInput > div {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 2rem;
            }
            
            .stChatInput > div > div > div > div {
                background-color: var(--bg-input) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-lg) !important;
                box-shadow: var(--shadow-sm);
            }
            
            .stChatInput textarea {
                background-color: transparent !important;
                border: none !important;
                color: var(--text-primary) !important;
                padding: 0.875rem 1.25rem !important;
                font-size: 0.95rem !important;
                font-family: inherit !important;
                line-height: 1.5 !important;
                resize: none !important;
            }
            
            .stChatInput textarea:focus {
                outline: none !important;
                box-shadow: none !important;
            }
            
            .stChatInput textarea::placeholder {
                color: var(--text-muted) !important;
            }
            
            /* Chat messages container */
            .chat-container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
                min-height: calc(100vh - 200px);
                display: flex;
                flex-direction: column;
            }
            
            /* Chat messages */
            .chat-message-user,
            .chat-message-bot {
                display: flex;
                gap: 1rem;
                margin-bottom: 2rem;
                padding: 0 2rem;
                max-width: 1200px;
                width: 100%;
                margin-left: auto;
                margin-right: auto;
            }
            
            .chat-message-user {
                flex-direction: row-reverse;
            }
            
            .message-content {
                max-width: 70%;
                padding: 0.875rem 1.25rem;
                border-radius: var(--radius-lg);
                line-height: 1.6;
                font-size: 0.95rem;
                word-wrap: break-word;
            }
            
            .chat-message-user .message-content {
                background-color: var(--bg-tertiary);
                color: var(--text-primary);
                border: 1px solid var(--border-color);
            }
            
            .chat-message-bot .message-content {
                background-color: transparent;
                color: var(--text-primary);
                padding-left: 0;
                padding-right: 0;
            }
            
            /* Avatars */
            .avatar {
                width: 32px;
                height: 32px;
                border-radius: var(--radius-full);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 0.875rem;
                flex-shrink: 0;
            }
            
            .avatar-user {
                background-color: var(--bg-tertiary);
                color: var(--text-primary);
                border: 1px solid var(--border-color);
            }
            
            .avatar-bot {
                background: linear-gradient(135deg, #FA8B00, #8B00FA);
                color: white;
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
            
            /* Main title */
            .main-title {
                font-size: 1.5rem;
                font-weight: 500;
                color: var(--text-primary);
                text-align: center;
                margin: 2rem 0 1rem 0;
                letter-spacing: -0.01em;
            }
            
            .sub-title {
                font-size: 1rem;
                color: var(--text-secondary);
                text-align: center;
                margin-bottom: 2rem;
            }
            
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
            
            /* Alerts */
            .stAlert {
                border-radius: var(--radius-md) !important;
                border: 1px solid !important;
                font-size: 0.9rem !important;
                padding: 0.875rem 1rem !important;
            }
            
            .stAlert[data-baseweb="notification"] {
                background-color: rgba(0, 161, 241, 0.1) !important;
                border-color: var(--accent-blue) !important;
                color: var(--text-primary) !important;
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
            
            /* Canvas button estilo Gemini */
            .canvas-button {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                padding: 0.625rem 1rem;
                background-color: var(--bg-tertiary);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-md);
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
            
            /* Form submit button */
            .stFormSubmitButton > button {
                background-color: var(--accent-blue) !important;
                color: white !important;
                border: none !important;
                padding: 0.625rem 1.5rem !important;
                border-radius: var(--radius-md) !important;
                font-size: 0.95rem !important;
                font-weight: 500 !important;
                cursor: pointer !important;
                transition: var(--transition) !important;
            }
            
            .stFormSubmitButton > button:hover {
                background-color: var(--primary-hover) !important;
                transform: translateY(-1px);
                box-shadow: var(--shadow-sm);
            }
            
            /* Welcome screen estilo Gemini */
            .welcome-container {
                max-width: 800px;
                margin: 0 auto;
                padding: 3rem 2rem;
                text-align: center;
            }
            
            .welcome-icon {
                font-size: 3rem;
                margin-bottom: 1.5rem;
                display: inline-block;
                background: linear-gradient(135deg, #FA8B00, #8B00FA);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .welcome-title {
                font-size: 2rem;
                font-weight: 500;
                color: var(--text-primary);
                margin-bottom: 0.5rem;
            }
            
            .welcome-subtitle {
                font-size: 1.125rem;
                color: var(--text-secondary);
                max-width: 500px;
                margin: 0 auto 2rem auto;
                line-height: 1.6;
            }
            
            /* Deep Research button */
            .deep-research-button {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                padding: 0.625rem 1rem;
                background-color: transparent;
                border: 1px solid var(--border-color);
                border-radius: var(--radius-full);
                color: var(--text-secondary);
                font-size: 0.875rem;
                cursor: pointer;
                transition: var(--transition);
                margin-bottom: 1rem;
            }
            
            .deep-research-button:hover {
                background-color: var(--bg-tertiary);
                color: var(--text-primary);
                border-color: var(--text-muted);
            }
            
            /* Info section */
            .info-section {
                background-color: var(--bg-tertiary);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-lg);
                padding: 1rem 1.5rem;
                margin: 1rem 0;
                display: flex;
                align-items: flex-start;
                gap: 1rem;
            }
            
            .info-icon {
                color: var(--accent-blue);
                font-size: 1.25rem;
                flex-shrink: 0;
            }
            
            .info-text {
                color: var(--text-secondary);
                font-size: 0.9rem;
                line-height: 1.5;
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
            
            /* Recomendaciones */
            .recomendacion {
                background-color: var(--bg-tertiary);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-md);
                padding: 1rem 1.25rem;
                margin-bottom: 0.75rem;
                color: var(--text-primary);
                transition: var(--transition);
            }
            
            .recomendacion:hover {
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
            
            .form-title {
                font-size: 1.125rem;
                font-weight: 500;
                color: var(--text-primary);
                margin-bottom: 1.25rem;
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            
            .form-icon {
                color: var(--accent-blue);
                font-size: 1.25rem;
            }
            
            .form-description {
                font-size: 0.8125rem;
                color: var(--text-muted);
                margin-top: 0.25rem;
            }
            
            /* Responsive */
            @media (max-width: 768px) {
                .chat-container {
                    padding: 1rem;
                }
                
                .message-content {
                    max-width: 85%;
                }
                
                .chat-message-user,
                .chat-message-bot {
                    padding: 0 1rem;
                }
            }
        </style>
        """