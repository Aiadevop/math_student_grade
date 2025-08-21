#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para procesar datos del formulario Next.js de análisis educativo
"""

import json
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Configurar estilo para gráficos
plt.style.use('default')
sns.set_palette("husl")

def cargar_datos_ejemplo():
    """
    Cargar datos de ejemplo del formulario Next.js (ya transformados)
    """
    datos_ejemplo = {
        "reading_score": 85.5,
        "writing_score": 78.2,
        "lunch": 1,  # standard = 1, free/reduced = 0
        "race_ethnicity_group_E": 0,  # group E = 1, otros = 0
        "test_preparation_course": 1,  # completed = 1, none = 0
        "gender": 0,  # male = 1, female = 0
        "parental_level_of_education_high_school": 0  # high school = 1, otros = 0
    }
    return datos_ejemplo

def cargar_datos_desde_json(archivo_json):
    """
    Cargar datos desde un archivo JSON exportado por el formulario Next.js
    """
    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        return datos
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {archivo_json}")
        return None
    except json.JSONDecodeError:
        print(f"❌ Error: El archivo {archivo_json} no es un JSON válido")
        return None

def mostrar_transformacion_datos(datos):
    """
    Mostrar cómo se transformaron los datos originales
    """
    print("\n🔄 TRANSFORMACIÓN DE DATOS:")
    print("-" * 40)
    print("Datos originales → Datos numéricos:")
    print(f"reading_score: {datos['reading_score']} (numérico 0-100)")
    print(f"writing_score: {datos['writing_score']} (numérico 0-100)")
    print(f"lunch: {datos['lunch']} (0=free/reduced, 1=standard)")
    print(f"test_preparation_course: {datos['test_preparation_course']} (0=none, 1=completed)")
    print(f"gender: {datos['gender']} (0=female, 1=male)")
    print(f"race_ethnicity_group_E: {datos['race_ethnicity_group_E']} (0=otros, 1=group E)")
    print(f"parental_level_of_education_high_school: {datos['parental_level_of_education_high_school']} (0=otros, 1=high school)")

def procesar_datos_formulario(datos):
    """
    Procesar los datos del formulario y realizar análisis básico
    """
    print("=" * 60)
    print("📊 ANÁLISIS DE DATOS EDUCATIVOS - FORMULARIO NEXT.JS")
    print("=" * 60)
    
    # Convertir a DataFrame
    df = pd.DataFrame([datos])
    
    # Mostrar datos
    print("\n📋 DATOS DEL FORMULARIO:")
    print("-" * 40)
    for columna, valor in datos.items():
        print(f"{columna}: {valor}")
    
    # Análisis de puntuaciones
    print("\n📈 ANÁLISIS DE PUNTUACIONES:")
    print("-" * 40)
    reading_score = float(datos['reading_score'])
    writing_score = float(datos['writing_score'])
    
    print(f"Puntuación de lectura: {reading_score}")
    print(f"Puntuación de escritura: {writing_score}")
    print(f"Promedio: {(reading_score + writing_score) / 2:.2f}")
    
    # Análisis de rendimiento
    rendimiento_lectura = "Excelente" if reading_score >= 90 else \
                         "Bueno" if reading_score >= 80 else \
                         "Promedio" if reading_score >= 70 else "Necesita mejorar"
    
    rendimiento_escritura = "Excelente" if writing_score >= 90 else \
                           "Bueno" if writing_score >= 80 else \
                           "Promedio" if writing_score >= 70 else "Necesita mejorar"
    
    print(f"\n🎯 EVALUACIÓN DE RENDIMIENTO:")
    print("-" * 40)
    print(f"Lectura: {rendimiento_lectura}")
    print(f"Escritura: {rendimiento_escritura}")
    
    # Análisis demográfico
    print(f"\n👥 ANÁLISIS DEMOGRÁFICO:")
    print("-" * 40)
    print(f"Género: {'Masculino' if datos['gender'] == 1 else 'Femenino'}")
    print(f"Grupo étnico: {'Grupo E' if datos['race_ethnicity_group_E'] == 1 else 'Otros grupos'}")
    print(f"Tipo de almuerzo: {'Estándar' if datos['lunch'] == 1 else 'Gratuito/Reducido'}")
    print(f"Nivel educativo de los padres: {'Secundaria completa' if datos['parental_level_of_education_high_school'] == 1 else 'Otros niveles'}")
    print(f"Curso de preparación: {'Completado' if datos['test_preparation_course'] == 1 else 'Ninguno'}")
    
    return df

def generar_recomendaciones(datos):
    """
    Generar recomendaciones basadas en los datos
    """
    print(f"\n💡 RECOMENDACIONES:")
    print("-" * 40)
    
    reading_score = float(datos['reading_score'])
    writing_score = float(datos['writing_score'])
    
    # Recomendaciones basadas en puntuaciones
    if reading_score < 80:
        print("📖 Considera tomar clases adicionales de lectura")
    
    if writing_score < 80:
        print("✍️ Practica más la escritura y composición")
    
    if datos['test_preparation_course'] == 0:
        print("📚 Considera tomar un curso de preparación para mejorar tus puntuaciones")
    
    # Recomendaciones específicas por nivel educativo de los padres
    if datos['parental_level_of_education_high_school'] == 0:
        print("🎓 Considera buscar apoyo adicional para compensar la falta de experiencia universitaria en casa")
    
    # Recomendaciones generales
    print("🎯 Mantén un horario de estudio consistente")
    print("📝 Practica regularmente con ejercicios de lectura y escritura")
    print("👥 Participa en grupos de estudio para mejorar el aprendizaje")

def crear_visualizacion(datos):
    """
    Crear visualización de los datos
    """
    try:
        # Crear figura con subplots
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('📊 Análisis Educativo - Formulario Next.js', fontsize=16, fontweight='bold')
        
        # Gráfico 1: Puntuaciones por materia
        materias = ['Lectura', 'Escritura']
        puntuaciones = [float(datos['reading_score']), float(datos['writing_score'])]
        colores = ['#3B82F6', '#8B5CF6']
        
        bars = ax1.bar(materias, puntuaciones, color=colores, alpha=0.7)
        ax1.set_title('📊 Puntuaciones por Materia', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Puntuación')
        ax1.set_ylim(0, 100)
        
        # Agregar valores en las barras
        for bar, puntuacion in zip(bars, puntuaciones):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{puntuacion}', ha='center', va='bottom', fontweight='bold')
        
        # Gráfico 2: Gráfico de radar para características
        categorias = ['Lectura', 'Escritura', 'Preparación', 'Apoyo Familiar']
        valores = [
            float(datos['reading_score']) / 100,
            float(datos['writing_score']) / 100,
            1.0 if datos['test_preparation_course'] == 'completed' else 0.3,
            0.8  # Valor estimado para apoyo familiar
        ]
        
        # Cerrar el gráfico de radar
        valores += valores[:1]
        categorias += categorias[:1]
        
        angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
        angles += angles[:1]
        
        ax2.plot(angles, valores, 'o-', linewidth=2, color='#667eea')
        ax2.fill(angles, valores, alpha=0.25, color='#667eea')
        ax2.set_xticks(angles[:-1])
        ax2.set_xticklabels(categorias[:-1])
        ax2.set_ylim(0, 1)
        ax2.set_title('🎯 Perfil del Estudiante', fontsize=14, fontweight='bold')
        
        # Gráfico 3: Distribución de características demográficas
        demograficas = ['Género', 'Grupo Étnico', 'Tipo Almuerzo', 'Preparación']
        valores_demo = [
            datos['gender'],
            datos['race_ethnicity_group_E'],
            datos['lunch'],
            datos['test_preparation_course']
        ]
        
        ax3.barh(demograficas, valores_demo, color=['#10B981', '#F59E0B', '#EF4444', '#8B5CF6'])
        ax3.set_title('👥 Características Demográficas', fontsize=14, fontweight='bold')
        ax3.set_xlim(0, 1)
        
        # Gráfico 4: Comparación con estándares
        estandares = ['Excelente\n(90-100)', 'Bueno\n(80-89)', 'Promedio\n(70-79)', 'Mejorar\n(<70)']
        reading_level = 0 if reading_score >= 90 else 1 if reading_score >= 80 else 2 if reading_score >= 70 else 3
        writing_level = 0 if writing_score >= 90 else 1 if writing_score >= 80 else 2 if writing_score >= 70 else 3
        
        x = np.arange(len(estandares))
        width = 0.35
        
        ax4.bar(x - width/2, [1 if i == reading_level else 0 for i in range(4)], width, label='Lectura', color='#3B82F6')
        ax4.bar(x + width/2, [1 if i == writing_level else 0 for i in range(4)], width, label='Escritura', color='#8B5CF6')
        
        ax4.set_title('📈 Nivel de Rendimiento', fontsize=14, fontweight='bold')
        ax4.set_xticks(x)
        ax4.set_xticklabels(estandares)
        ax4.legend()
        
        plt.tight_layout()
        plt.savefig('analisis_educativo_nextjs.png', dpi=300, bbox_inches='tight')
        print(f"\n📊 Gráfico guardado como 'analisis_educativo_nextjs.png'")
        
    except Exception as e:
        print(f"⚠️ No se pudo crear la visualización: {e}")

def exportar_datos(datos, formato='json'):
    """
    Exportar datos en diferentes formatos
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if formato == 'json':
        filename = f'datos_educativos_nextjs_{timestamp}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Datos exportados como JSON: {filename}")
    
    elif formato == 'csv':
        filename = f'datos_educativos_nextjs_{timestamp}.csv'
        df = pd.DataFrame([datos])
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"\n💾 Datos exportados como CSV: {filename}")

