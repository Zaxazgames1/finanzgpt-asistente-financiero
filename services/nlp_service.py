import re
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class NLPService:
    """
    Servicio para procesamiento de lenguaje natural.
    """
    def __init__(self):
        """
        Inicializa el servicio NLP y carga los modelos necesarios.
        """
        # Descargar recursos necesarios de NLTK
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)

        # Cargar el modelo de spaCy para español
        self.nlp = spacy.load('es_core_news_sm')
    
    def tokenizar_texto(self, texto):
        """
        Tokeniza un texto en palabras individuales.
        
        Args:
            texto (str): Texto a tokenizar
            
        Returns:
            list: Lista de tokens
        """
        return word_tokenize(texto.lower())
    
    def lematizar_texto(self, texto):
        """
        Lematiza un texto utilizando spaCy.
        
        Args:
            texto (str): Texto a lematizar
            
        Returns:
            list: Lista de lemas
        """
        doc = self.nlp(texto.lower())
        return [token.lemma_ for token in doc]
    
    def pos_tagging(self, texto):
        """
        Realiza el etiquetado gramatical (POS tagging) de un texto.
        
        Args:
            texto (str): Texto para etiquetar
            
        Returns:
            list: Lista de tuplas (palabra, etiqueta)
        """
        doc = self.nlp(texto.lower())
        return [(token.text, token.pos_) for token in doc]
    
    def crear_embedding(self, texto):
        """
        Crea un embedding simple para un texto utilizando CountVectorizer.
        
        Args:
            texto (str): Texto para crear embedding
            
        Returns:
            numpy.ndarray: Vector de embedding
        """
        vectorizer = CountVectorizer()
        return vectorizer.fit_transform([texto]).toarray()[0]
    
    def similaridad_textos(self, texto1, texto2):
        """
        Calcula la similaridad coseno entre dos textos.
        
        Args:
            texto1 (str): Primer texto
            texto2 (str): Segundo texto
            
        Returns:
            float: Valor de similaridad
        """
        vectorizer = CountVectorizer().fit([texto1, texto2])
        vectores = vectorizer.transform([texto1, texto2])
        return cosine_similarity(vectores[0:1], vectores[1:2])[0][0]
    
    def normalizar_texto(self, texto):
        """
        Normaliza un texto: elimina caracteres especiales, convierte a minúsculas.
        
        Args:
            texto (str): Texto a normalizar
            
        Returns:
            str: Texto normalizado
        """
        # Convertir a minúsculas
        texto = texto.lower()
        # Eliminar caracteres especiales
        texto = re.sub(r'[^\w\s]', '', texto)
        # Eliminar números
        texto = re.sub(r'\d+', '', texto)
        # Eliminar espacios múltiples
        texto = re.sub(r'\s+', ' ', texto).strip()
        return texto
    
    def extraer_keywords(self, texto, num_palabras=5):
        """
        Extrae palabras clave de un texto basado en frecuencia y relevancia.
        
        Args:
            texto (str): Texto para extraer palabras clave
            num_palabras (int): Número de palabras clave a extraer
            
        Returns:
            list: Lista de palabras clave
        """
        doc = self.nlp(texto.lower())
        palabras = [token.text for token in doc if not token.is_stop and token.is_alpha]
        frecuencia = {}
        
        for palabra in palabras:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
        
        # Ordenar por frecuencia
        keywords = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
        return [palabra for palabra, _ in keywords[:num_palabras]]
    
    def es_mensaje_no_financiero(self, mensaje):
        """
        Detecta si un mensaje está fuera del ámbito financiero.
        
        Args:
            mensaje (str): Mensaje del usuario
            
        Returns:
            tuple: (bool, str) - (es_no_financiero, tipo)
        """
        # Palabras clave de saludos comunes
        saludos = ['hola', 'buenos días', 'buenas tardes', 'buenas noches', 'saludos', 'qué tal', 'como estas', 'cómo estás', 'como vas', 'qué hay']
        
        # Palabras clave de despedidas
        despedidas = ['adiós', 'chao', 'hasta luego', 'nos vemos', 'bye', 'hasta pronto', 'hasta mañana']
        
        # Palabras clave sobre estados emocionales
        emociones = ['triste', 'feliz', 'deprimido', 'ansioso', 'estresado', 'cansado', 'aburrido', 'mal', 'bien', 'enfermo']
        
        # Palabras clave sobre temas personales
        temas_personales = ['salud', 'vida', 'familia', 'amigo', 'amor', 'relación', 'matrimonio', 'hijo', 'niño', 'mascota']
        
        # Peticiones de ayuda generales
        ayuda_general = ['ayuda', 'ayúdame', 'socorro', 'sos', 'help']
        
        # Verificar si el mensaje coincide con alguna categoría
        mensaje_lower = mensaje.lower()
        
        # Detectar saludos simples
        if any(saludo == mensaje_lower for saludo in saludos):
            return True, "saludo"
        
        # Detectar despedidas simples
        if any(despedida == mensaje_lower for despedida in despedidas):
            return True, "despedida"
            
        # Detectar si es una petición de ayuda general
        if any(ayuda == mensaje_lower for ayuda in ayuda_general):
            return True, "ayuda"
        
        # Detectar emociones o temas personales
        if any(emocion in mensaje_lower for emocion in emociones):
            return True, "emocion"
        
        if any(tema in mensaje_lower for tema in temas_personales):
            return True, "personal"
        
        # Detectar mensajes muy cortos o sin palabras clave financieras
        if len(mensaje_lower.split()) < 2:
            # Puede ser una respuesta corta no financiera
            return True, "corto"
        
        # Palabras clave financieras para verificar si es un mensaje financiero
        palabras_financieras = [
            'finanza', 'empresa', 'dinero', 'capital', 'beneficio', 'ganancia', 'activo', 'pasivo', 
            'deuda', 'préstamo', 'inversion', 'cartera', 'crédito', 'liquidez', 'rentabilidad', 
            'margen', 'impuesto', 'pago', 'cobro', 'factura', 'balance', 'contabilidad', 'inventario',
            'flujo', 'costo', 'ingreso', 'gasto', 'ratio', 'indicador', 'estado', 'análisis',
            'endeudamiento', 'productividad', 'rotación'
        ]
        
        # Si contiene alguna palabra financiera, considerarlo como mensaje financiero
        if any(palabra in mensaje_lower for palabra in palabras_financieras):
            return False, "financiero"
        
        # Por defecto, considerar como no financiero
        return True, "otro"