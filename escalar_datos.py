#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple para escalar datos del formulario educativo usando StandardScaler
con los parámetros exactos del modelo original (solo variables utilizadas)
"""

import json
import pandas as pd
import numpy as np
import sys

def escalar_datos_formulario(datos_json):
    """
    Preparar los datos del formulario sin escalar (el modelo fue entrenado sin escalar)
    """
    try:
        # Cargar datos desde JSON
        datos = json.loads(datos_json)
        
        # Variables numéricas del formulario (en el orden correcto del modelo)
        variables_numericas = ['gender', 'lunch', 'test_preparation_course', 
                              'reading_score', 'writing_score', 'race_ethnicity_group_E', 
                              'parental_level_of_education_high_school']
        
        # NO escalar las variables - usar valores originales
        resultado = datos.copy()
        for var in variables_numericas:
            resultado[var] = float(datos[var])
        
        # Agregar información sobre las variables (sin escalar)
        resultado['_variables_escaladas'] = variables_numericas
        resultado['_escalado'] = False  # Indicar que no se escalaron
        
        return resultado
        
    except Exception as e:
        return {"error": f"Error al escalar datos: {str(e)}"}

if __name__ == "__main__":
    # Leer datos desde stdin o argumento
    if len(sys.argv) > 1:
        datos_json = sys.argv[1]
    else:
        datos_json = sys.stdin.read().strip()
    
    # Escalar datos
    resultado = escalar_datos_formulario(datos_json)
    
    # Devolver resultado como JSON
    print(json.dumps(resultado, ensure_ascii=False))