def analisis_estadistico(datos):
    """
    Realizar análisis estadístico básico
    """
    print(f"\n📊 ANÁLISIS ESTADÍSTICO:")
    print("-" * 40)
    
    reading_score = float(datos['reading_score'])
    writing_score = float(datos['writing_score'])
    
    # Estadísticas básicas
    promedio = (reading_score + writing_score) / 2
    diferencia = abs(reading_score - writing_score)
    
    print(f"Promedio general: {promedio:.2f}")
    print(f"Diferencia entre materias: {diferencia:.2f}")
    print(f"Rendimiento relativo: {'Lectura' if reading_score > writing_score else 'Escritura'}")
    
    # Análisis de correlación (simulado)
    if reading_score > 80 and writing_score > 80:
        print("✅ Alto rendimiento en ambas materias")
    elif reading_score < 70 or writing_score < 70:
        print("⚠️ Necesita apoyo en al menos una materia")
    else:
        print("📈 Rendimiento moderado, con potencial de mejora")

def main():
    """
    Función principal
    """
    print("🚀 Iniciando análisis de datos educativos - Formulario Next.js...")
    
    # Buscar archivos JSON en el directorio actual
    json_files = list(Path('.').glob('datos_educativos_*.json'))
    
    if json_files:
        print(f"📁 Encontrados {len(json_files)} archivos de datos:")
        for i, file in enumerate(json_files, 1):
            print(f"  {i}. {file.name}")
        
        # Usar el archivo más reciente
        latest_file = max(json_files, key=lambda x: x.stat().st_mtime)
        print(f"\n📂 Usando archivo más reciente: {latest_file.name}")
        datos = cargar_datos_desde_json(latest_file)
    else:
        print("📝 No se encontraron archivos JSON, usando datos de ejemplo")
        datos = cargar_datos_ejemplo()
    
    if datos:
        # Mostrar transformación de datos
        mostrar_transformacion_datos(datos)
        
        # Procesar datos
        df = procesar_datos_formulario(datos)
        
        # Generar recomendaciones
        generar_recomendaciones(datos)
        
        # Análisis estadístico
        analisis_estadistico(datos)
        
        # Crear visualización
        crear_visualizacion(datos)
        
        # Exportar datos
        exportar_datos(datos, 'json')
        exportar_datos(datos, 'csv')
        
        print("\n" + "=" * 60)
        print("✅ Análisis completado exitosamente")
        print("=" * 60)
    else:
        print("❌ No se pudieron cargar los datos")

if __name__ == "__main__":
    main()
