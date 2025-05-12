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
                --primary-hover: #0d8a6a;
                --primary-light: #2dd4bf;
                --bg-primary: #09090b;
                --bg-secondary: #171717;
                --bg-tertiary: #262626;
                --bg-card: #1a1a1a;
                --text-primary: #f4f4f5;
                --text-secondary: #a1a1aa;
                --text-muted: #71717a;
                --border-color: #27272a;
                --border-focus: #10a37f;
                --red: #dc2626;
                --yellow: #facc15;
                --green: #22c55e;
                --blue: #3b82f6;
                --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
                --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
                --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
                --radius-sm: 0.375rem;
                --radius-md: 0.5rem;
                --radius-lg: 0.75rem;
                --radius-xl: 1rem;
                --transition: all 0.2s ease;
            }
            
            /* Reset global */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            /* Base styles */
            .stApp {
                background-color: var(--bg-primary);
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
            }
            
            /* Ocultar elementos de Streamlit */
            #MainMenu, footer, header {
                display: none !important;
            }
            
            .viewerBadge_container__r5tak {
                display: none !important;
            }
            
            [data-testid="stHeader"] {
                display: none !important;
            }
            
            [data-testid="stToolbar"] {
                display: none !important;
            }
            
            /* Eliminar padding default */
            .block-container {
                padding: 0 !important;
                max-width: none !important;
            }
            
            [data-testid="stAppViewContainer"] {
                padding-top: 0 !important;
            }
            
            /* Sidebar styling */
            section[data-testid="stSidebar"] {
                background-color: var(--bg-secondary);
                border-right: 1px solid var(--border-color);
                width: 280px;
            }
            
            section[data-testid="stSidebar"] > div {
                padding: 0;
                height: 100vh;
                background-color: var(--bg-secondary);
            }
            
            /* Botones */
            .stButton > button {
                background-color: transparent;
                border: 1px solid var(--border-color);
                color: var(--text-secondary);
                padding: 0.75rem 1rem;
                margin-bottom: 0.25rem;
                border-radius: var(--radius-md);
                font-size: 0.9375rem;
                font-weight: 500;
                transition: var(--transition);
                width: 100%;
                text-align: left;
                display: flex;
                align-items: center;
                gap: 0.75rem;
            }
            
            .stButton > button:hover {
                background-color: var(--bg-tertiary);
                color: var(--text-primary);
                border-color: var(--primary-color);
            }
            
            .stButton > button:disabled {
                background-color: var(--primary-color) !important;
                color: white !important;
                cursor: default !important;
                border-color: var(--primary-color) !important;
                opacity: 1 !important;
            }
            
            /* Forms */
            .stTextInput > div > div > input,
            .stNumberInput > div > div > input,
            .stSelectbox > div > div > div {
                background-color: var(--bg-tertiary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-md) !important;
                color: var(--text-primary) !important;
                padding: 0.75rem 1rem !important;
                font-size: 0.9375rem !important;
                transition: var(--transition) !important;
            }
            
            .stTextInput > div > div > input:focus,
            .stNumberInput > div > div > input:focus,
            .stSelectbox > div > div > div:focus {
                border-color: var(--primary-color) !important;
                box-shadow: 0 0 0 2px rgba(16, 163, 127, 0.1) !important;
                outline: none !important;
            }
            
            .stTextInput > label,
            .stNumberInput > label,
            .stSelectbox > label {
                color: var(--text-primary) !important;
                font-weight: 500 !important;
                font-size: 0.9375rem !important;
                margin-bottom: 0.5rem !important;
            }
            
            /* Chat input */
            .stChatInput {
                position: fixed !important;
                bottom: 0;
                left: 0;
                right: 0;
                background-color: var(--bg-secondary);
                border-top: 1px solid var(--border-color);
                padding: 1rem 0;
                z-index: 100;
            }
            
            .stChatInput > div {
                max-width: 900px;
                margin: 0 auto;
                padding: 0 2rem;
            }
            
            .stChatInput textarea {
                background-color: var(--bg-tertiary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-lg) !important;
                color: var(--text-primary) !important;
                padding: 0.875rem 1.25rem !important;
                font-size: 0.9375rem !important;
                resize: none !important;
                transition: var(--transition) !important;
                font-family: inherit !important;
            }
            
            .stChatInput textarea:focus {
                border-color: var(--primary-color) !important;
                box-shadow: 0 0 0 2px rgba(16, 163, 127, 0.1) !important;
                outline: none !important;
            }
            
            .stChatInput textarea::placeholder {
                color: var(--text-muted) !important;
            }
            
            /* Alerts */
            .stAlert {
                border-radius: var(--radius-lg) !important;
                border: 1px solid !important;
                font-size: 0.9375rem !important;
            }
            
            .stAlert[data-testid="stSuccess"] {
                background-color: rgba(34, 197, 94, 0.1) !important;
                border-color: var(--green) !important;
                color: var(--green) !important;
            }
            
            .stAlert[data-testid="stError"] {
                background-color: rgba(220, 38, 38, 0.1) !important;
                border-color: var(--red) !important;
                color: var(--text-primary) !important;
            }
            
            .stAlert[data-testid="stWarning"] {
                background-color: rgba(250, 204, 21, 0.1) !important;
                border-color: var(--yellow) !important;
                color: var(--text-primary) !important;
            }
            
            .stAlert[data-testid="stInfo"] {
                background-color: rgba(59, 130, 246, 0.1) !important;
                border-color: var(--blue) !important;
                color: var(--text-primary) !important;
            }
            
            /* Tabs */
            .stTabs {
                background-color: transparent !important;
            }
            
            .stTabs [data-baseweb="tab-list"] {
                background-color: var(--bg-tertiary);
                border-radius: var(--radius-lg);
                padding: 0.25rem;
                gap: 0.25rem;
                border: 1px solid var(--border-color);
            }
            
            .stTabs [data-baseweb="tab"] {
                background-color: transparent;
                color: var(--text-secondary);
                border-radius: var(--radius-md);
                padding: 0.75rem 1.5rem;
                font-weight: 500;
                font-size: 0.9375rem;
                transition: var(--transition);
                border: none;
            }
            
            .stTabs [data-baseweb="tab"]:hover {
                background-color: var(--bg-secondary);
                color: var(--text-primary);
            }
            
            .stTabs [aria-selected="true"] {
                background-color: var(--primary-color) !important;
                color: white !important;
                box-shadow: var(--shadow-sm);
            }
            
            .stTabs [data-baseweb="tab-highlight"],
            .stTabs [data-baseweb="tab-border"] {
                display: none !important;
            }
            
            /* Expander */
            .streamlit-expanderHeader {
                background-color: var(--bg-tertiary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-lg) !important;
                color: var(--text-primary) !important;
                font-weight: 500 !important;
                font-size: 0.9375rem !important;
                transition: var(--transition) !important;
                padding: 1rem 1.25rem !important;
            }
            
            .streamlit-expanderHeader:hover {
                border-color: var(--primary-color) !important;
                box-shadow: var(--shadow-sm) !important;
            }
            
            [data-baseweb="accordion"] {
                background-color: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-lg);
                overflow: hidden;
            }
            
            /* Cards */
            .card {
                background-color: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-xl);
                padding: 2rem;
                margin-bottom: 1.5rem;
                transition: var(--transition);
            }
            
            .card:hover {
                border-color: var(--primary-color);
                box-shadow: var(--shadow-md);
            }
            
            /* Code blocks */
            .stCodeBlock {
                background-color: var(--bg-tertiary) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: var(--radius-lg) !important;
            }
            
            .stCodeBlock > div {
                background-color: var(--bg-tertiary) !important;
            }
            
            code {
                color: var(--primary-light) !important;
                background-color: var(--bg-tertiary) !important;
                padding: 0.125rem 0.375rem !important;
                border-radius: var(--radius-sm) !important;
                font-size: 0.875rem !important;
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 8px;
                height: 8px;
            }
            
            ::-webkit-scrollbar-track {
                background-color: transparent;
            }
            
            ::-webkit-scrollbar-thumb {
                background-color: var(--border-color);
                border-radius: var(--radius-md);
                transition: var(--transition);
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background-color: var(--text-muted);
            }
            
            /* Animations */
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            /* Utility classes */
            .main-title {
                font-size: 2rem;
                font-weight: 700;
                background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-align: center;
                margin: 2rem 0 1rem 0;
                letter-spacing: -0.02em;
            }
            
            .sub-title {
                font-size: 1.125rem;
                color: var(--text-secondary);
                text-align: center;
                margin-bottom: 2rem;
                font-weight: 400;
            }
            
            /* Estado cards */
            .estado-excelente {
                background: linear-gradient(135deg, var(--green), #16a34a);
                color: white;
                padding: 1.5rem;
                border-radius: var(--radius-lg);
                text-align: center;
                font-weight: 600;
                box-shadow: var(--shadow-lg);
            }
            
            .estado-bueno {
                background: linear-gradient(135deg, var(--blue), #2563eb);
                color: white;
                padding: 1.5rem;
                border-radius: var(--radius-lg);
                text-align: center;
                font-weight: 600;
                box-shadow: var(--shadow-lg);
            }
            
            .estado-regular {
                background: linear-gradient(135deg, var(--yellow), #eab308);
                color: white;
                padding: 1.5rem;
                border-radius: var(--radius-lg);
                text-align: center;
                font-weight: 600;
                box-shadow: var(--shadow-lg);
            }
            
            .estado-critico {
                background: linear-gradient(135deg, var(--red), #b91c1c);
                color: white;
                padding: 1.5rem;
                border-radius: var(--radius-lg);
                text-align: center;
                font-weight: 600;
                box-shadow: var(--shadow-lg);
            }
            
            /* Highlight metrics */
            .highlight-metric {
                background-color: var(--bg-tertiary);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-lg);
                padding: 1.5rem;
                margin-bottom: 1rem;
                position: relative;
                overflow: hidden;
                transition: var(--transition);
            }
            
            .highlight-metric::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 4px;
                height: 100%;
                background: linear-gradient(180deg, var(--primary-color), var(--primary-light));
            }
            
            .highlight-metric:hover {
                transform: translateX(4px);
                border-color: var(--primary-color);
                box-shadow: var(--shadow-md);
            }
            
            /* Recomendaciones */
            .recomendacion {
                background-color: var(--bg-tertiary);
                border-left: 4px solid var(--primary-color);
                padding: 1rem 1.5rem;
                margin-bottom: 1rem;
                border-radius: var(--radius-md);
                transition: var(--transition);
            }
            
            .recomendacion:hover {
                transform: translateX(4px);
                box-shadow: var(--shadow-md);
            }
            
            /* Responsive */
            @media (max-width: 768px) {
                .chat-container {
                    padding: 1rem;
                }
                
                .message-content {
                    max-width: 85%;
                }
                
                .welcome-title {
                    font-size: 2rem;
                }
                
                .features-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """