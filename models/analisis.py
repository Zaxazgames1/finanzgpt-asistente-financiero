class ResultadoAnalisis:
    """
    Clase que representa el resultado de un análisis financiero.
    """
    def __init__(self, nombre, sector, indicadores, evaluacion, 
                 estado_general, recomendaciones, nlp_ejemplo=None):
        """
        Inicializa una nueva instancia de ResultadoAnalisis.
        
        Args:
            nombre (str): Nombre de la empresa analizada
            sector (str): Sector económico de la empresa
            indicadores (dict): Diccionario con los indicadores financieros
            evaluacion (dict): Evaluación de cada indicador
            estado_general (str): Estado general de la empresa
            recomendaciones (list): Lista de recomendaciones
            nlp_ejemplo (dict, optional): Ejemplos de procesamiento NLP
        """
        self.nombre = nombre
        self.sector = sector
        self.indicadores = indicadores
        self.evaluacion = evaluacion
        self.estado_general = estado_general
        self.recomendaciones = recomendaciones
        self.nlp_ejemplo = nlp_ejemplo or {}
    
    @property
    def data_dict(self):
        """
        Retorna un diccionario con los resultados del análisis.
        
        Returns:
            dict: Diccionario con los resultados
        """
        return {
            'nombre': self.nombre,
            'sector': self.sector,
            'indicadores': self.indicadores,
            'evaluacion': self.evaluacion,
            'estado_general': self.estado_general,
            'recomendaciones': self.recomendaciones,
            'nlp_ejemplo': self.nlp_ejemplo
        }
    
    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una instancia de ResultadoAnalisis a partir de un diccionario.
        
        Args:
            data_dict (dict): Diccionario con los resultados
            
        Returns:
            ResultadoAnalisis: Nueva instancia de ResultadoAnalisis
        """
        return cls(
            nombre=data_dict.get('nombre', ""),
            sector=data_dict.get('sector', ""),
            indicadores=data_dict.get('indicadores', {}),
            evaluacion=data_dict.get('evaluacion', {}),
            estado_general=data_dict.get('estado_general', ""),
            recomendaciones=data_dict.get('recomendaciones', []),
            nlp_ejemplo=data_dict.get('nlp_ejemplo', {})
        )
    
    def generar_mensaje(self):
        """
        Genera un mensaje de resumen del análisis.
        
        Returns:
            str: Mensaje de resumen
        """
        mensaje = f"Análisis económico para {self.nombre} (Sector: {self.sector}):\n\n"
        mensaje += f"Estado económico general: {self.estado_general}\n\n"
        
        mensaje += "Indicadores analizados:\n"
        mensaje += f"• Ratio de endeudamiento: {self.indicadores['ratio_endeudamiento']:.2f} ({self.evaluacion['endeudamiento']})\n"
        mensaje += f"• Rentabilidad sobre activos: {self.indicadores['rentabilidad']:.2%} ({self.evaluacion['rentabilidad']})\n"
        mensaje += f"• Productividad por empleado: ${self.indicadores['productividad']:,.0f} COP ({self.evaluacion['productividad']})\n"
        mensaje += f"• Rotación de cartera: {self.indicadores['rotacion_cartera']:.1f} días ({self.evaluacion['rotacion']})\n\n"
        
        if self.recomendaciones:
            mensaje += "Recomendaciones:\n"
            for i, rec in enumerate(self.recomendaciones, 1):
                mensaje += f"{i}. {rec}\n"
        
        return mensaje