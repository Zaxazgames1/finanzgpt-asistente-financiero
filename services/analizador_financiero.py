import numpy as np
from models.empresa import Empresa
from models.analisis import ResultadoAnalisis
from services.nlp_service import NLPService

class AnalizadorFinanciero:
    """
    Servicio para realizar análisis financieros de empresas.
    """
    def __init__(self):
        """
        Inicializa el analizador financiero.
        """
        self.nlp_service = NLPService()
        self.limites_sector = {
            'tecnología': {
                'endeudamiento': 0.6,
                'rentabilidad': 0.15,
                'productividad': 100000000,  # 100 millones COP por empleado
                'rotacion': 60
            },
            'comercio': {
                'endeudamiento': 0.5,
                'rentabilidad': 0.08,
                'productividad': 50000000,  # 50 millones COP por empleado
                'rotacion': 45
            },
            'manufactura': {
                'endeudamiento': 0.55,
                'rentabilidad': 0.1,
                'productividad': 70000000,  # 70 millones COP por empleado
                'rotacion': 50
            },
            'servicios': {
                'endeudamiento': 0.45,
                'rentabilidad': 0.12,
                'productividad': 60000000,  # 60 millones COP por empleado
                'rotacion': 30
            },
            'otro': {
                'endeudamiento': 0.5,
                'rentabilidad': 0.1,
                'productividad': 60000000,  # 60 millones COP por empleado
                'rotacion': 45
            }
        }
    
    def calcular_ratio_endeudamiento(self, valor_deudas, valor_activos):
        """
        Calcula el ratio de endeudamiento de la empresa.
        
        Args:
            valor_deudas (float): Valor total de deudas
            valor_activos (float): Valor total de activos
            
        Returns:
            float: Ratio de endeudamiento
        """
        if valor_activos == 0:
            return float('inf')
        return valor_deudas / valor_activos
    
    def calcular_rentabilidad(self, ganancias_anuales, valor_activos):
        """
        Calcula la rentabilidad económica (ROA).
        
        Args:
            ganancias_anuales (float): Ganancias anuales
            valor_activos (float): Valor total de activos
            
        Returns:
            float: Rentabilidad sobre activos
        """
        if valor_activos == 0:
            return 0
        return ganancias_anuales / valor_activos
    
    def calcular_productividad_empleado(self, ganancias_anuales, num_empleados):
        """
        Calcula la productividad por empleado.
        
        Args:
            ganancias_anuales (float): Ganancias anuales
            num_empleados (int): Número de empleados
            
        Returns:
            float: Productividad por empleado
        """
        if num_empleados == 0:
            return 0
        return ganancias_anuales / num_empleados
    
    def calcular_rotacion_cartera(self, valor_cartera, ganancias_anuales):
        """
        Calcula la rotación de cartera.
        
        Args:
            valor_cartera (float): Valor en cartera
            ganancias_anuales (float): Ganancias anuales
            
        Returns:
            float: Rotación de cartera (días)
        """
        if ganancias_anuales == 0:
            return float('inf')
        return (valor_cartera / ganancias_anuales) * 365  # Días de rotación
    
    def analizar_empresa(self, empresa):
        """
        Realiza un análisis completo de la situación económica de la empresa.
        
        Args:
            empresa (Empresa): Instancia de Empresa a analizar
            
        Returns:
            ResultadoAnalisis: Resultados del análisis
        """
        # Calcular indicadores
        ratio_endeudamiento = self.calcular_ratio_endeudamiento(empresa.deudas, empresa.activos)
        rentabilidad = self.calcular_rentabilidad(empresa.ganancias, empresa.activos)
        productividad = self.calcular_productividad_empleado(empresa.ganancias, empresa.empleados)
        rotacion_cartera = self.calcular_rotacion_cartera(empresa.cartera, empresa.ganancias)
        
        # Si el sector no está en los predefinidos, usar "otro"
        sector_analisis = empresa.sector.lower()
        if sector_analisis not in self.limites_sector:
            sector_analisis = 'otro'
        
        # Evaluación por indicador
        evaluacion = {
            'endeudamiento': 'bueno' if ratio_endeudamiento <= self.limites_sector[sector_analisis]['endeudamiento'] else 'alto',
            'rentabilidad': 'buena' if rentabilidad >= self.limites_sector[sector_analisis]['rentabilidad'] else 'baja',
            'productividad': 'buena' if productividad >= self.limites_sector[sector_analisis]['productividad'] else 'baja',
            'rotacion': 'buena' if rotacion_cartera <= self.limites_sector[sector_analisis]['rotacion'] else 'alta'
        }
        
        # Evaluación general
        puntos_positivos = sum(1 for valor in evaluacion.values() if valor in ['bueno', 'buena'])
        
        if puntos_positivos >= 3:
            estado_general = "Excelente"
        elif puntos_positivos == 2:
            estado_general = "Bueno"
        elif puntos_positivos == 1:
            estado_general = "Regular"
        else:
            estado_general = "Crítico"
        
        # Preparar recomendaciones basadas en puntos débiles
        recomendaciones = []
        
        if evaluacion['endeudamiento'] == 'alto':
            recomendaciones.append("Reducir el nivel de endeudamiento, considerar reestructuración de deuda.")
        
        if evaluacion['rentabilidad'] == 'baja':
            recomendaciones.append("Mejorar la eficiencia operativa y revisar la estructura de costos.")
        
        if evaluacion['productividad'] == 'baja':
            recomendaciones.append("Optimizar procesos y/o implementar programas de capacitación para los empleados.")
        
        if evaluacion['rotacion'] == 'alta':
            recomendaciones.append("Mejorar las políticas de cobro y gestión de cartera.")
        
        # Procesamiento NLP de ejemplo
        tokens_nombre = self.nlp_service.tokenizar_texto(empresa.nombre)
        lemas_sector = self.nlp_service.lematizar_texto(empresa.sector)
        pos_tags = self.nlp_service.pos_tagging(f"{empresa.nombre} es una empresa del sector {empresa.sector}")
        
        # Crear embedding para futuras comparaciones
        embedding = self.nlp_service.crear_embedding(
            f"Empresa {empresa.nombre} del sector {empresa.sector} con {empresa.empleados} empleados"
        )
        
        # Crear objeto de resultado
        indicadores = {
            'ratio_endeudamiento': ratio_endeudamiento,
            'rentabilidad': rentabilidad,
            'productividad': productividad,
            'rotacion_cartera': rotacion_cartera
        }
        
        nlp_ejemplo = {
            'tokens': tokens_nombre,
            'lemas': lemas_sector,
            'pos_tags': pos_tags,
            'embedding_dim': len(embedding) if isinstance(embedding, np.ndarray) else 0
        }
        
        resultado = ResultadoAnalisis(
            nombre=empresa.nombre,
            sector=empresa.sector,
            indicadores=indicadores,
            evaluacion=evaluacion,
            estado_general=estado_general,
            recomendaciones=recomendaciones,
            nlp_ejemplo=nlp_ejemplo
        )
        
        return resultado