#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple para validar datos del formulario educativo
con los parámetros exactos del modelo original (solo variables utilizadas)
"""

import json
import pandas as pd
import numpy as np
import sys

def validar_datos_formulario(datos_json):
    """
    Validar y preparar los datos del formulario (el modelo fue entrenado sin escalar)
    """
    try:
        # Cargar datos desde JSON
        datos = json.loads(datos_json)
        
        # Variables numéricas del formulario (en el orden correcto del modelo)
        variables_numericas = ['gender', 'lunch', 'test_preparation_course', 
                              'reading_score', 'writing_score', 'race_ethnicity_group_E', 
                              'parental_level_of_education_high_school']
        
        # Validar y convertir las variables a float
        resultado = datos.copy()
        for var in variables_numericas:
            resultado[var] = float(datos[var])
        
        # Agregar información sobre las variables validadas
        resultado['_variables_validadas'] = variables_numericas
        resultado['_validado'] = True  # Indicar que se validaron correctamente
        
        return resultado
        
    except Exception as e:
        return {"error": f"Error al validar datos: {str(e)}"}

if __name__ == "__main__":
    # Leer datos desde stdin o argumento
    if len(sys.argv) > 1:
        datos_json = sys.argv[1]
    else:
        datos_json = sys.stdin.read().strip()
    
    # Validar datos
    resultado = validar_datos_formulario(datos_json)
    
    # Devolver resultado como JSON
    print(json.dumps(resultado, ensure_ascii=False))
