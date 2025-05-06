class Validators:
    """
    Clase con utilidades para validación de datos.
    """
    @staticmethod
    def validar_numeros(valor, min_valor=0.0, nombre="valor"):
        """
        Valida que un valor numérico esté dentro de un rango aceptable.
        
        Args:
            valor (float): Valor a validar
            min_valor (float): Valor mínimo aceptable
            nombre (str): Nombre del campo para mensajes de error
            
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        if valor is None:
            return False, f"Por favor, ingresa un {nombre}."
        
        try:
            num_valor = float(valor)
            if num_valor < min_valor:
                return False, f"El {nombre} debe ser mayor o igual a {min_valor}."
            return True, ""
        except ValueError:
            return False, f"El {nombre} debe ser un número válido."