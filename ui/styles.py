class StylesUI:
    """
    Clase que contiene los estilos CSS para la aplicación.
    """
    @staticmethod
    def get_css():
        """
        Retorna los estilos CSS personalizados.
        
        Returns:
            str: Código CSS
        """
        return """
        <style>
            /* Estilos generales */
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #353740;
                background-color: #F7F7F8;
            }
            
            /* Títulos y encabezados */
            .main-title {
                font-size: 2.2rem;
                font-weight: 600;
                color: #10A37F;
                margin-bottom: 1rem;
                text-align: center;
            }
            
            .sub-title {
                font-size: 1.4rem;
                font-weight: 500;
                color: #444654;
                margin-bottom: 1rem;
                text-align: center;
            }
            
            /* Mensajes de chat */
            .chat-container {
                display: flex;
                flex-direction: column;
                gap: 10px;
                padding: 10px;
                max-width: 900px;
                margin: 0 auto;
            }
            
            .chat-message-user {
                background-color: #FFFFFF;
                border-radius: 8px;
                padding: 15px;
                margin: 5px 0;
                box-shadow: 0 1px 2px rgba(0,0,0,0.1);
                color: #353740;
                font-size: 16px;
                position: relative;
                display: flex;
                align-items: flex-start;
            }
            
            .chat-message-bot {
                background-color: #F7F7F8;
                border-radius: 8px;
                padding: 15px;
                margin: 5px 0;
                box-shadow: 0 1px 2px rgba(0,0,0,0.1);
                color: #353740;
                font-size: 16px;
                position: relative;
                display: flex;
                align-items: flex-start;
            }
            
            .avatar {
                width: 30px;
                height: 30px;
                border-radius: 50%;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-right: 15px;
                flex-shrink: 0;
            }
            
            .avatar-user {
                background-color: #10A37F;
                color: white;
                font-weight: bold;
            }
            
            .avatar-bot {
                background-color: #0FA47F;
                color: white;
                font-weight: bold;
            }
            
            .message-content {
                flex-grow: 1;
                line-height: 1.5;
            }
            
            /* Tarjetas y componentes */
            .card {
                background-color: #FFFFFF;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 20px;
                color: #353740;
            }
            
            .highlight-metric {
                background-color: #F8FAFC;
                padding: 15px;
                border-radius: 8px;
                margin: 10px 0;
                font-weight: 500;
                color: #353740;
                border-left: 4px solid #10A37F;
                transition: all 0.3s ease;
            }
            
            .highlight-metric:hover {
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            
            /* Estados financieros */
            .estado-excelente {
                background-color: #10A37F;
                color: white;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                font-weight: 600;
                box-shadow: 0 2px 8px rgba(16, 163, 127, 0.3);
            }
            
            .estado-bueno {
                background-color: #3B82F6;
                color: white;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                font-weight: 600;
                box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
            }
            
            .estado-regular {
                background-color: #F59E0B;
                color: white;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                font-weight: 600;
                box-shadow: 0 2px 8px rgba(245, 158, 11, 0.3);
            }
            
            .estado-critico {
                background-color: #EF4444;
                color: white;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                font-weight: 600;
                box-shadow: 0 2px 8px rgba(239, 68, 68, 0.3);
            }
            
            /* Recomendaciones */
            .recomendacion {
                background-color: #FFFBEB;
                padding: 12px;
                border-radius: 8px;
                margin: 8px 0;
                border-left: 4px solid #F59E0B;
                color: #353740;
                font-weight: 400;
                transition: transform 0.2s ease;
            }
            
            .recomendacion:hover {
                transform: translateX(5px);
            }
            
            /* Formulario */
            .stTextInput > div > div > input {
                border-radius: 8px;
                border: 1px solid #E5E7EB;
                padding: 12px;
                font-size: 16px;
            }
            
            .stTextInput > div > div > input:focus {
                border-color: #10A37F;
                box-shadow: 0 0 0 2px rgba(16, 163, 127, 0.2);
            }
            
            .stButton > button {
                background-color: #10A37F;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: 500;
                border: none;
                transition: all 0.3s ease;
            }
            
            .stButton > button:hover {
                background-color: #0C8D6C;
                box-shadow: 0 4px 12px rgba(16, 163, 127, 0.3);
            }
            
            /* Chat input */
            .stChatInput > div > textarea {
                border-radius: 8px;
                border: 1px solid #E5E7EB;
                padding: 12px;
                font-size: 16px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            }
            
            .stChatInput > div > textarea:focus {
                border-color: #10A37F;
                box-shadow: 0 0 0 2px rgba(16, 163, 127, 0.2);
            }
            
            /* Sidebar */
            .sidebar .sidebar-content {
                background-color: #FFFFFF;
            }
            
            /* Esconder elementos de streamlit */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* Botones de navegación */
            .nav-button {
                background-color: #F8FAFC;
                border: 1px solid #E5E7EB;
                border-radius: 8px;
                padding: 10px;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                display: block;
                width: 100%;
                margin-bottom: 8px;
                font-weight: 500;
                color: #444654;
            }
            
            .nav-button:hover {
                background-color: #F0F9F6;
                border-color: #10A37F;
                color: #10A37F;
            }
            
            .nav-button-active {
                background-color: #10A37F;
                color: white;
                border: 1px solid #10A37F;
                border-radius: 8px;
                padding: 10px;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s ease;
                display: block;
                width: 100%;
                margin-bottom: 8px;
                font-weight: 500;
            }
            
            /* Animación de pensamiento */
            .thinking-animation {
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 20px 0;
            }
            
            .thinking-dot {
                width: 10px;
                height: 10px;
                margin: 0 5px;
                background-color: #10A37F;
                border-radius: 50%;
                animation: pulse 1.5s infinite ease-in-out;
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
        </style>
        """