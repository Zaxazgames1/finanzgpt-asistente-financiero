#!/usr/bin/env python3
"""
Script de configuración inicial para FinanzGPT con Flan-T5
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala todos los requerimientos necesarios"""
    print("📦 Instalando requerimientos...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ Requerimientos instalados")

def download_nltk_data():
    """Descarga los datos necesarios de NLTK"""
    print("📚 Descargando datos de NLTK...")
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    print("✅ Datos de NLTK descargados")

def download_spacy_model():
    """Descarga el modelo de spaCy para español"""
    print("🌐 Descargando modelo de spaCy...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "es_core_news_sm"])
    print("✅ Modelo de spaCy descargado")

def test_flan_t5():
    """Prueba que Flan-T5 se puede cargar correctamente"""
    print("🤖 Probando Flan-T5...")
    try:
        from transformers import T5Tokenizer, T5ForConditionalGeneration
        import torch
        
        # Esto descargará el modelo la primera vez
        print("Descargando modelo Flan-T5-small (puede tomar unos minutos)...")
        tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
        model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")
        
        # Prueba simple
        input_text = "Translate to Spanish: Hello, how are you?"
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50)
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print(f"✅ Flan-T5 funcionando correctamente")
        print(f"   Prueba: {input_text}")
        print(f"   Resultado: {result}")
        
    except Exception as e:
        print(f"❌ Error al probar Flan-T5: {e}")
        sys.exit(1)

def main():
    print("""
    🚀 Configuración de FinanzGPT con Flan-T5
    =======================================
    
    Este script instalará todas las dependencias necesarias
    para ejecutar FinanzGPT con capacidades de generación
    de texto similares a ChatGPT.
    
    Componentes a instalar:
    - Librerías de Python (streamlit, transformers, etc.)
    - Datos de NLTK
    - Modelo de spaCy para español
    - Modelo Flan-T5-small de Google (300MB)
    
    """)
    
    try:
        # Instalar requerimientos
        install_requirements()
        
        # Descargar datos de NLTK
        download_nltk_data()
        
        # Descargar modelo de spaCy
        download_spacy_model()
        
        # Probar Flan-T5
        test_flan_t5()
        
        print("""
        ✨ ¡Configuración completada con éxito!
        
        Para ejecutar la aplicación:
        streamlit run app.py
        
        Nota: La primera vez que ejecutes la aplicación,
        tomará unos segundos adicionales mientras carga
        el modelo de Flan-T5 en memoria.
        """)
        
    except Exception as e:
        print(f"❌ Error durante la configuración: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()