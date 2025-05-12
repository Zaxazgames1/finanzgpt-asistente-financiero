class StylesUI:
    """
    Clase con estilos CSS ultra modernos tipo ChatGPT.
    """
    @staticmethod
    def get_css():
        """
        Retorna estilos CSS premium tipo ChatGPT.
        """
        return """
        <style>
            /* Variables de color */
            :root {
                --primary-color: #10a37f;
                --primary-dark: #0d8a6a;
                --primary-light: #1aba8f;
                --bg-dark: #171717;
                --bg-medium: #212121;
                --bg-light: #2a2a2a;
                --text-primary: #ececec;
                --text-secondary: #a8a8a8;
                --border-color: #444444;
                --error-color: #ef4444;
                --success-color: #10a37f;
                --warning-color: #f59e0b;
                --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
                --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
            }
            
            /* Reset y base */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            /* Tema oscuro global */
            body, .stApp {
                background-color: var(--bg-dark) !important;
                font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif;
                color: var(--text-primary);
            }
            
            /* Ocultar elementos de Streamlit */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Container principal tipo ChatGPT */
            .main {
                background-color: var(--bg-dark);
                padding: 0;
                max-width: 100%;
            }
            
            /* Sidebar estilo moderno */
            .sidebar .sidebar-content {
                background-color: var(--bg-medium);
                padding: 1.5rem;
                height: 100vh;
                border-right: 1px solid var(--border-color);
            }
            
            /* Título principal estilo ChatGPT */
            .main-title {
                font-size: 2.5rem;
                font-weight: 700;
                background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-align: center;
                margin: 2rem 0;
                letter-spacing: -0.02em;
                animation: glow 3s ease-in-out infinite;
            }
            
            @keyframes glow {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.8; }
            }
            
            /* Subtítulos */
            .sub-title {
                font-size: 1.2rem;
                color: var(--text-secondary);
                text-align: center;
                margin-bottom: 2rem;
                font-weight: 400;
            }
            
            /* Container del chat estilo ChatGPT */
            .chat-container {
                max-width: 800px;
                margin: 0 auto;
                height: calc(100vh - 180px);
                overflow-y: auto;
                padding: 2rem;
                scrollbar-width: thin;
                scrollbar-color: var(--border-color) transparent;
            }
            
            .chat-container::-webkit-scrollbar {
                width: 8px;
            }
            
            .chat-container::-webkit-scrollbar-track {
                background: transparent;
            }
            
            .chat-container::-webkit-scrollbar-thumb {
                background: var(--border-color);
                border-radius: 4px;
            }
            
            /* Mensajes de chat estilo ChatGPT */
            .chat-message-user, .chat-message-bot {
                display: flex;
                gap: 1rem;
                margin-bottom: 1.5rem;
                padding: 1rem;
                border-radius: 12px;
                animation: fadeIn 0.3s ease-in;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .chat-message-user {
                background-color: var(--bg-light);
                margin-left: 4rem;
                border: 1px solid var(--border-color);
                box-shadow: var(--shadow);
            }
            
            .chat-message-bot {
                background-color: var(--bg-medium);
                margin-right: 4rem;
                border: 1px solid var(--primary-dark);
                box-shadow: var(--shadow);
            }
            
            /* Avatares estilo moderno */
            .avatar {
                width: 40px;
                height: 40px;
                border-radius: 8px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: 600;
                flex-shrink: 0;
                box-shadow: var(--shadow);
            }
            
            .avatar-user {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
            }
            
            .avatar-bot {
                background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
                color: white;
            }
            
            /* Contenido del mensaje */
            .message-content {
                flex: 1;
                color: var(--text-primary);
                line-height: 1.6;
                font-size: 1rem;
            }
            
            .message-content p {
                margin-bottom: 0.5rem;
            }
            
            .message-content ul, .message-content ol {
                margin-left: 1.5rem;
                margin-bottom: 0.5rem;
            }
            
            .message-content strong {
                color: var(--primary-light);
                font-weight: 600;
            }
            
            .message-content h3 {
                color: var(--primary-color);
                margin: 1rem 0 0.5rem 0;
                font-size: 1.3rem;
                font-weight: 600;
            }
            
            /* Input del chat estilo ChatGPT */
            .stChatInput {
                position: fixed !important;
                bottom: 0;
                left: 0;
                right: 0;
                background: var(--bg-dark);
                padding: 1rem;
                border-top: 1px solid var(--border-color);
                z-index: 1000;
            }
            
            .stChatInput > div {
                max-width: 800px;
                margin: 0 auto;
            }
            
            .stChatInput textarea {
                background: var(--bg-medium) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 12px !important;
                color: var(--text-primary) !important;
                font-size: 1rem !important;
                padding: 1rem 1.5rem !important;
                resize: none !important;
                transition: all 0.3s ease !important;
            }
            
            .stChatInput textarea:focus {
                border-color: var(--primary-color) !important;
                box-shadow: 0 0 0 3px rgba(16, 163, 127, 0.2) !important;
                outline: none !important;
            }
            
            .stChatInput textarea::placeholder {
                color: var(--text-secondary) !important;
            }
            
            /* Botones estilo ChatGPT */
            .stButton > button {
                background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0.75rem 1.5rem;
                font-size: 1rem;
                font-weight: 500;
                cursor: pointer;
                transition: all 0.3s ease;
                box-shadow: var(--shadow);
            }
            
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: var(--shadow-lg);
                background: linear-gradient(135deg, var(--primary-dark), var(--primary-color));
            }
            
            .stButton > button:active {
                transform: translateY(0);
            }
            
            /* Cards modernas */
            .card {
                background: var(--bg-medium);
                border-radius: 16px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                border: 1px solid var(--border-color);
                box-shadow: var(--shadow);
                transition: all 0.3s ease;
            }
            
            .card:hover {
                border-color: var(--primary-color);
                transform: translateY(-2px);
                box-shadow: var(--shadow-lg);
            }
            
            /* Animación de pensamiento tipo ChatGPT */
            .thinking-animation {
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 2rem;
                gap: 0.5rem;
            }
            
            .thinking-dot {
                width: 12px;
                height: 12px;
                background: var(--primary-color);
                border-radius: 50%;
                animation: pulse 1.5s ease-in-out infinite;
                box-shadow: 0 0 10px rgba(16, 163, 127, 0.5);
            }
            
            .thinking-dot:nth-child(2) {
                animation-delay: 0.2s;
            }
            
            .thinking-dot:nth-child(3) {
                animation-delay: 0.4s;
            }
            
            @keyframes pulse {
                0%, 100% {
                    transform: scale(0.8);
                    opacity: 0.5;
                }
                50% {
                    transform: scale(1.2);
                    opacity: 1;
                }
            }
            
            /* Estados financieros con gradientes */
            .estado-excelente {
                background: linear-gradient(135deg, #10a37f, #1aba8f);
                color: white;
                padding: 1rem;
                border-radius: 12px;
                text-align: center;
                font-weight: 600;
                box-shadow: 0 4px 15px rgba(16, 163, 127, 0.3);
            }
            
            .estado-bueno {
                background: linear-gradient(135deg, #3b82f6, #60a5fa);
                color: white;
                padding: 1rem;
                border-radius: 12px;
                text-align: center;
                font-weight: 600;
                box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
            }
            
            .estado-regular {
                background: linear-gradient(135deg, #f59e0b, #fbbf24);
                color: white;
                padding: 1rem;
                border-radius: 12px;
                text-align: center;
                font-weight: 600;
                box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
            }
            
            .estado-critico {
                background: linear-gradient(135deg, #ef4444, #f87171);
                color: white;
                padding: 1rem;
                border-radius: 12px;
                text-align: center;
                font-weight: 600;
                box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
            }
            
            /* Métricas destacadas */
            .highlight-metric {
                background: linear-gradient(135deg, var(--bg-light), var(--bg-medium));
                border: 1px solid var(--primary-color);
                border-radius: 12px;
                padding: 1.25rem;
                margin: 1rem 0;
                position: relative;
                overflow: hidden;
                transition: all 0.3s ease;
            }
            
            .highlight-metric::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 4px;
                height: 100%;
                background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
            }
            
            .highlight-metric:hover {
                transform: translateX(5px);
                box-shadow: var(--shadow-lg);
            }
            
            /* Formularios modernos */
            .stTextInput > div > div > input,
            .stNumberInput > div > div > input,
            .stSelectbox > div > div > div {
                background: var(--bg-medium) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 8px !important;
                color: var(--text-primary) !important;
                padding: 0.75rem 1rem !important;
                transition: all 0.3s ease !important;
            }
            
            .stTextInput > div > div > input:focus,
            .stNumberInput > div > div > input:focus,
            .stSelectbox > div > div > div:focus {
                border-color: var(--primary-color) !important;
                box-shadow: 0 0 0 3px rgba(16, 163, 127, 0.2) !important;
                outline: none !important;
            }
            
            /* Labels de formularios */
            .stTextInput > label,
            .stNumberInput > label,
            .stSelectbox > label {
                color: var(--text-primary) !important;
                font-weight: 500 !important;
                margin-bottom: 0.5rem !important;
            }
            
            /* Expander personalizado */
            .streamlit-expanderHeader {
                background: var(--bg-medium) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 8px !important;
                color: var(--text-primary) !important;
                font-weight: 500 !important;
                transition: all 0.3s ease !important;
            }
            
            .streamlit-expanderHeader:hover {
                border-color: var(--primary-color) !important;
                box-shadow: var(--shadow) !important;
            }
            
            /* Tabs personalizados */
            .stTabs [data-baseweb="tab-list"] {
                background-color: var(--bg-medium);
                border-radius: 12px;
                padding: 0.5rem;
                gap: 0.5rem;
            }
            
            .stTabs [data-baseweb="tab"] {
                background-color: transparent;
                color: var(--text-secondary);
                border-radius: 8px;
                padding: 0.75rem 1.5rem;
                font-weight: 500;
                transition: all 0.3s ease;
            }
            
            .stTabs [aria-selected="true"] {
                background-color: var(--primary-color) !important;
                color: white !important;
                box-shadow: var(--shadow);
            }
            
            /* Scrollbar personalizado */
            ::-webkit-scrollbar {
                width: 10px;
                height: 10px;
            }
            
            ::-webkit-scrollbar-track {
                background: var(--bg-dark);
                border-radius: 5px;
            }
            
            ::-webkit-scrollbar-thumb {
                background: var(--border-color);
                border-radius: 5px;
                transition: background 0.3s ease;
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background: var(--primary-color);
            }
            
            /* Responsive design */
            @media (max-width: 768px) {
                .chat-message-user,
                .chat-message-bot {
                    margin-left: 0;
                    margin-right: 0;
                }
                
                .main-title {
                    font-size: 2rem;
                }
                
                .chat-container {
                    padding: 1rem;
                }
            }
            
            /* Animaciones de carga */
            .loading-spinner {
                display: inline-block;
                width: 20px;
                height: 20px;
                border: 3px solid var(--border-color);
                border-radius: 50%;
                border-top-color: var(--primary-color);
                animation: spin 1s ease-in-out infinite;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            
            /* Efectos de hover para links */
            a {
                color: var(--primary-color);
                text-decoration: none;
                transition: all 0.3s ease;
            }
            
            a:hover {
                color: var(--primary-light);
                text-decoration: underline;
            }
            
            /* Tooltips personalizados */
            .tooltip {
                position: relative;
                display: inline-block;
            }
            
            .tooltip .tooltiptext {
                visibility: hidden;
                background-color: var(--bg-dark);
                color: var(--text-primary);
                text-align: center;
                border-radius: 6px;
                padding: 5px 10px;
                position: absolute;
                z-index: 1;
                bottom: 125%;
                left: 50%;
                transform: translateX(-50%);
                opacity: 0;
                transition: opacity 0.3s;
                box-shadow: var(--shadow-lg);
                border: 1px solid var(--border-color);
            }
            
            .tooltip:hover .tooltiptext {
                visibility: visible;
                opacity: 1;
            }
            
            /* Badges y etiquetas */
            .badge {
                display: inline-block;
                padding: 0.25rem 0.75rem;
                border-radius: 9999px;
                font-size: 0.875rem;
                font-weight: 500;
                line-height: 1;
                text-align: center;
                white-space: nowrap;
                vertical-align: baseline;
            }
            
            .badge-success {
                background-color: var(--success-color);
                color: white;
            }
            
            .badge-warning {
                background-color: var(--warning-color);
                color: white;
            }
            
            .badge-error {
                background-color: var(--error-color);
                color: white;
            }
            
            /* Efectos de glassmorphism */
            .glass {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
        </style>
        """