#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicación Flask para predicción de calificaciones matemáticas
Reemplaza la funcionalidad de Next.js para Vercel
"""

from flask import Flask, request, jsonify, render_template_string
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
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Predicción de Calificaciones Matemáticas</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            .gradient-bg {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .card-shadow {
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body class="gradient-bg min-h-screen">
        <div class="container mx-auto px-4 py-8">
            <div class="max-w-2xl mx-auto">
                <div class="text-center mb-8">
                    <h1 class="text-4xl font-bold text-white mb-4">📊 Predicción de Calificaciones Matemáticas</h1>
                    <p class="text-white/80 text-lg">Sistema de predicción basado en Machine Learning</p>
                </div>
                
                <div class="bg-white rounded-lg card-shadow p-8">
                    <form id="predictionForm" class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <!-- Género -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Género</label>
                                <select name="gender" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required>
                                    <option value="0">Femenino</option>
                                    <option value="1">Masculino</option>
                                </select>
                            </div>
                            
                            <!-- Almuerzo -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Tipo de Almuerzo</label>
                                <select name="lunch" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required>
                                  
                                    <option value="1">Estándar</option>
                                    <option value="0">Gratuito/Reducido</option>
                                </select>
                            </div>
                            
                            <!-- Preparación del examen -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Preparación del Examen</label>
                                <select name="test_preparation_course" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required>
                                   
                                    <option value="0">Ninguna</option>
                                    <option value="1">Completado</option>
                                </select>
                            </div>
                            
                            <!-- Grupo étnico -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Grupo Étnico E</label>
                                <select name="race_ethnicity_group_E" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required>
                                   
                                    <option value="0">No</option>
                                    <option value="1">Sí</option>
                                </select>
                            </div>
                            
                            <!-- Nivel educativo de los padres -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Nivel Educativo de los Padres Solo Secundaria</label>
                                <select name="parental_level_of_education_high_school" class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" required>
                              
                                    <option value="0">Otro</option>
                                    <option value="1">Secundaria</option>
                                </select>
                            </div>
                        </div>
                        
                        <!-- Calificaciones -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Calificación de Lectura (0-100)</label>
                                <input type="number" name="reading_score" min="0" max="100" step="0.1" 
                                       class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" 
                                       placeholder="Ej: 85.5" required>
                            </div>
                            
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-2">Calificación de Escritura (0-100)</label>
                                <input type="number" name="writing_score" min="0" max="100" step="0.1" 
                                       class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" 
                                       placeholder="Ej: 82.3" required>
                            </div>
                        </div>
                        
                        <div class="text-center">
                            <button type="submit" 
                                    class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-lg transition duration-200 transform hover:scale-105">
                                🎯 Predecir Calificación Matemática
                            </button>
                        </div>
                    </form>
                    
                    <!-- Resultado -->
                    <div id="result" class="mt-8 hidden">
                        <div class="bg-gradient-to-r from-green-50 to-blue-50 border border-green-200 rounded-lg p-6">
                            <h3 class="text-xl font-semibold text-gray-800 mb-4">📊 Resultado de la Predicción</h3>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div class="text-center">
                                    <div class="text-3xl font-bold text-blue-600" id="predictedScore">--</div>
                                    <div class="text-sm text-gray-600">Calificación Predicha</div>
                                </div>
                                <div class="text-center">
                                    <div class="text-3xl font-bold text-green-600" id="confidence">--</div>
                                    <div class="text-sm text-gray-600">Confianza del Modelo</div>
                                </div>
                            </div>
                            <div class="mt-4 text-sm text-gray-600">
                                <p><strong>Información del modelo:</strong> <span id="modelInfo">--</span></p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Error -->
                    <div id="error" class="mt-8 hidden">
                        <div class="bg-red-50 border border-red-200 rounded-lg p-4">
                            <div class="flex">
                                <div class="flex-shrink-0">
                                    <svg class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                                    </svg>
                                </div>
                                <div class="ml-3">
                                    <h3 class="text-sm font-medium text-red-800" id="errorTitle">Error</h3>
                                    <div class="mt-2 text-sm text-red-700" id="errorMessage"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            document.getElementById('predictionForm').addEventListener('submit', async function(e) {
                e.preventDefault();
                
                // Ocultar resultados anteriores
                document.getElementById('result').classList.add('hidden');
                document.getElementById('error').classList.add('hidden');
                
                // Recopilar datos del formulario
                const formData = new FormData(this);
                const data = {};
                for (let [key, value] of formData.entries()) {
                    data[key] = parseFloat(value);
                }
                
                try {
                    // Enviar datos al servidor
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(data)
                    });
                    
                    const result = await response.json();
                    
                    if (response.ok) {
                        // Mostrar resultado exitoso
                        document.getElementById('predictedScore').textContent = result.math_score_prediction;
                        document.getElementById('confidence').textContent = (result.confidence * 100).toFixed(1) + '%';
                        document.getElementById('modelInfo').textContent = `${result.model_info.type} con ${result.model_info.features_used} características`;
                        document.getElementById('result').classList.remove('hidden');
                    } else {
                        // Mostrar error
                        document.getElementById('errorTitle').textContent = 'Error en la Predicción';
                        document.getElementById('errorMessage').textContent = result.error || 'Error desconocido';
                        document.getElementById('error').classList.remove('hidden');
                    }
                } catch (error) {
                    // Mostrar error de conexión
                    document.getElementById('errorTitle').textContent = 'Error de Conexión';
                    document.getElementById('errorMessage').textContent = 'No se pudo conectar con el servidor';
                    document.getElementById('error').classList.remove('hidden');
                }
            });
        </script>
    </body>
    </html>
    """
    return html_template

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
