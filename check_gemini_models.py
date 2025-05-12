import requests
import json

def listar_modelos_disponibles():
    """Lista todos los modelos disponibles con tu API key"""
    
    # Tu API key
    api_key = "AIzaSyA-Vuy7H8fSsJ1gLAaJDVg-jMtGwpCP6kQ"
    
    # URL para listar modelos
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    try:
        # Hacer la petición
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            print("🤖 MODELOS DISPONIBLES EN TU API:\n")
            print("=" * 50)
            
            if 'models' in data:
                for model in data['models']:
                    print(f"\n📌 Modelo: {model['name']}")
                    print(f"   Nombre: {model.get('displayName', 'N/A')}")
                    print(f"   Descripción: {model.get('description', 'N/A')}")
                    print(f"   Versión: {model.get('version', 'N/A')}")
                    
                    # Métodos soportados
                    if 'supportedGenerationMethods' in model:
                        print(f"   Métodos soportados: {', '.join(model['supportedGenerationMethods'])}")
                    
                    # Límites
                    if 'inputTokenLimit' in model:
                        print(f"   Límite de tokens de entrada: {model['inputTokenLimit']}")
                    if 'outputTokenLimit' in model:
                        print(f"   Límite de tokens de salida: {model['outputTokenLimit']}")
                    
                    print("-" * 30)
            else:
                print("No se encontraron modelos")
                
            # Mostrar cuotas de uso
            print("\n💳 INFORMACIÓN DE CUOTAS Y LÍMITES:")
            print("=" * 50)
            print("\nPara ver tus cuotas y límites actuales, visita:")
            print("https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas")
            
            print("\n📊 PRECIOS TÍPICOS (pueden variar):")
            print("- Gemini 1.5 Flash: $0.075 por millón de tokens")
            print("- Gemini 1.5 Pro: $3.50 por millón de tokens")
            print("- Gemini 2.0 Flash: Ver consola de Google Cloud")
            
            print("\n✅ RECOMENDACIONES:")
            print("1. Usa el modelo más económico que cumpla tus necesidades")
            print("2. Monitorea tu uso en Google Cloud Console")
            print("3. Configura alertas de facturación si es necesario")
            
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Error al consultar modelos: {e}")
    
    # Probar que los modelos funcionan
    print("\n🧪 PROBANDO MODELOS POPULARES:")
    print("=" * 50)
    
    modelos_a_probar = [
        "gemini-1.5-flash-latest",
        "gemini-1.5-flash",
        "gemini-2.0-flash-exp",
        "gemini-1.5-pro-latest",
        "gemini-1.5-pro",
        "gemini-pro",
        "gemini-pro-vision"
    ]
    
    for modelo in modelos_a_probar:
        probar_modelo(modelo, api_key)

def probar_modelo(modelo, api_key):
    """Prueba si un modelo específico funciona"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{
                "text": "Di 'hola' en español"
            }]
        }]
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ {modelo}: FUNCIONA")
            # Mostrar respuesta
            result = response.json()
            if 'candidates' in result:
                texto = result['candidates'][0]['content']['parts'][0]['text']
                print(f"   Respuesta: {texto[:50]}...")
        else:
            print(f"❌ {modelo}: NO DISPONIBLE ({response.status_code})")
    except Exception as e:
        print(f"❌ {modelo}: ERROR ({str(e)})")

if __name__ == "__main__":
    print("🔍 VERIFICANDO MODELOS DISPONIBLES PARA TU API KEY...")
    print("=" * 50)
    listar_modelos_disponibles()
    
    print("\n\n📝 CÓMO ADMINISTRAR TU USO:")
    print("=" * 50)
    print("1. Ve a: https://console.cloud.google.com")
    print("2. Selecciona tu proyecto")
    print("3. Ve a 'APIs & Services' > 'Credentials'")
    print("4. Revisa 'Quotas' para ver límites")
    print("5. Ve a 'Billing' para ver costos")
    
    print("\n💡 CONSEJOS PARA AHORRAR:")
    print("- Usa modelos Flash para respuestas rápidas")
    print("- Usa modelos Pro solo para análisis complejos")
    print("- Implementa caché de respuestas comunes")
    print("- Limita el tamaño de tokens por respuesta")