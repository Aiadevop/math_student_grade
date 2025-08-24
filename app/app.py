#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicación Flask para predicción de calificaciones matemáticas
Reemplaza la funcionalidad de Next.js para Vercel
"""

from flask import Flask, request, jsonify, render_template_string, render_template
from flask_cors import CORS
import json
import pickle
import numpy as np
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Intentar importar joblib para mejor compatibilidad
try:
    from joblib import load as joblib_load
    JOBLIB_AVAILABLE = True
except ImportError:
    JOBLIB_AVAILABLE = False
    print("⚠️ joblib no disponible, usando pickle")

app = Flask(__name__)
CORS(app)

def cargar_modelo():
    """
    Cargar el modelo entrenado lin_reg_model_opt
    """
    try:
        # Buscar el archivo del modelo en diferentes ubicaciones posibles
        posibles_rutas = [
            'app/models/lin_reg_model_opt.pkl',  # Primera opción: carpeta app/models
            'models/lin_reg_model_opt.pkl',      # Segunda opción: carpeta models
            'model/lin_reg_model_opt.pkl',
            'lin_reg_model_opt.pkl',             # Fallback: raíz del proyecto
            '../app/models/lin_reg_model_opt.pkl',
            '../models/lin_reg_model_opt.pkl',
            '../model/lin_reg_model_opt.pkl',
            '../lin_reg_model_opt.pkl'
        ]
        
        modelo = None
        ruta_modelo = None
        
        for ruta in posibles_rutas:
            if Path(ruta).exists():
                print(f"🔍 Intentando cargar modelo desde: {ruta}")
                try:
                    # Intentar primero con joblib si está disponible
                    if JOBLIB_AVAILABLE:
                        try:
                            modelo = joblib_load(ruta)
                            ruta_modelo = ruta
                            print(f"✅ Modelo cargado exitosamente con joblib desde: {ruta}")
                            print(f"📊 Tipo de modelo: {type(modelo).__name__}")
                            break
                        except Exception as joblib_error:
                            print(f"⚠️ joblib falló, intentando pickle: {str(joblib_error)}")
                    
                    # Si joblib no funciona, intentar con pickle
                    with open(ruta, 'rb') as f:
                        # Intentar con diferentes protocolos de pickle
                        try:
                            modelo = pickle.load(f)
                        except:
                            f.seek(0)
                            modelo = pickle.load(f, encoding='latin1')
                    ruta_modelo = ruta
                    print(f"✅ Modelo cargado exitosamente con pickle desde: {ruta}")
                    print(f"📊 Tipo de modelo: {type(modelo).__name__}")
                    break
                except Exception as load_error:
                    print(f"⚠️ Error al cargar desde {ruta}: {str(load_error)}")
                    continue
        
        if modelo is None:
            raise FileNotFoundError("No se pudo cargar el modelo desde ninguna ubicación")
        
        return modelo, ruta_modelo
        
    except Exception as e:
        print(f"❌ Error al cargar el modelo: {str(e)}")
        print(f"🔧 Sugerencia: Verifica que el modelo se guardó correctamente con pickle")
        raise

def validar_datos_formulario(datos):
    """
    Validar y preparar los datos del formulario
    """
    try:
        # Variables requeridas del formulario (en el orden correcto del modelo)
        variables_requeridas = [
            'gender', 'lunch', 'test_preparation_course', 
            'reading_score', 'writing_score', 'race_ethnicity_group_E', 
            'parental_level_of_education_high_school'
        ]
        
        # Verificar que todas las variables estén presentes
        for var in variables_requeridas:
            if var not in datos:
                raise ValueError(f"Variable faltante: {var}")
        
        # Validar y convertir las variables a float
        resultado = datos.copy()
        for var in variables_requeridas:
            resultado[var] = float(datos[var])
        
        # Agregar información sobre las variables validadas
        resultado['_variables_validadas'] = variables_requeridas
        resultado['_validado'] = True
        
        return resultado
        
    except Exception as e:
        raise ValueError(f"Error al validar datos: {str(e)}")

def hacer_prediccion(datos_validados, modelo):
    """
    Hacer predicción usando el modelo cargado
    """
    try:
        # Preparar datos para el modelo (en el orden correcto)
        variables_orden = [
            'gender', 'lunch', 'test_preparation_course', 
            'reading_score', 'writing_score', 'race_ethnicity_group_E', 
            'parental_level_of_education_high_school'
        ]
        
        datos_para_modelo = [datos_validados[var] for var in variables_orden]
        
        # Convertir datos a array numpy
        datos_array = np.array(datos_para_modelo).reshape(1, -1)
        
        print(f"📊 Datos para predicción: {datos_array}")
        print(f"📊 Forma de los datos: {datos_array.shape}")
        
        # Hacer predicción
        prediccion = modelo.predict(datos_array)
        
        # Obtener el valor de la predicción (ya en escala original)
        math_score = float(prediccion[0])
        
        # Validar que el resultado esté en el rango válido (0-100)
        if math_score < 0:
            print(f"⚠️ Predicción negativa detectada: {math_score}, estableciendo en 0")
            math_score = 0
        elif math_score > 100:
            print(f"⚠️ Predicción mayor a 100 detectada: {math_score}, estableciendo en 100")
            math_score = 100
        
        print(f"🎯 Predicción final: {math_score}")
        
        # Usar la precisión real del modelo basada en validación cruzada
        # R² = 0.872151 (87.2% de precisión)
        confidence = 0.872151
        
        return {
            "math_score": round(math_score, 2),
            "confidence": round(confidence, 3) if confidence is not None else None,
            "model_info": {
                "type": type(modelo).__name__,
                "features_used": len(datos_para_modelo)
            }
        }
        
    except Exception as e:
        print(f"❌ Error en predicción: {str(e)}")
        raise

# Cargar el modelo al iniciar la aplicación
modelo = None
ruta_modelo = None

try:
    modelo, ruta_modelo = cargar_modelo()
    print(f"✅ Modelo cargado exitosamente desde: {ruta_modelo}")
except Exception as e:
    print(f"❌ Error al cargar el modelo: {e}")
    modelo = None

@app.route('/')
def index():
    """
    Página principal con el formulario HTML
    """
    return render_template('index.html')

@app.route('/api/escalar', methods=['POST'])
def escalar_datos():
    """
    Endpoint para validar y escalar datos (equivalente a /api/escalar de Next.js)
    """
    try:
        print('🌐 API de validación recibida')
        
        # Obtener datos del formulario
        datos = request.get_json()
        print('📥 Datos recibidos:', datos)
        
        # Validar datos
        datos_validados = validar_datos_formulario(datos)
        print('✅ Datos validados:', datos_validados)
        
        return jsonify(datos_validados)
        
    except ValueError as e:
        print(f'❌ Error de validación: {str(e)}')
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f'❌ Error en API de validación: {str(e)}')
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Endpoint para hacer predicciones (equivalente a /api/predict de Next.js)
    """
    try:
        print('🎯 API de predicción recibida')
        
        # Obtener datos validados
        datos = request.get_json()
        print('📥 Datos recibidos:', datos)
        
        # Verificar que el modelo esté cargado
        if modelo is None:
            return jsonify({'error': 'Modelo no disponible'}), 500
        
        # Validar datos
        datos_validados = validar_datos_formulario(datos)
        print('✅ Datos validados:', datos_validados)
        
        # Hacer predicción
        resultado_prediccion = hacer_prediccion(datos_validados, modelo)
        print('✅ Predicción realizada:', resultado_prediccion)
        
        # Combinar datos validados con la predicción
        resultado_completo = {
            **datos_validados,
            'math_score_prediction': resultado_prediccion['math_score'],
            'confidence': resultado_prediccion['confidence'],
            'model_info': resultado_prediccion['model_info']
        }
        
        return jsonify(resultado_completo)
        
    except ValueError as e:
        print(f'❌ Error de validación: {str(e)}')
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f'❌ Error en API de predicción: {str(e)}')
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/predict', methods=['POST'])
def predict_direct():
    """
    Endpoint directo para predicciones desde el formulario HTML
    """
    try:
        print('🎯 Predicción directa recibida')
        
        # Obtener datos del formulario
        datos = request.get_json()
        print('📥 Datos recibidos:', datos)
        
        # Verificar que el modelo esté cargado
        if modelo is None:
            return jsonify({'error': 'Modelo no disponible'}), 500
        
        # Validar datos
        datos_validados = validar_datos_formulario(datos)
        print('✅ Datos validados:', datos_validados)
        
        # Hacer predicción
        resultado_prediccion = hacer_prediccion(datos_validados, modelo)
        print('✅ Predicción realizada:', resultado_prediccion)
        
        # Combinar datos validados con la predicción
        resultado_completo = {
            **datos_validados,
            'math_score_prediction': resultado_prediccion['math_score'],
            'confidence': resultado_prediccion['confidence'],
            'model_info': resultado_prediccion['model_info']
        }
        
        return jsonify(resultado_completo)
        
    except ValueError as e:
        print(f'❌ Error de validación: {str(e)}')
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f'❌ Error en predicción directa: {str(e)}')
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/health')
def health_check():
    """
    Endpoint de verificación de salud
    """
    return jsonify({
        'status': 'healthy',
        'model_loaded': modelo is not None,
        'model_path': ruta_modelo
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
