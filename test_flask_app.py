#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para la aplicación Flask
"""

import requests
import json
import time

def test_flask_app():
    """
    Probar la aplicación Flask
    """
    base_url = "http://localhost:5000"
    
    print("🧪 Iniciando pruebas de la aplicación Flask...")
    
    # Datos de prueba
    test_data = {
        "gender": 1,
        "lunch": 1,
        "test_preparation_course": 1,
        "reading_score": 85.5,
        "writing_score": 82.3,
        "race_ethnicity_group_E": 0,
        "parental_level_of_education_high_school": 1
    }
    
    try:
        # 1. Probar endpoint de salud
        print("\n1️⃣ Probando endpoint de salud...")
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ Salud: {health_data}")
            print(f"   Modelo cargado: {health_data.get('model_loaded', False)}")
            print(f"   Ruta del modelo: {health_data.get('model_path', 'N/A')}")
        else:
            print(f"❌ Error en salud: {response.status_code}")
            return False
        
        # 2. Probar validación de datos
        print("\n2️⃣ Probando validación de datos...")
        response = requests.post(
            f"{base_url}/api/escalar",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            validated_data = response.json()
            print(f"✅ Datos validados: {validated_data}")
        else:
            print(f"❌ Error en validación: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
        
        # 3. Probar predicción
        print("\n3️⃣ Probando predicción...")
        response = requests.post(
            f"{base_url}/predict",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            prediction_data = response.json()
            print(f"✅ Predicción exitosa:")
            print(f"   Calificación predicha: {prediction_data.get('math_score_prediction', 'N/A')}")
            print(f"   Confianza: {prediction_data.get('confidence', 'N/A')}")
            print(f"   Información del modelo: {prediction_data.get('model_info', 'N/A')}")
        else:
            print(f"❌ Error en predicción: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False
        
        # 4. Probar endpoint alternativo de predicción
        print("\n4️⃣ Probando endpoint alternativo de predicción...")
        response = requests.post(
            f"{base_url}/api/predict",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            prediction_data = response.json()
            print(f"✅ Predicción exitosa (endpoint alternativo):")
            print(f"   Calificación predicha: {prediction_data.get('math_score_prediction', 'N/A')}")
        else:
            print(f"❌ Error en predicción (endpoint alternativo): {response.status_code}")
            return False
        
        print("\n🎉 ¡Todas las pruebas pasaron exitosamente!")
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ No se pudo conectar al servidor Flask")
        print("   Asegúrate de que la aplicación esté ejecutándose en http://localhost:5000")
        return False
    except Exception as e:
        print(f"❌ Error durante las pruebas: {str(e)}")
        return False

def test_invalid_data():
    """
    Probar con datos inválidos
    """
    base_url = "http://localhost:5000"
    
    print("\n🧪 Probando con datos inválidos...")
    
    # Datos incompletos
    invalid_data = {
        "gender": 1,
        "reading_score": 85.5
        # Faltan variables requeridas
    }
    
    try:
        response = requests.post(
            f"{base_url}/predict",
            json=invalid_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 400:
            error_data = response.json()
            print(f"✅ Error manejado correctamente: {error_data.get('error', 'N/A')}")
            return True
        else:
            print(f"❌ Error no manejado correctamente: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error durante prueba de datos inválidos: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando pruebas de la aplicación Flask")
    print("=" * 50)
    
    # Esperar un momento para que el servidor se inicie
    print("⏳ Esperando 3 segundos para que el servidor se inicie...")
    time.sleep(3)
    
    # Ejecutar pruebas
    success = test_flask_app()
    
    if success:
        success_invalid = test_invalid_data()
        if success_invalid:
            print("\n🎉 ¡Todas las pruebas completadas exitosamente!")
        else:
            print("\n⚠️ Algunas pruebas fallaron")
    else:
        print("\n❌ Las pruebas principales fallaron")
    
    print("\n" + "=" * 50)
    print("🏁 Fin de las pruebas")
