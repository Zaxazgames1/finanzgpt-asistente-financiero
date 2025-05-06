class Formatters:
    """
    Clase con utilidades para formateo de datos.
    """
    @staticmethod
    def formato_numero(numero):
        """
        Formatea un número grande para mejor legibilidad.
        Ejemplo: 1234567 -> 1,234,567
        
        Args:
            numero (float): Número a formatear
        
        Returns:
            str: Número formateado
        """
        return f"{numero:,.0f}"
    
    @staticmethod
    def formato_porcentaje(numero):
        """
        Formatea un número como porcentaje.
        Ejemplo: 0.156 -> 15.6%
        
        Args:
            numero (float): Número a formatear
        
        Returns:
            str: Porcentaje formateado
        """
        return f"{numero:.1%}"
    
    @staticmethod
    def formato_moneda(numero, simbolo="$", moneda="COP"):
        """
        Formatea un número como moneda.
        Ejemplo: 1234567 -> $1,234,567 COP
        
        Args:
            numero (float): Número a formatear
            simbolo (str): Símbolo de moneda
            moneda (str): Código de moneda
        
        Returns:
            str: Valor monetario formateado
        """
        return f"{simbolo}{numero:,.0f} {moneda}"