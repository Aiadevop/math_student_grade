#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para hacer predicciones de math_score usando el modelo lin_reg_model_opt
"""

import json
import sys
import pickle
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Intentar importar joblib para mejor compatibilidad
try:
    from joblib import load as joblib_load
    JOBLIB_AVAILABLE = True
except ImportError:
    JOBLIB_AVAILABLE = False
    print("⚠️ joblib no disponible, usando pickle", file=sys.stderr)

def cargar_modelo():
    """
    Cargar el modelo entrenado lin_reg_model_opt
    """
    try:
        # Buscar el archivo del modelo en diferentes ubicaciones posibles
        posibles_rutas = [
            'lin_reg_model_opt.pkl',
            'model/lin_reg_model_opt.pkl',
            'models/lin_reg_model_opt.pkl',
            '../lin_reg_model_opt.pkl',
            '../model/lin_reg_model_opt.pkl',
            '../models/lin_reg_model_opt.pkl'
        ]
        
        modelo = None
        ruta_modelo = None
        
        for ruta in posibles_rutas:
            if Path(ruta).exists():
                print(f"🔍 Intentando cargar modelo desde: {ruta}", file=sys.stderr)
                try:
                    # Intentar primero con joblib si está disponible
                    if JOBLIB_AVAILABLE:
                        try:
                            modelo = joblib_load(ruta)
                            ruta_modelo = ruta
                            print(f"✅ Modelo cargado exitosamente con joblib desde: {ruta}", file=sys.stderr)
                            print(f"📊 Tipo de modelo: {type(modelo).__name__}", file=sys.stderr)
                            break
                        except Exception as joblib_error:
                            print(f"⚠️ joblib falló, intentando pickle: {str(joblib_error)}", file=sys.stderr)
                    
                    # Si joblib no funciona, intentar con pickle
                    with open(ruta, 'rb') as f:
                        # Intentar con diferentes protocolos de pickle
                        try:
                            modelo = pickle.load(f)
                        except:
                            f.seek(0)
                            modelo = pickle.load(f, encoding='latin1')
                    ruta_modelo = ruta
                    print(f"✅ Modelo cargado exitosamente con pickle desde: {ruta}", file=sys.stderr)
                    print(f"📊 Tipo de modelo: {type(modelo).__name__}", file=sys.stderr)
                    break
                except Exception as load_error:
                    print(f"⚠️ Error al cargar desde {ruta}: {str(load_error)}", file=sys.stderr)
                    continue
        
        if modelo is None:
            raise FileNotFoundError("No se pudo cargar el modelo desde ninguna ubicación")
        
        return modelo, ruta_modelo
        
    except Exception as e:
        print(f"❌ Error al cargar el modelo: {str(e)}", file=sys.stderr)
        print(f"🔧 Sugerencia: Verifica que el modelo se guardó correctamente con pickle", file=sys.stderr)
        raise

def hacer_prediccion(datos_escalados, modelo):
    """
    Hacer predicción usando el modelo cargado
    """
    try:
        # Convertir datos a array numpy
        datos_array = np.array(datos_escalados).reshape(1, -1)
        
        print(f"📊 Datos para predicción: {datos_array}", file=sys.stderr)
        print(f"📊 Forma de los datos: {datos_array.shape}", file=sys.stderr)
        
        # Hacer predicción
        prediccion = modelo.predict(datos_array)
        
        # Obtener el valor de la predicción (ya en escala original)
        math_score = float(prediccion[0])
        
        # Validar que el resultado esté en el rango válido (0-100)
        if math_score < 0:
            print(f"⚠️ Predicción negativa detectada: {math_score}, estableciendo en 0", file=sys.stderr)
            math_score = 0
        elif math_score > 100:
            print(f"⚠️ Predicción mayor a 100 detectada: {math_score}, estableciendo en 100", file=sys.stderr)
            math_score = 100
        
        print(f"🎯 Predicción final: {math_score}", file=sys.stderr)
        
        # Usar la precisión real del modelo basada en validación cruzada
        # R² = 0.872151 (87.2% de precisión)
        confidence = 0.872151
        
        return {
            "math_score": round(math_score, 2),
            "confidence": round(confidence, 3) if confidence is not None else None,
            "model_info": {
                "type": type(modelo).__name__,
                "features_used": len(datos_escalados)
            }
        }
        
    except Exception as e:
        print(f"❌ Error en predicción: {str(e)}", file=sys.stderr)
        raise

def main():
    """
    Función principal
    """
    try:
        # Leer datos desde stdin o argumento
        if len(sys.argv) > 1:
            datos_json = sys.argv[1]
        else:
            datos_json = sys.stdin.read().strip()
        
        print(f"📥 Datos recibidos: {datos_json}", file=sys.stderr)
        
        # Parsear datos JSON
        datos_escalados = json.loads(datos_json)
        
        print(f"✅ Datos parseados: {datos_escalados}", file=sys.stderr)
        
        # Verificar que tenemos 7 variables
        if len(datos_escalados) != 7:
            raise ValueError(f"Se esperaban 7 variables, se recibieron {len(datos_escalados)}")
        
        # Cargar modelo
        modelo, ruta_modelo = cargar_modelo()
        
        # Hacer predicción
        resultado = hacer_prediccion(datos_escalados, modelo)
        
        # Agregar información adicional
        resultado["datos_entrada"] = datos_escalados
        resultado["ruta_modelo"] = ruta_modelo
        
        # Devolver resultado como JSON
        print(json.dumps(resultado, ensure_ascii=False))
        
    except Exception as e:
        error_result = {
            "error": str(e),
            "tipo_error": type(e).__name__
        }
        print(json.dumps(error_result, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    main()
