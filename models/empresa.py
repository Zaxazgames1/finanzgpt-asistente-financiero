class Empresa:
    """
    Clase que representa una empresa con sus datos financieros.
    """
    def __init__(self, nombre="", sector="Tecnología", ganancias=0.0, 
                 empleados=1, activos=0.0, cartera=0.0, deudas=0.0):
        """
        Inicializa una nueva instancia de Empresa.
        
        Args:
            nombre (str): Nombre de la empresa
            sector (str): Sector económico de la empresa
            ganancias (float): Ganancias anuales en COP
            empleados (int): Número de empleados
            activos (float): Valor total de activos en COP
            cartera (float): Valor en cartera por cobrar en COP
            deudas (float): Valor de deudas en COP
        """
        self.nombre = nombre
        self.sector = sector
        self.ganancias = ganancias
        self.empleados = empleados
        self.activos = activos
        self.cartera = cartera
        self.deudas = deudas
    
    @property
    def data_dict(self):
        """
        Retorna un diccionario con los datos de la empresa.
        
        Returns:
            dict: Diccionario con los datos de la empresa
        """
        return {
            'nombre': self.nombre,
            'sector': self.sector,
            'ganancias': self.ganancias,
            'empleados': self.empleados,
            'activos': self.activos,
            'cartera': self.cartera,
            'deudas': self.deudas
        }
    
    @classmethod
    def from_dict(cls, data_dict):
        """
        Crea una instancia de Empresa a partir de un diccionario.
        
        Args:
            data_dict (dict): Diccionario con los datos de la empresa
            
        Returns:
            Empresa: Nueva instancia de Empresa
        """
        return cls(
            nombre=data_dict.get('nombre', ""),
            sector=data_dict.get('sector', "Tecnología"),
            ganancias=float(data_dict.get('ganancias', 0.0)),
            empleados=int(data_dict.get('empleados', 1)),
            activos=float(data_dict.get('activos', 0.0)),
            cartera=float(data_dict.get('cartera', 0.0)),
            deudas=float(data_dict.get('deudas', 0.0))
        )